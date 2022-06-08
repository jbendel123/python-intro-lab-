from tkinter import *
window = Tk()
window.title("Stick Figure Drawing")
canvas = Canvas(window, width=300, height=300)
canvas.pack()
window.mainloop(30)
canvas.create_line(150,80,150,200)#body
canvas.create_line(150,200,120,250)#left leg
canvas.create_line(150,200,180,250)#right leg
canvas.create_line(150,140,120,150)#left arm 
canvas.create_line(150,140,180,150)#right arm 
canvas.create_oval(130,40,170,80)#head 
canvas.create_arc(135, 30, 165, 125, start=160, extent=220, width=1, outline="red", style="chord")#smile
