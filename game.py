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

player_turn = 1;
player1_points = 0
player2_points = 0
marked_lines = []

    # The following will help track which lines belong to a box and determining if a box has been completed.
box0 = [[1,0],[2,1],[1,2],[0,1]]
box1 = [[3,0],[4,1],[3,2],[2,1]]
box2 = [[5,0],[6,1],[5,2],[4,1]]
box3 = [[7,0],[8,1],[7,2],[6,1]]
box4 = [[9,0],[10,1],[9,2],[8,1]]
box5 = [[1,2],[2,3],[1,4],[0,3]]
box6 = [[3,2],[4,3],[3,4],[2,3]]
box7 = [[5,2],[6,3],[5,4],[4,3]]
box8 = [[7,2],[8,3],[7,4],[6,3]]
box9 = [[9,2],[10,3],[9,4],[8,3]]
box10 = [[1,4],[2,5],[1,6],[0,5]]
box11 = [[3,4],[4,5],[3,6],[2,5]]
box12 = [[5,4],[6,5],[5,6],[4,5]]
box13 = [[7,4],[8,5],[7,6],[6,5]]
box14 = [[9,4],[10,5],[9,6],[8,5]]
box15 = [[1,6],[2,7],[1,8],[0,7]]
box16 = [[3,6],[4,7],[3,8],[2,7]]
box17 = [[5,6],[6,7],[5,8],[4,7]]
box18 = [[7,6],[8,7],[7,8],[6,7]]
box19 = [[9,6],[10,7],[9,8],[8,7]]
box20 = [[1,8],[2,9],[1,10],[0,9]]
box21 = [[3,8],[4,9],[3,10],[2,9]]
box22 = [[5,8],[6,9],[5,10],[4,9]]
box23 = [[7,8],[8,9],[7,10],[6,9]]
box24 = [[9,8],[10,9],[9,10],[8,9]]
boxes = [box0, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15, box16, box17, box18, box19, box20, box21, box22, box23, box24]

distance_between_dots = size_of_board/number_of_dots
dot_width = distance_between_dots*.25
edge_width = distance_between_dots*.10




#for i in range(50,650, 100):
  #canvas.create_line(50, i, 550, i, fill="gray", dash = (2,2))
  #canvas.create_line(i, 50, i, 550, fill="gray", dash = (2,2))

  #Functions

def isEven(n): 
    return n % 2 == 0


def get_logical_position(x, y):
  
  xlog = (x - 25) // 50
  ylog = (y - 25) // 50
  pos = []
  direction = ""
  if(isEven(xlog) == False and isEven(ylog) == True):
    direction = "row"
    pos[xlog, ylog]
    #(even, odd)
  elif(isEven(xlog) == True and isEven(ylog) == 
False):
    direction= "col"
    pos = [xlog, ylog]
    
  return pos, direction


# def mark_line (pos, direction:# problem 1 
#   global player_turn 
#   x= 50 + pos[0] + 25
#   y= 50 + pos[1] + 25
#   if player turn == 1 :
#     canvas.create_line(x, y, fill = player1_color)
# elif player_turn == 2:
#     canvas.create_line(x, y, fill = player2_color)

def handle_click(e):
  pos, direction = get_logical_position(e.x, e.y)
  print("someone clicked", e.x, e.y)
  mark_line(pos, direction)
    
def mark_line(pos, direction):
  print(pos, direction)
  return
  if direction == "row":
  #50,50,150,5 0
    r = int((pos[0] -1) //2)
    c = int(pos[1]//2) 
    start_x = 50 + r * 100
    end_x = start_x + 100 
    start_y = 50 + c * 100
    end_y = start_y
  elif direction == "col":  
    c = int((pos[1] -1 // 2))
    r = int(pos[0] // 2)
    start_y = 50 + c * 100
    end_y = start_y + 100
    start_x = 50 + r * 100
    end_x = start_x 
    
    
  if player_turn == 1:
    color = player1_color
  else: 
    color = player2_color

  canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=edge_width)
 
def draw_board(canvas):
  for i in range(50,650,100):
      canvas.create_line(50, i, 550, i, fill="gray", dash = (2,2))
      canvas.create_line(i, 50, i, 550, fill="gray", dash = (2,2)) 

  for i in range(6):
    for j in range(6):
      start_x = i * 100 + 50
      end_x = j * 100 + 50
      canvas.create_oval(start_x - dot_width/2, end_x -     dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill=dot_color, outline=dot_color)



window = Tk()
window.title('Dots and Line Game')
canvas = Canvas(window, width=size_of_board, height=size_of_board)
height=size_of_board
canvas.pack()
window.mainloop(30)
draw_board(canvas)
#Listener
window.bind('<Button-1>', handle_click)