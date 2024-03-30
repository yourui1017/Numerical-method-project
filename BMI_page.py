import tkinter as tk
from PIL import ImageTk, Image
from calorie_page import Calorie_page


class Bmi_page:
    def __init__(self, win, gender_value, work_value, height_value, weight_value, age_value):
        self.win = win

        #判斷是否可以前往前/後頁
        self.fail_to_move_on = 1
        self._go_back = 0

        #暫存user輸入的值的parameter
        self.gender_value = gender_value
        self.work_value = work_value
        self.height_value = height_value
        self.weight_value = weight_value
        self.age_value = age_value
        
        self.bmi_value = self.calculate_bmi()


        #以下為創建label, button, text, combobox的程式碼
        self.frame = tk.Frame(self.win)
        self.frame.grid()

        img_bak = Image.open('picture/image/background3.jpg').resize((600, 800))
        photo_bak = ImageTk.PhotoImage(img_bak)
        self.bak = tk.Canvas(self.frame, width=600, height=800)
        self.bak.grid()
        self.bak.create_image(0, 0, anchor=tk.NW, image = photo_bak)

        self.label_height = tk.Label(self.frame, text='Height: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 170, anchor=tk.NW, window=self.label_height)
        self.label_height_value = tk.Label(self.frame, text=self.height_value, width = 20, height = 1, bg = 'White', borderwidth=1, relief="groove", font=('Lucida Console', 14))
        self.bak.create_window(220, 170, anchor=tk.NW, window=self.label_height_value)
        self.label_height_unit = tk.Label(self.frame, text='cm', bg = 'White', font=('Arial', 14))
        self.bak.create_window(450, 170, anchor=tk.NW, window=self.label_height_unit)   

        self.label_weight = tk.Label(self.frame, text='Weight: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 230, anchor=tk.NW, window=self.label_weight)
        self.label_weight_value = tk.Label(self.frame, text=self.weight_value, width = 20, height = 1, bg = 'White', borderwidth=1, relief="groove", font=('Lucida Console', 14))
        self.bak.create_window(220, 230, anchor=tk.NW, window=self.label_weight_value)
        self.label_weight_unit = tk.Label(self.frame, text='kg', bg = 'White', font=('Arial', 14))
        self.bak.create_window(450, 230, anchor=tk.NW, window=self.label_weight_unit)   

        self.label_bmi = tk.Label(self.frame, text='BMI: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 290, anchor=tk.NW, window=self.label_bmi)
        self.label_bmi_value = tk.Label(self.frame, text=f'{self.bmi_value}', width = 20, height = 1, bg = 'White', borderwidth=1, relief="groove", font=('Lucida Console', 14))
        self.bak.create_window(220, 290, anchor=tk.NW, window=self.label_bmi_value)

        self.calculate_btn = tk.Button(self.frame, width = 8, height = 1, text = 'Next', \
                                      font=('Arial', 18), borderwidth = -2, command = self.check_go_to_next_step)
        self.bak.create_window(450, 720, anchor=tk.NW, window=self.calculate_btn) 
        #到此為創建label, button, text, combobox的程式碼
        

        self.frame.mainloop()

    def calculate_bmi(self):
        '''Calculate bmi value'''
        self.height_value = float(self.height_value)
        self.weight_value = float(self.weight_value)
        self.age_value = float(self.age_value)
        bmi_value = round(self.weight_value / (self.height_value/100)**2, 2)
        return bmi_value

    def check_go_to_next_step(self):
        self.frame.destroy()
        Calorie_page(self.win, self.gender_value, self.work_value, self.height_value, self.weight_value, self.age_value)
        self.frame.quit()

