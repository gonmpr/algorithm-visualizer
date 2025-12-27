import tkinter as tk
from constants import WIDTH, HEIGHT 
def main():
    #ventana principal
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    root.config(bg="skyblue")
    root.geometry(f"{WIDTH}x{HEIGHT}")

    x1, y1 = 50, 50
    x2, y2 = 250, 150

    #contenedor de botones
    frame = tk.Frame(root, width=WIDTH//1, height=HEIGHT//12)
    frame.pack(padx=20,pady=5,side=tk.TOP)

    # visualizador
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(padx=20,pady=20,side=tk.BOTTOM)

    canvas.create_rectangle(200, 5, 10, 30, fill="blue", outline="black", width=1)


    root.mainloop()
    


if __name__ == '__main__':
    main()
