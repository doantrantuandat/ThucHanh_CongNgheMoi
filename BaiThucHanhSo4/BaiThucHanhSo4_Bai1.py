from drawingpanel import *
def doc():
    print("Doan Tran Tuan Dat - 16035741 - DHKHMT12A")
def main():
    print("\n")
    doc()
    panel = DrawingPanel(400, 300)
    panel.set_background("yellow")
    panel.canvas.create_rectangle(100, 50, 200, 300)
    panel.mainloop
if __name__ == '__main__':
    main()
    
