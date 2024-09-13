import tkinter as tk
from tkinter import filedialog
from PIL import Image  # type: ignore

def getPNG():
    global im1
    import_file_path = filedialog.askopenfile(filetypes=[("PNG files", "*.png")])
    if import_file_path:
        im1 = Image.open(import_file_path)

def convert():
    global im1
    if im1:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg',filetypes=[("JPG files", "*.jpg")])
        if export_file_path:
            im1.save(export_file_path)
        else:
            print("No image selected")

#creating main GUI window
root = tk.Tk()

#Creating canvas
canvas1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
canvas1.pack()

#Adding label to the canvas
label1 = tk.Label(root, text="Image Converter",bg="azure3")
label1.config(font=('helvicta', 20))
canvas1.create_window(150, 60, window=label1)

#Adding button to select PNF file
browse_png = tk.Button(text="Select PNG File", command=getPNG, bg="royalblue", fg='white', font=('helvicta',12,'bold'))
canvas1.create_window(150, 300, window=browse_png)

#Adding Button to Convert PNG to JPG
saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg='royalblue', fg='white', font=('helvicta', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)

root.mainloop()

