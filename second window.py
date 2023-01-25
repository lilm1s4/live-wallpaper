import ctypes
import tkinter as tk
from PIL import Image, ImageTk


def update_for_little_gif_1(ind):
    frame_little_gif_1 = frames_little_gif_1[ind]
    ind += 1
    if ind == frameCnt_little_gif_1:
        ind = 0
    label_for_little_gif_1.configure(image=frame_little_gif_1)
    window.after(50, update_for_little_gif_1, ind)


def update_for_little_gif_2(ind):
    frame_little_gif_2 = frames_little_gif_2[ind]
    ind += 1
    if ind == frameCnt_little_gif_2:
        ind = 0
    label_for_little_gif_2.configure(image=frame_little_gif_2)
    window.after(50, update_for_little_gif_2, ind)


def update_for_little_gif_3(ind):
    frame_little_gif_3 = frames_little_gif_3[ind]
    ind += 1
    if ind == frameCnt_little_gif_3:
        ind = 0
    label_for_little_gif_3.configure(image=frame_little_gif_3)
    window.after(50, update_for_little_gif_3, ind)


def gif_launch_1():
    window.destroy()

    root = tk.Tk()
    root.geometry("1280x984")
    root.title("gifka")
    root.overrideredirect(1)

    label = tk.Label(root)

    file = Image.open("C:\\1280x1024.gif")
    frameCnt = file.n_frames
    frames = [tk.PhotoImage(file="C:\\1280x1024.gif", format=f'gif -index {i}') for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1

        if ind == frameCnt:
            ind = 0

        label.configure(image=frame)
        root.after(50, update, ind)

    label.pack()

    root.after(0, update, 0)
    root.mainloop()


def gif_launch_2():
    window.destroy()

    root = tk.Tk()
    root.geometry("1280x984")
    root.title("gifka")
    root.overrideredirect(1)

    label = tk.Label(root)

    file = Image.open("C:\\1280x1024.gif")
    frameCnt = file.n_frames
    frames = [tk.PhotoImage(file="C:\\1280x1024.gif", format=f'gif -index {i}') for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1

        if ind == frameCnt:
            ind = 0

        label.configure(image=frame)
        root.after(50, update, ind)

    label.pack()

    root.after(0, update, 0)
    root.mainloop()


def gif_launch_3():
    window.destroy()

    root = tk.Tk()
    root.geometry("1280x984")
    root.title("gifka")
    root.overrideredirect(1)

    label = tk.Label(root)

    file = Image.open("C:\\1280x1024.gif")
    frameCnt = file.n_frames
    frames = [tk.PhotoImage(file="C:\\1280x1024.gif", format=f'gif -index {i}') for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1

        if ind == frameCnt:
            ind = 0

        label.configure(image=frame)
        root.after(50, update, ind)

    label.pack()

    root.after(0, update, 0)
    root.mainloop()


def place_1():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\oboi.jpg", 0)


def place_2():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\oboi2.jpg", 0)


def place_3():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\obo\\obob3.jpg", 0)


window = tk.Tk()
window.title("vashi oboi")
window.geometry("610x460")

file_little_gif_1 = Image.open("C:\\200x200.gif")
frameCnt_little_gif_1 = file_little_gif_1.n_frames
frames_little_gif_1 = [tk.PhotoImage(file='C:\\200x200.gif', format=f'gif -index {i}')
                       for i in range(frameCnt_little_gif_1)]

file_little_gif_2 = Image.open("C:\\200x200.gif")
frameCnt_little_gif_2 = file_little_gif_2.n_frames
frames_little_gif_2 = [tk.PhotoImage(file='C:\\200x200.gif', format=f'gif -index {i}')
                       for i in range(frameCnt_little_gif_2)]

file_little_gif_3 = Image.open("C:\\200x200.gif")
frameCnt_little_gif_3 = file_little_gif_3.n_frames
frames_little_gif_3 = [tk.PhotoImage(file='C:\\200x200.gif', format=f'gif -index {i}')
                       for i in range(frameCnt_little_gif_3)]

btn1 = tk.Button(window, text="OBOI1", command=place_1, width=27, height=1, bg="white")
btn1.grid(row=2, column=1)

btn2 = tk.Button(window, text="OBOI2", command=place_2, width=27, height=1, bg="white")
btn2.grid(row=2, column=2)

btn3 = tk.Button(window, text="OBOI3", command=place_3, width=27, height=1, bg="white")
btn3.grid(row=2, column=3)

btn4 = tk.Button(window, text="OBOI4", command=gif_launch_1, width=27, height=1, bg="white")
btn4.grid(row=4, column=1)

btn5 = tk.Button(window, text="OBOI5", command=gif_launch_2, width=27, height=1, bg="white")
btn5.grid(row=4, column=2)

btn6 = tk.Button(window, text="OBOI6", command=gif_launch_3, width=27, height=1, bg="white")
btn6.grid(row=4, column=3)

canvas = tk.Canvas(window, height=200, width=200)
image1 = Image.open("C:\\obo\\oboi.jpg")
photo1 = ImageTk.PhotoImage(image1)
image1 = canvas.create_image(0, 0, anchor='nw', image=photo1)
canvas.grid(row=1, column=1)

canvas = tk.Canvas(window, height=200, width=200)
image2 = Image.open("C:\\obo\\oboi2.jpg")
photo2 = ImageTk.PhotoImage(image2)
image2 = canvas.create_image(0, 0, anchor='nw', image=photo2)
canvas.grid(row=1, column=2)

canvas = tk.Canvas(window, height=200, width=200)
image3 = Image.open("C:\\obo\\obob3.jpg")
photo3 = ImageTk.PhotoImage(image3)
image3 = canvas.create_image(0, 0, anchor='nw', image=photo3)
canvas.grid(row=1, column=3)

label_for_little_gif_1 = tk.Label(window)
label_for_little_gif_1.grid(row=3, column=1)

label_for_little_gif_2 = tk.Label(window)
label_for_little_gif_2.grid(row=3, column=2)

label_for_little_gif_3 = tk.Label(window)
label_for_little_gif_3.grid(row=3, column=3)

window.after(0, update_for_little_gif_1, 0)
window.after(0, update_for_little_gif_2, 0)
window.after(0, update_for_little_gif_3, 0)

window.mainloop()