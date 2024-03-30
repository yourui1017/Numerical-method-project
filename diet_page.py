import tkinter as tk
from PIL import ImageTk, Image


class Diet_page:
    def __init__(self, win, breakfast_list, breakfast_calorie_sum, lunch_list, lunch_calorie_sum, dinner_list, dinner_calorie_sum):
        self.win = win

        #暫存三餐的資訊
        self.breakfast_list = breakfast_list
        self.breakfast_calorie_sum = breakfast_calorie_sum
        self.lunch_list = lunch_list
        self.lunch_calorie_sum = lunch_calorie_sum
        self.dinner_list = dinner_list 
        self.dinner_calorie_sum = dinner_calorie_sum

        #以下為創建label, button, text, combobox的程式碼

        self.frame = tk.Frame(self.win)
        self.frame.grid()

        img_bak = Image.open('picture/image/background5.jpg').resize((600, 800))
        photo_bak = ImageTk.PhotoImage(img_bak)
        self.bak = tk.Canvas(self.frame, width=600, height=800)
        self.bak.grid()
        self.bak.create_image(0, 0, anchor=tk.NW, image = photo_bak)

        self.label_breakfast_title = tk.Label(self.frame, text = 'Breakfast',  bg = 'White',font=('Arial', 18))
        self.bak.create_window(350, 140, anchor=tk.NW, window=self.label_breakfast_title)

        breakfast_str = f'Main: {self.breakfast_list[0][0]} \nSide: {self.breakfast_list[1][0]}\nDrink: {self.breakfast_list[2][0]}\nTotal calorie: {self.breakfast_calorie_sum}kcal'
        self.label_breakfast = tk.Label(self.frame, text = breakfast_str, justify = 'left' , bg = 'White', font=('Arial', 14))
        self.bak.create_window(190, 180, anchor=tk.NW, window=self.label_breakfast)

        self.label_lunch_title = tk.Label(self.frame, text = 'Lunch', bg = 'White',font=('Arial', 18))
        self.bak.create_window(350, 325, anchor=tk.NW, window=self.label_lunch_title)

        lunch_str = f'Main: {self.lunch_list[0][0]} \nSide: {self.lunch_list[1][0]}\nDrink: {self.lunch_list[2][0]}\nTotal calorie: {self.lunch_calorie_sum}kcal'
        self.label_lunch = tk.Label(self.frame, text = lunch_str, justify = 'left' , bg = 'White', font=('Arial', 14))
        self.bak.create_window(190, 365, anchor=tk.NW, window=self.label_lunch)

        self.label_dinner_title = tk.Label(self.frame, text = 'Dinner', bg = 'White', font=('Arial', 18))
        self.bak.create_window(350, 510, anchor=tk.NW, window=self.label_dinner_title)

        dinner_str = f'Main: {self.dinner_list[0][0]} \nSide: {self.dinner_list[1][0]}\nDrink: {self.dinner_list[2][0]}\nTotal calorie: {self.dinner_calorie_sum}kcal'
        self.label_dinner = tk.Label(self.frame, text = dinner_str, justify = 'left' , bg = 'White', font=('Arial', 14))
        self.bak.create_window(190, 550, anchor=tk.NW, window=self.label_dinner)

        self.label_lunch_calorie = tk.Label(self.frame, text = f'Sum of calorie: {self.breakfast_calorie_sum+self.lunch_calorie_sum+self.dinner_calorie_sum}kcal', bg = 'White',font=('Arial', 16))
        self.bak.create_window(170, 680, anchor=tk.NW, window=self.label_lunch_calorie)

        self.calculate_btn = tk.Button(self.frame, width = 8, height = 1, text = 'Try again', \
                                      font=('Arial', 18), borderwidth = -2, command = self.try_again)
        self.bak.create_window(450, 720, anchor=tk.NW, window=self.calculate_btn) 

        #到此為創建label, button, text, combobox的程式碼

        self.frame.mainloop()
    
    def try_again(self):
        self.frame.destroy()
        self.frame.quit()
