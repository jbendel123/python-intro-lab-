from tkinter import * 

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#1F2232' 
player1_color = '#A27E6F'
player1_color_light = '#E7EBC5'
player2_color = '#3E505B'
player2_color_light = '#9B9987'
Green_color = '#1F2232'

distance_between_dots = size_of_board/number_of_dots
dot_width = distance_between_dots*.25
edge_width = distance_between_dots*.10

window = Tk()
window.title('Dots and Line Game')
canvas = Canvas(window, width=size_of_board, height=size_of_board)
height=size_of_board
canvas.pack()
window.mainloop(30)
#1st row 
canvas.create_line(50, 50, 550, 50, fill="gray", dash = (2,2))
#2nd row 
canvas.create_line(50, 150, 550, 150, fill="gray", dash = (2,2))
#3rd row  
canvas.create_line(50,250,550,250, fill="gray", dash = (2,2))
#4th row 
canvas.create_line(50,350,550,350, fill="gray", dash = (2,2))
#5th row
canvas.create_line(50,450,550,450, fill="gray", dash = (2,2))
#6th row 
canvas.create_line(50,550,550,550, fill="gray", dash = (2,2))

#1st collum 
canvas.create_line(50, 50, 50, 550, fill="gray", dash = (2,2))
#2nd collum 
canvas.create_line(150,50,150,550, fill="gray", dash = (2,2))
#3rd collum 
canvas.create_line(250,50,250,550, fill="gray", dash = (2,2))
#4th collum 
canvas.create_line(350,50,350,550, fill="gray", dash = (2,2))
#5th collum 
canvas.create_line(450,50,450,550, fill="gray", dash = (2,2))
#6th collum 
canvas.create_line(550,50,550,550, fill="gray", dash = (2,2))
