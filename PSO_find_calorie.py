import random
import sys
import pandas as pd
#%%
class PSOSolver():
    def __init__(self,plant_input, propotion=0.3, dimension=3,iteration=300, pop_size=300,
               cognition_factor=1,social_factor=1,weight=0.5):

        self.plant_input = plant_input
        self.err = 0
        self.input_list = []
        self.tolerance = 50

        self.iteration = iteration
        self.pop_size = pop_size
        self.dimension = dimension
        self.propotion = propotion
        self.upper_bounds = [plant_input]*dimension
        self.lower_bounds = [0]*dimension
        self.weight = weight
        self.cognition_factor = cognition_factor #particle movement follows its own search experience
        self.social_factor = social_factor  #particle movement follows the swarm search experience

        
        self.solutions = [] #current solution
        self.individual_best_solution = [] #individual best solution
        self.individual_best_objective_value = [] #individual best val
        
        self.global_best_solution = [] #global best solution
        self.global_best_objective_value = sys.float_info.max
                
        self.global_best_arr = []
        self.idiv_gen_average = 0
        self.global_gen_average = []
        self.obj_val = 0
        self.v = 0
        self.initialize()

    def initialize(self):
        for i in range(self.pop_size):
            solution = []
            for d in range(self.dimension):
                rand_pos = self.lower_bounds[d]+random.random()*(self.upper_bounds[d]-self.lower_bounds[d])
                solution.append(rand_pos)

            self.solutions.append(solution)
            
            #update invidual best solution
            self.individual_best_solution.append(solution)
            objective = self.compute_objective_value(solution)
            self.individual_best_objective_value.append(objective)
            
        #udpate so far the best solution
        self.global_best_solution = solution
        self.global_best_objective_value = objective
        
    def move_to_new_positions(self):
        #print(f'{self.global_best_solution}ooo')
        for i,solution in enumerate(self.solutions):
            alpha = self.cognition_factor*0.2
            beta = self.social_factor*0.2
            for d in range(self.dimension):
                self.v = self.v*self.weight + alpha*(self.individual_best_solution[i][d]-self.solutions[i][d])+\
                    beta*(self.global_best_solution[d]-self.solutions[i][d])
                
                #set velocity limit
                self.v = min(self.v, 0.5)
                self.v = max(self.v, -0.5)
                self.solutions[i][d] += self.v
                self.solutions[i][d] = min(self.solutions[i][d],self.upper_bounds[d])
                self.solutions[i][d] = max(self.solutions[i][d],self.lower_bounds[d])
    
    def update_best_solution(self):
        for i,solution in enumerate(self.solutions):
            self.obj_val = self.compute_objective_value(solution)

            #udpate indivisual solution
            if(self.obj_val < self.individual_best_objective_value[i]):
                self.individual_best_solution[i] = solution
                self.individual_best_objective_value[i] = self.obj_val
                
                if(self.obj_val < self.global_best_objective_value):
                    self.global_best_solution = solution
                    self.global_best_objective_value = self.obj_val
                    self.err = abs(self.plant_input - sum(self.global_best_solution))
                    
    #cost function
    def compute_objective_value(self, array):
        #計算最接近一餐中main meal,side meal 和 drink的熱量
        val = 0
        multi_1 = random.uniform(0.6, 0.8)
        multi_2 = random.uniform(self.propotion, multi_1)
        multi_3 = 1 - multi_1 - multi_2
        self.input_list = [self.plant_input*multi_1, self.plant_input*multi_2, self.plant_input*multi_3]
        for i in range(len(array)):
            val = val + (array[i] - self.input_list[i])**2 + abs(self.plant_input - sum(array))
        return val
                    
    def do_pso(self):
        for iter in range(self.iteration):
            self.move_to_new_positions()
            self.update_best_solution()
            self.global_best_arr.append(self.global_best_objective_value)

        print(f'gbest_fit: {self.global_best_objective_value}')
        print(f'gbest_pos: {self.global_best_solution}')
        print(self.plant_input - sum(self.global_best_solution))


    def select(self, which):
        #尋找最為接近最佳值熱量的餐點
        if which == 'breakfast':
            df_main = pd.read_csv('dataset/dataset_breakfast_main.csv', index_col = 'items', encoding = 'unicode_escape')
            df_main = df_main[df_main['calorie'].notna()]
            data_main = df_main.iloc[:,0]

            df_side = pd.read_csv('dataset/dataset_breakfast_side.csv', index_col = 'items', encoding = 'unicode_escape')
            df_side = df_side[df_side['calorie'].notna()]
            data_side = df_side.iloc[:,0]

            df_drink = pd.read_csv('dataset/dataset_breakfast_drink.csv', index_col = 'items', encoding = 'unicode_escape')
            df_drink = df_drink[df_drink['calorie'].notna()]
            data_drink = df_drink.iloc[:,0]
        
        else:
            df_main = pd.read_csv('dataset/dataset_lunch_main.csv', index_col = 'items', encoding = 'unicode_escape')
            df_main = df_main[df_main['calorie'].notna()]
            data_main = df_main.iloc[:,0]

            df_side = pd.read_csv('dataset/dataset_lunch_side.csv', index_col = 'items', encoding = 'unicode_escape')
            df_side = df_side[df_side['calorie'].notna()]
            data_side = df_side.iloc[:,0]

            df_drink = pd.read_csv('dataset/dataset_lunch_drink.csv', index_col = 'items', encoding = 'unicode_escape')
            df_drink = df_drink[df_drink['calorie'].notna()]
            data_drink = df_drink.iloc[:,0]

        self.do_pso()
        menu =[]
        menu_calorie = 0
        for i in range(len(self.global_best_solution)):
            err = 500
            if i == 0:
                for j in range(len(data_main)):
                    if abs(self.global_best_solution[i] - data_main[j]) < err:
                        err = abs(self.global_best_solution[i] - data_main[j])
                        tag = data_main[j]
            elif i == 1:
                for j in range(len(data_side)):
                    if abs(self.global_best_solution[i] - data_side[j]) < err:
                        err = abs(self.global_best_solution[i] - data_side[j])
                        tag = data_side[j]
            else:
                for j in range(len(data_drink)):
                    if abs(self.global_best_solution[i] - data_drink[j]) < err:
                        err = abs(self.global_best_solution[i] - data_drink[j])
                        tag = data_drink[j]
            if i == 0:
                df = df_main
            elif i == 1:
                df = df_side
            else:
                df = df_drink
            menu_calorie = menu_calorie + tag
            menu.append(df.index[df['calorie'] == tag].tolist())

        print(menu_calorie)
        print(menu)
        return menu, menu_calorie
