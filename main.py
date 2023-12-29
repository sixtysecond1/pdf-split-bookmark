from tkinter import filedialog
import tkinter as tk
from tkinter.constants import CENTER  # 加到第一行
from bookmarks import run


def loadFile():
    if loadFile_en.get() is None:
        file_path = filedialog.askopenfilename(filetypes=(
            ("pdf files", "*.pdf"), ("all files", "*.*")))
        loadFile_en.insert(0, file_path)
    else:
        file_path = filedialog.askopenfilename(filetypes=(
            ("pdf files", "*.pdf"), ("all files", "*.*")))
        loadFile_en.delete(0, 'end')
        loadFile_en.insert(0, file_path)


def output():
    fileRoute = loadFile_en.get()
    run(fileRoute)


win = tk.Tk()
win.title('pdf依書籤分檔.exe')
win.geometry('380x400')
win.resizable(False, False)
win.iconbitmap('icon.ico')
'''Label區域'''
lb = tk.Label(text="請選取檔案", bg="grey", fg="white", height=1)
lb.place(x=0, y=0)

'''Label區域'''
'''Entry區域'''
loadFile_en = tk.Entry(width=40)
loadFile_en.place(x=70, y=0)


loadFile_btn = tk.Button(text="...", height=1,
                         command=loadFile)  # 這行多加command=loadFile
loadFile_btn.place(x=355, y=0)
output_btn = tk.Button(text="輸出", height=1, command=output)
output_btn.place(anchor=CENTER, x=180, y=200)
'''Button區域'''


win.mainloop()
