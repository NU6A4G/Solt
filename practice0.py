import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
from tkinter import simpledialog
import os


def draw_shape(shape, turtle):
    if shape == "Négyzet":
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)
    elif shape == "Kör":
        turtle.circle(50)
    elif shape == "Háromszög":
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)
    elif shape == "Csillag":
        for _ in range(5):
            turtle.forward(100)
            turtle.right(144)
    elif shape == "Ötszög":
        for _ in range(5):
            turtle.forward(100)
            turtle.left(72)


def save_drawing(canvas, user_name, shape):
    file_path = f"{user_name}_{shape}.eps"
    canvas.postscript(file=file_path, colormode='color')
    print(f"Rajz mentve: {file_path}")


def main():
    root = tk.Tk()
    root.title("Forma rajzoló")

    user_name = simpledialog.askstring("Input", "Mi a neve?")

    canvas = ScrolledCanvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)

    turtle = RawTurtle(canvas)
    turtle.speed(2)

    shapes = ["Négyzet", "Kör", "Háromszög", "Csillag", "Ötszög"]

    shape_var = tk.StringVar(root)
    shape_var.set(shapes[0])

    shape_label = tk.Label(root, text="Válassz formát:")
    shape_label.pack(pady=10)

    shape_menu = tk.OptionMenu(root, shape_var, *shapes)
    shape_menu.pack(pady=10)

    draw_button = tk.Button(root, text="Rajzolás", command=lambda: draw_shape(shape_var.get(), turtle))
    draw_button.pack(pady=10)

    save_button = tk.Button(root, text="Kép kódjának mentése", command=lambda: save_drawing(canvas, user_name, shape_var.get()))
    save_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
