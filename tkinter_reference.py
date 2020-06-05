# for quick references for myself

import tkinter
import tkinter.filedialog
import tkinter.messagebox
import time  # for clock
from PIL import Image, ImageTk  # for loading image


def resize(image, factor):
    width, height = image.size
    new_width = round(width * factor)
    new_height = round(height * factor)
    image = image.resize((new_width, new_height))
    return image


def clock():
    current = time.strftime("%H:%M:%S")
    main_time.configure(text=current)
    main_time.after(1000, clock)


def main():
    # make window object
    root = tkinter.Tk()

    # set title of the window
    root.wm_title("Yay")
    # set the default window size
    root.geometry("1280x640")

    # make a button
    exitButton = tkinter.Button(text="Exit", command=exit)
    exitButton.grid(column=0)

    # make menu
    menu = tkinter.Menu()
    root.config(menu=menu)

    file_menu = tkinter.Menu()
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Item")
    file_menu.add_command(label="Exit", command=exit)

    edit_menu = tkinter.Menu()
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")

    # make clock with text label
    global main_time
    main_time = tkinter.Label(text="", fg="red", font=("Helvetica", 9))
    main_time.grid(column=4, row=0)
    main_time.after(0, clock)

    # load image onto GUI
    load = Image.open("images/hamedori.jpg")
    load = resize(load, 0.1)
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(image=render)
    img.grid(column=1, row=2)

    # canvas
    canvas = tkinter.Canvas(root, bg="white", height=300, width=300)
    coord = 100, 100, 300, 300
    canvas.create_arc(coord, start=0, extent=120, fill="red")
    canvas.create_arc(coord, start=150, extent=215, fill="green")
    canvas.grid(column=2, row=3)

    # checkbox
    var1 = tkinter.IntVar()
    var2 = tkinter.IntVar()
    c1 = tkinter.Checkbutton(text='Dreams', variable=var1, onvalue=1, offvalue=0)
    c1.grid(column=2, row=0)
    c2 = tkinter.Checkbutton(text='Come true', variable=var2, onvalue=1, offvalue=0)
    c2.grid(column=2, row=1)

    # entry for user input (just 1 line)
    text1 = tkinter.StringVar(value="default value")
    e1 = tkinter.Entry(textvariable=text1, font=('Arial', 14))
    e1.grid(column=3, row=1)
    e2 = tkinter.Entry(root, show='*', font=('Arial', 14))
    e2.grid(column=3, row=2)

    # text box for user input (can take more than 1 line)
    text2 = tkinter.StringVar(value="default text value")
    textbox1 = tkinter.Text(font=('Arial', 10))
    textbox1.grid(column=3, row=3)

    # list box
    str1 = tkinter.StringVar()
    str1.set((1, 2, 3, 4))
    lb = tkinter.Listbox(listvariable=str1)
    lb.grid(column=1, row=3)  # set position
    list_items = [11, 22, 33, 44]
    for item in list_items:
        lb.insert('end', item)  # append item to list box
    lb.insert(2, 'second')  # insert 'second' after 2
    lb.delete(3)  # delete object after 3

    # message box
    tkinter.messagebox.showinfo("title", "message")

    # radio button = like multiple choice
    r1 = tkinter.Radiobutton(text='Option A', value='A')
    r1.grid(column=3, row=4)
    r2 = tkinter.Radiobutton(text='Option B', value='B')
    r2.grid(column=3, row=5)
    r3 = tkinter.Radiobutton(text='Option C', value='C')
    r3.grid(column=3, row=6)

    # show the window
    root.mainloop()


main()
