import tkinter as tk

# --- functions ---

def change_frame(new_frame):
    global current

    # hide current tk.Frame
    current.pack_forget()

    # show new tk.Frame
    current = new_frame
    current.pack()

# ---

def show_main_frame():
    change_frame(main_frame)

def show_frame_1():
    change_frame(frame_1)

def show_frame_2():
    change_frame(frame_2)

# --- main ---

root = tk.Tk()

# --- main frame without .pack() ---

main_frame = tk.Frame(root)

button = tk.Button(main_frame, text="Frame #1", command=show_frame_1)
button.pack()

button = tk.Button(main_frame, text="Frame #2", command=show_frame_2)
button.pack()

# --- tk.Frame ---

frame_1 = tk.Frame(root)

l = tk.Label(frame_1, text="It is Frame #1", bg='red')
l.pack()

b = tk.Button(frame_1, text="BACK", command=show_main_frame)
b.pack()

# --- tk.Frame without .pack() ---

frame_2 = tk.Frame(root)

l = tk.Label(frame_2, text="It is Frame #2", bg='green')
l.pack()

b = tk.Button(frame_2, text="BACK", command=show_main_frame)
b.pack()

# ---

current = main_frame
current.pack()

root.mainloop()
