from drawingpanel import *
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def draw_2():
	showName()
	panel = DrawingPanel(200, 200)
	panel.canvas.create_polygon(100, 50, 150,0,150, 100, fill="green")
	panel.canvas.create_line(10, 120, 20, 160,30, 120, 40, 175)
if __name__ == '__main__':
	draw_2()