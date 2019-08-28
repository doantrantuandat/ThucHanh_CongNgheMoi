from drawingpanel import *
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def draw_1():
    showName()
    panel = DrawingPanel(400, 300)
    panel.set_background("yellow")
    panel.canvas.create_rectangle(100, 50, 200, 300)
if __name__ == '__main__':
	draw_1()
    
