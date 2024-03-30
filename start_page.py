import tkinter as tk
from PIL import ImageTk, Image
from enter_page import Enter_page

class Start_page():
    def __init__(self, win):
        self.win = win

        #以下為印出label和button的code
        self.frame = tk.Frame(self.win)
        self.frame.grid()

        img_bak = Image.open('picture/image/background1.jpg').resize((600, 800))
        photo_bak = ImageTk.PhotoImage(img_bak)
        self.bak = tk.Canvas(self.frame, width=600, height=800)
        self.bak.grid()
        self.bak.create_image(0, 0, anchor=tk.NW, image = photo_bak)

        self.button_next = tk.Button(self.frame, width = 7, height = 1, text = 'Next', \
                                      font=('Arial', 18), borderwidth = -2 , command = self.next_page)
        self.bak.create_window(450, 720, anchor=tk.NW, window=self.button_next)
        #到此為印出label和button的code

        self.frame.mainloop()
    
    def next_page(self):
        self.frame.destroy()
        Enter_page(self.win)
        self.frame.quit()

        # Try again start initialize
        self.__init__(self.win)

#test
if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('600x800')
    win.title('Health keeper')
    m = Start_page(win)