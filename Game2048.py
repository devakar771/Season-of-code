import tkinter as tk
from tkinter import Frame,ttk,Label
import tensorflow as tf
from Game import *
from tkinter.messagebox import showinfo

path = r'content\bestWeights\bestWt'
SIZE = 4
PADX = 10
PADY = 10   
WIN_SIZE = 500

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }

CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }

FONT = ("Verdana", 35, "bold")

model = tf.keras.models.load_model(path)

class InputFrame(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid_cells = []
        self.cell_size = WIN_SIZE//SIZE
        self.init_matrix()
        self.init_grid()
        self.after(20,self.move)

    def init_grid(self):
        for i in range(4):
            gridRow = []
            for j in range(4):
                cell = Frame(self,bg=BACKGROUND_COLOR_CELL_EMPTY,width=self.cell_size-20,height=self.cell_size-20)
                cell.grid(row=i,column=j,padx=10,pady=10)
                z = Label(self,text="",bg=BACKGROUND_COLOR_CELL_EMPTY,justify='center',width=10,height=5)
                z.grid(row=i,column=j)
                gridRow.append(z)
            self.grid_cells.append(gridRow)
    
    def init_matrix(self):
        self.matrix = game2048(SIZE)
        self.matrix = add2(self.matrix,SIZE)
        self.matrix = add2(self.matrix,SIZE)

    def update(self):
        for i in range(SIZE):
            for j in range(SIZE):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()
    
    def move(self):
        out = model.predict(getInput(self.matrix,SIZE))
        self.matrix,_ = RUN(self.matrix,SIZE,np.argmax(out))
        contd = True
        contd = getState(self.matrix,SIZE)

        if contd == False:
            showinfo(message=f"GAME OVER !!! \n SCORE: {np.max(self.matrix)}")
            self.destroy()
        else:
            self.update()
            self.matrix = add2(self.matrix,SIZE)
            self.after(100,self.move)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('2048')
        self.geometry('{}x{}'.format(WIN_SIZE,WIN_SIZE))
        self.resizable(0, 0)
        self.configure(bg=BACKGROUND_COLOR_GAME)

        self.attributes('-toolwindow', True)
        self.__create_widgets()

    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()
