import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white")
canvas.place(x=0, y=0, width=398, height=300)

bar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)
bar.config(command=canvas.yview)
        
canvas.config(yscrollcommand=bar.set)
canvas.config(scrollregion=(0, 0, 300, 500))

canvas.create_oval(100, 200, 200, 300, fill="orange")

root.mainloop()