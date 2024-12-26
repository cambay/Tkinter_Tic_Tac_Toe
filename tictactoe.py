import tkinter as tk 
from tkinter import * 

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")


canvas_height = 400
canvas_width = 400

gamecanvas = tk.Canvas(window, height= canvas_height, width= canvas_width, background='white')
gamecanvas.grid()


gameborder = gamecanvas.create_line(125,10,125, 390, fill='black', width=6), gamecanvas.create_line(275,10,275,390, fill='black', width=6), 
gamecanvas.create_line(10,125,390,125, fill='black', width=6), gamecanvas.create_line(10,275,390,275, fill='black', width=6)
gamecanvas.grid()



turns = 0 
is_there_a_shape = [ [0,0,0],[0,0,0],[0,0,0]]


def check_Winner():
    for i in range(3):
        if is_there_a_shape[i][0] == is_there_a_shape[i][1] == is_there_a_shape[i][2] != 0:
            return is_there_a_shape[i][0]
        if is_there_a_shape[0][i] == is_there_a_shape[1][i] == is_there_a_shape[2][i] != 0:
            return is_there_a_shape[0][i]
    if is_there_a_shape[0][0] == is_there_a_shape[1][1] == is_there_a_shape[2][2] != 0:
        return is_there_a_shape[0][0]
    if is_there_a_shape[0][2] == is_there_a_shape[1][1] == is_there_a_shape[2][0] != 0:
        return is_there_a_shape[0][2]
    return 0

reset_button = None 

def reset_game():
    global turns, is_there_a_shape, reset_button

    if reset_button:
         reset_button.destroy()
         reset_button = None

    gamecanvas.delete("all")
    
    gamecanvas.create_line(125, 10, 125, 390, fill='black', width=6)
    gamecanvas.create_line(275, 10, 275, 390, fill='black', width=6)
    gamecanvas.create_line(10, 125, 390, 125, fill='black', width=6)
    gamecanvas.create_line(10, 275, 390, 275, fill='black', width=6)
    
    turns = 0
    is_there_a_shape = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    gamecanvas.bind("<Button-1>", on_canvas_click)

def on_canvas_click(event):
    global turns, is_there_a_shape, reset_button
    x, y =event.x, event.y


    #Row 1
    if 0 <= x <= 125 and 10 <= y <= 119:
            print("Top left quadrant")
            if is_there_a_shape[0][0] > 0:
                print("Cell occupied already!")
            else: 
                if turns % 2 == 0: 
                    gamecanvas.create_oval(20, 15, 110, 100, outline='black', width= 5)
                    is_there_a_shape[0][0] = 1 #O
                    turns += 1
                else:
                    gamecanvas.create_line(20, 20, 110, 115, fill='black', width= 5)
                    gamecanvas.create_line(20, 115, 115, 20, fill='black', width= 5)
                    is_there_a_shape[0][0] = 2 #X
                    turns += 1

    elif 126 <= x <= 269 and 10 <= y <= 119:
            print("Top middle quadrant")
            if is_there_a_shape[0][1] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(145, 15, 255, 110, outline='black', width= 5)
                    is_there_a_shape[0][1] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(150, 20, 260, 115, fill='black', width= 5)
                    gamecanvas.create_line(150, 115, 260, 20, fill='black', width= 5)
                    is_there_a_shape[0][1] = 2
                    turns += 1

  
    elif 270 <= x <= 390 and 10 <= y <= 119:
            print("Top Right quadrant")
            if is_there_a_shape[0][2] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(290, 15, 380, 105, outline='black', width= 5)
                    is_there_a_shape[0][2] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(290, 20, 380, 115, fill='black', width= 5)
                    gamecanvas.create_line(290, 115, 380, 20, fill='black', width= 5)
                    is_there_a_shape[0][2] = 2
                    turns += 1

    #Row 2
    elif 0 <= x <= 125 and 120 <= y <= 269:
            print("Middle left quadrant")
            if is_there_a_shape[1][0] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(10, 145, 115, 255, outline='black', width= 5)
                    is_there_a_shape[1][0] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(20, 150, 110, 245, fill='black', width= 5)
                    gamecanvas.create_line(20, 245, 110, 150, fill='black', width= 5)
                    is_there_a_shape[1][0] = 2
                    turns += 1

    elif 126 <= x <= 269 and 120 <= y <= 269:
            print("Middle middle quadrant")
            if is_there_a_shape[1][1] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(145, 145, 255, 255, outline='black', width= 5)
                    is_there_a_shape[1][1] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(150, 150, 260, 245, fill='black', width= 5)
                    gamecanvas.create_line(150, 245, 260, 150, fill='black', width= 5)
                    is_there_a_shape[1][1] = 2
                    turns += 1

    elif 270 <= x <= 390 and 120 <= y <= 269:
            print("Middle right quadrant")
            if is_there_a_shape[1][2] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(285, 145, 390, 255, outline='black', width= 5)
                    is_there_a_shape[1][2] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(290, 150, 380, 245, fill='black', width= 5)
                    gamecanvas.create_line(290, 245, 380, 150, fill='black', width= 5)
                    is_there_a_shape[1][2] = 2
                    turns += 1

    #Row 3
    elif 0 <= x <= 125 and 271 <= y <= 390:
            print("Botttom left quadrant")
            if is_there_a_shape[2][0] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(10, 285, 115, 385, outline='black', width= 5)
                    is_there_a_shape[2][0] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(20, 285, 110, 385, fill='black', width= 5)
                    gamecanvas.create_line(20, 385, 110, 285, fill='black', width= 5)
                    is_there_a_shape[2][0] = 2
                    turns += 1

    elif 126 <= x <= 269 and 271 <= y <= 390:
            print("Bottom middle quadrant")
            if is_there_a_shape[2][1] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(145, 285, 255, 385, outline='black', width= 5)
                    is_there_a_shape[2][1] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(150, 285, 260, 385, fill='black', width= 5)
                    gamecanvas.create_line(150, 385, 260, 285, fill='black', width= 5)
                    is_there_a_shape[2][1] = 2
                    turns += 1

    elif 270 <= x <= 390 and 271 <= y <= 390:
            print("Bottom right quadrant")
            if is_there_a_shape[2][2] > 0:
                print("Cell occupied already!")
            else:
                if turns % 2 == 0: 
                    gamecanvas.create_oval(285, 285, 390, 385, outline='black', width= 5)
                    is_there_a_shape[2][2] = 1
                    turns += 1
                else:
                    gamecanvas.create_line(285, 285, 390, 385, fill='black', width= 5)
                    gamecanvas.create_line(285, 385, 390, 285, fill='black', width= 5)
                    is_there_a_shape[2][2] = 2
                    turns += 1

    winner = check_Winner()
    if winner == 1:
        print("O wins!")
        gamecanvas.unbind("<Button-1>")
        reset_button = tk.Button(text="Reset Game", font=("hevetica",50), fg='black', bg='brown', command= reset_game)
        reset_button.grid(row= 0, column=0)
    elif winner == 2:
        print("X wins!")
        gamecanvas.unbind("<Button-1>")
        reset_button = tk.Button(text="Reset Game", font=("hevetica",50), fg='black', bg='brown', command= reset_game)
        reset_button.grid(row= 0, column=0)
    elif turns == 9:
        print("Cat")
        gamecanvas.unbind("<Button-1>")
        reset_button = tk.Button(text="Reset Game", font=("hevetica",50), fg='black', bg='brown', command= reset_game)
        reset_button.grid(row= 0, column=0)


gamecanvas.bind("<Button-1>", on_canvas_click)


window.mainloop()