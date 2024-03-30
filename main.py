import tkinter as tk
from start_page import Start_page


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('600x800')
    win.title('Health keeper')
    m = Start_page(win)