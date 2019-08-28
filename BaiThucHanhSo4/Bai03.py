from drawingpanel import *
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def draw_3():
	showName()
	panel = DrawingPanel(500, 400)
	panel.set_background("gray")
	panel.canvas.create_rectangle(200, 200, 450, 300,fill="black")
	panel.canvas.create_rectangle(350, 220, 440, 260,fill="green")
	x=250
	y=300
	r=20
	panel.canvas.create_oval(x-r, y-r, x+r, y+r,fill="red")
	x=400
	panel.canvas.create_oval(x-r, y-r, x+r, y+r,fill="red")
if __name__ == '__main__':
	draw_3()