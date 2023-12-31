import tkinter as tk
from components.login import *

def main():
    root = tk.Tk()
    
    ### FRAME ###
    window_height = 400
    window_width = 600

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws-window_width)/2
    y = (hs-window_height)/2

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
    root.resizable(False, False)
    
    root.title('ĐỒ ÁN CUỐI KỲ')
    ###

    mainframe = tk.Frame(root, name='mainframe', width=window_width, height=window_height)

    ### MAIN ###

    menu = login(mainframe)

    root.mainloop()

if __name__ == '__main__':
    main()