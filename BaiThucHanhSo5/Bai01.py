from drawingpanel import *
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def draw_1():
	showName()
	panel = DrawingPanel(400, 400)
	panel.set_background("yellow")
	panel.canvas.create_rectangle(100, 100, 300, 300,fill="red")
	panel.canvas.create_rectangle(100, 200, 300, 203,fill="black")
	x=100
	y=100
	r=50
	panel.canvas.create_oval(x-r, y-r, x+r, y+r,fill="blue")
	x=300
	y=100
	r=50
	panel.canvas.create_oval(x-r, y-r, x+r, y+r,fill="blue")
if __name__ == '__main__':
	draw_1()