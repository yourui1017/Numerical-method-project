import tkinter as tk
from PIL import ImageTk, Image
from diet_page import Diet_page
from PSO_find_calorie import PSOSolver


class Calorie_page:
    def __init__(self, win, gender_value, work_value, height_value, weight_value, age_value):
        self.win = win

        #暫存三餐的資訊
        self.breakfast_list = []
        self.breakfast_calorie_sum = 0
        self.lunch_list = []
        self.lunch_calorie_sum = 0
        self.dinner_list = []
        self.dinner_calorie_sum = 0

        #暫存user輸入的值的parameter
        self.gender_value = gender_value
        self.work_value = work_value
        self.height_value = height_value
        self.weight_value = weight_value
        self.age_value = age_value

        #BMR(基礎代謝率)
        self.bmr_value = 0

        #TDEE(一日熱量需求)
        self.tdee_value = 0

        self.bmr_calculate()
        self.tdee_calculate()

        #以下為創建label, button, text, combobox的程式碼
        self.frame = tk.Frame(self.win)
        self.frame.grid()

        img_bak = Image.open('picture/image/background4.jpg').resize((600, 800))
        photo_bak = ImageTk.PhotoImage(img_bak)
        self.bak = tk.Canvas(self.frame, width=600, height=800)
        self.bak.grid()
        self.bak.create_image(0, 0, anchor=tk.NW, image = photo_bak)


        imformation_str = f'你的基礎代謝(BMR){self.bmr_value} 大卡,\n\n因{self.work_value},\n\n每日所需總熱量約{self.tdee_value} 大卡'
        self.label_bmr = tk.Label(self.frame, text = imformation_str, justify = 'left' , bg = 'White', borderwidth=1, font=('microsoft yahei', 16))
        self.bak.create_window(90, 168, anchor=tk.NW, window=self.label_bmr)

        self.calculate_btn = tk.Button(self.frame, width = 8, height = 1, text = 'Next', \
                                      font=('Arial', 18), borderwidth = -2, command = self.check_go_to_next_step)
        self.bak.create_window(230, 730, anchor=tk.NW, window=self.calculate_btn)
        #到此為創建label, button, text, combobox的程式碼 


        #計算卡路里
        self.calorie_calculate()
        self.frame.mainloop()


    def bmr_calculate(self):
        '''Calculate bmr value'''
        if self.gender_value == '女性':
            self.bmr_value = 655 + (9.6*self.weight_value) + (1.8*self.height_value) - (4.7*self.age_value)
        else:
            self.bmr_value = 66+ (13.7*self.weight_value) + (5*self.height_value) - (6.8*self.age_value)

        self.bmr_value = round(self.bmr_value, 2)
        
        return self.bmr_value

    def tdee_calculate(self):
        '''calculate tdee value'''
        activity_multi = 0
        if self.work_value == '幾乎很少或坐著沒運動':
            activity_multi = 1.2
        elif self.work_value == '每周運動1-2次':
            activity_multi = 1.375
        elif self.work_value == '每周運動3-5次':
            activity_multi = 1.55
        elif self.work_value == '每周運動6-7次':
            activity_multi = 1.725
        else:
            activity_multi = 1.9
        
        self.tdee_value = activity_multi*self.bmr_value

        self.tdee_value = round(self.tdee_value, 2)
        return self.tdee_value

    def check_go_to_next_step(self):
        self.frame.destroy()
        Diet_page(self.win, self.breakfast_list, self.breakfast_calorie_sum, self.lunch_list, self.lunch_calorie_sum, self.dinner_list, self.dinner_calorie_sum)
        self.frame.quit()

    def calorie_calculate(self):
        '''計算三餐的資訊'''
        plant_input  = (self.tdee_value + self.bmr_value)/2
        #將一天的三餐熱量分為1:1.5:1.5
        self.breakfast_value = plant_input*0.25
        self.lunch_value = plant_input*0.375
        self.dinner_value = plant_input*0.375

        #進入PSO求取最佳值
        solver_breakfast = PSOSolver(self.breakfast_value)
        self.breakfast_list, self.breakfast_calorie_sum = solver_breakfast.select('breakfast')
        solver_lunch = PSOSolver(self.lunch_value)
        self.lunch_list, self.lunch_calorie_sum= solver_lunch.select('lunch')
        solver_dinner = PSOSolver(self.dinner_value)
        self.dinner_list, self.dinner_calorie_sum= solver_dinner.select('dinner')
