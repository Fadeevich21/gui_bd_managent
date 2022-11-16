from libs.gui import Gui
import tkinter as tk 


if __name__ == "__main__":
   root = tk.Tk()
   app = Gui(root)
   app.pack()
   root.title('Л/р №6')
   root.geometry('1000x600')
   root.mainloop()
