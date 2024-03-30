import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from BMI_page import Bmi_page
import re 

class Enter_page:
    def __init__(self, win):
        self.win = win
        self.win_err = None
        
        #判斷是否可以前往下一頁
        self.fail_height = 1
        self.fail_weight = 1
        self.fail_age = 1

        #暫存user輸入的值的parameter
        self.gender_value = None
        self.work_value = None
        self.height_value = 0
        self.weight_value = 0
        self.age_value = 0


        #以下為創建label, button, text, combobox的程式碼
        self.frame = tk.Frame(self.win)
        self.frame.grid()

        img_bak = Image.open('picture/image/background2.jpg').resize((600, 800))
        photo_bak = ImageTk.PhotoImage(img_bak)
        self.bak = tk.Canvas(self.frame, width=600, height=800)
        self.bak.grid()
        self.bak.create_image(0, 0, anchor=tk.NW, image = photo_bak)

        self.label_gender = tk.Label(self.frame, text='Gender: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 420, anchor=tk.NW, window=self.label_gender)
        self.combobox_gender = ttk.Combobox(self.frame, values = ['男性',
                                                                   '女性'], font=('Symbol', 14))
        self.combobox_gender.current(0)
        self.bak.create_window(220, 420, anchor=tk.NW, window=self.combobox_gender)

        self.label_work = tk.Label(self.frame, text='Exercise: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 475, anchor=tk.NW, window=self.label_work)

        self.combobox_work = ttk.Combobox(self.frame, values = ['幾乎很少或坐著沒運動', 
                                                                   '每周運動1-2次',
                                                                   '每周運動3-5次',
                                                                   '每周運動6-7次',
                                                                   '每天高度運動',
                                                                   ], font=('Symbol', 14))
        self.combobox_work.current(0)
        self.bak.create_window(220, 475, anchor=tk.NW, window=self.combobox_work)    

        self.label_height = tk.Label(self.frame, text='Height: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 530, anchor=tk.NW, window=self.label_height)    
        self.text_height = tk.Text(self.frame, width = 20, height = 1, font=('Symbol', 14), border = 2)
        self.bak.create_window(220, 530, anchor=tk.NW, window=self.text_height)  
        self.label_height_unit = tk.Label(self.frame, text='cm', bg = 'White', font=('Arial', 14))
        self.bak.create_window(430, 530, anchor=tk.NW, window=self.label_height_unit)   


        self.label_weight = tk.Label(self.frame, text='Weight: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 585, anchor=tk.NW, window=self.label_weight)    
        self.text_weight = tk.Text(self.frame, width = 20, height = 1, font=('Symbol', 14), border = 2)
        self.bak.create_window(220, 585, anchor=tk.NW, window=self.text_weight)
        self.label_weight_unit = tk.Label(self.frame, text='kg', bg = 'White', font=('Arial', 14))
        self.bak.create_window(430, 585, anchor=tk.NW, window=self.label_weight_unit)       


        self.label_age = tk.Label(self.frame, text='Age: ', bg = 'White', font=('Arial', 14))
        self.bak.create_window(100, 640, anchor=tk.NW, window=self.label_age)    
        self.text_age = tk.Text(self.frame, width = 20, height = 1, font=('Symbol', 14), border = 2)
        self.bak.create_window(220, 640, anchor=tk.NW, window=self.text_age)  
        self.label_age_unit = tk.Label(self.frame, text='years old', bg = 'White', font=('Arial', 14))
        self.bak.create_window(430, 640, anchor=tk.NW, window=self.label_age_unit)     

        self.calculate_btn = tk.Button(self.frame, width = 8, height = 1, text = 'Next', \
                                      font=('Arial', 18), borderwidth = -2, command = self.check_go_to_next_step)
        self.bak.create_window(450, 720, anchor=tk.NW, window=self.calculate_btn)    

        #到此為創建label, button, text, combobox的程式碼

        self.frame.mainloop()        

    def check_gender_combobox(self):
        '''檢查combobox是否有輸入'''
        self.gender_value = self.combobox_gender.get()


    def check_work_combobox(self):
        '''檢查combobox是否有輸入'''
        self.work_value = self.combobox_work.get()



    def check_height_text(self):
        '''檢查text是否有輸入'''
        check = self.get_num(self.text_height.get('1.0', 'end-1c'))
        if check is not None:   
            self.height_value = check
            self.fail_height = 0
        else:
            self.fail_height = 1


    def check_weight_text(self):
        '''檢查text是否有輸入'''
        check = self.get_num(self.text_weight.get('1.0', 'end-1c'))
        if check is not None:   
            self.weight_value = check
            self.fail_weight = 0
        else:
            self.fail_weight = 1

    def check_age_text(self):
        '''檢查text是否有輸入'''
        check = self.get_num(self.text_age.get('1.0', 'end-1c'))
        if check is not None:   
            self.age_value = check
            self.fail_age = 0
        else:
            self.fail_age = 1

    def create_err_message(self):
        '''跳出錯誤訊息'''
        self.win_err = tk.Tk()
        self.win_err.geometry('260x100')
        self.win_err.title('err')
            
        frame0 = tk.Frame(self.win_err)
        frame0.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = tk.W)

        frame1 = tk.Frame(self.win_err)
        frame1.grid(row = 1, column = 0, padx = 25, pady = 35, sticky = tk.W)
        label_gender = tk.Label(frame1, text='Error:Please enter your data', font=('Arial', 12))
        label_gender.grid(row = 0, column = 0, sticky = tk.W)

    def check_go_to_next_step(self):
        '''檢查所有輸入都有值'''
        self.check_gender_combobox()
        self.check_work_combobox()
        self.check_height_text()
        self.check_weight_text()
        self.check_age_text()

        if self.fail_age == 0 and self.fail_height ==0 and self.fail_weight == 0:
            self.frame.destroy()
            Bmi_page(self.win, self.gender_value, self.work_value, self.height_value, self.weight_value, self.age_value)
            self.frame.quit()
        else:
            self.create_err_message()

    def get_num(self, str):
        if re.sub("\s", "", str) == '':
            return None
        else:
            return re.sub("\s", "", str)

if __name__ == '__main__':
    win = tk.Tk()
    m = Enter_page(win)
