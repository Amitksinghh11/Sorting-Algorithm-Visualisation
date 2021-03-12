import tkinter as tk
from tkinter import ttk
from algorithms import bubble_sort, create_list, insertion_sort, selection_sort, heap_sort, quick_sort, merge, merge_sort

root = tk.Tk()
root.title("Sorting Algorithm Visualisation")
root.maxsize(900,800)
root.config(bg = "black")
data = []
select_alg = tk.StringVar()
def generate():
    global data
    print("Selected Algo" + select_alg.get())
    try:
        size = int(sizeEntry.get())
    except Exception:
        size = 100
    try:    
        maxi = int(max_valueEntry.get())
    except Exception:
        maxi = 100
    data = create_list(size=size,max=maxi)
    print(data)
    draw_data(data, ["white" for x in range(len(data))])
    tk.Button(ui_frame, text = "Start", command = startAlgorithm, bg = "red").grid(row = 1, column = 4, padx = 5, pady = 5)

def draw_data(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width  = 800
    x_width = c_width / (len(data) + 1)
    spacing = 5
    normalize_data = [i / max(data) for i in data]
    for i, height in enumerate(normalize_data):
        x0= i * x_width + spacing
        y0= c_height - height * 340
        x1= (i+1) * x_width 
        y1= c_height
        canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
    root.update_idletasks()

def startAlgorithm():
    global data
    tick = speedScale.get()
    if select_alg.get() == "Bubble sort":
        sorted_data = bubble_sort(data, draw_data, tick)
        print(sorted_data)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])

    elif select_alg.get() == "Insertion Sort":
        sorted_data = insertion_sort(data, draw_data, tick)
        print(sorted_data)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])

    elif select_alg.get() == "Selection Sort":
        sorted_data = selection_sort(data, draw_data, tick)
        print(sorted_data,)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])

    elif select_alg.get() == "Heap Sort":
        sorted_data = heap_sort(data, draw_data, tick)
        print(sorted_data,)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])

    elif select_alg.get() == "Quick Sort":
        sorted_data = quick_sort(data, draw_data, tick)
        print(sorted_data,)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])

    elif select_alg.get() == "Merge Sort":
        sorted_data = merge_sort(data, draw_data, tick)
        print(sorted_data,)
        canvas.delete("all")
        draw_data(sorted_data,["white" for x in range(len(data))])
    

ui_frame = tk.Frame(root, width = 800, height = 200, bg = "grey")
ui_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

canvas = tk.Canvas(root, width = 800, height = 380, bg = "black")
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

# Row[0]
tk.Label(ui_frame, text = "Algorithm", bg = "grey").grid(row = 0, column = 0, padx = 10,pady = 10, sticky = "w")
alog_menu = ttk.Combobox(ui_frame,textvariable = select_alg, values = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort","Quick Sort","Merge Sort"])
alog_menu.grid(row = 0, column = 1, padx = 5, pady = 5)



speedScale = tk.Scale(ui_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = "horizontal", label = "Speed")
speedScale.grid(row = 0, column = 3, padx = 5, pady = 5)

# Row[1]
tk.Label(ui_frame, text = "Size", bg = "grey").grid(row = 1, column = 0, padx = 10,pady = 10, sticky = "w")
sizeEntry = tk.Entry(ui_frame)
sizeEntry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")

tk.Label(ui_frame, text = "Max Value", bg = "grey").grid(row = 1, column = 2, padx = 10,pady = 10, sticky = "w")
max_valueEntry = tk.Entry(ui_frame)
max_valueEntry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "w")

tk.Button(ui_frame, text = "Generate", command = generate, bg = "white").grid(row = 0, column = 2, padx = 5, pady = 5)

root.mainloop()