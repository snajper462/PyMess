import tkinter as tk


def retrieve_input(event):
    input_value = entry.get() + "\n"
    print(input_value)
    entry.delete(0,'end')
    text.insert(tk.END, input_value)

root = tk.Tk()
root.geometry("700x400")
root.title("Window")
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM, fill=tk.X)
entry.bind('<Return>', retrieve_input)
text = tk.Text(root)
text.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
root.mainloop()