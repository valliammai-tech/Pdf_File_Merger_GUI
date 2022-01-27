import tkinter
from tkinter import messagebox
from tkinter import *
import logging
from pdfFiles import filter_word_file_in_dir
from pdf_file_merge import merge_pdfs

window=tkinter.Tk()
files=[]
listbox=Listbox(window)

def on_click():
    try:
        res=txt.get()
        files=filter_word_file_in_dir(res)
        for i in files:
            listbox.insert('end', i)
        output=merge_pdfs(filter_word_file_in_dir(res))
        if not output:
            messagebox.showerror ("Invalid directory!!", 'Please Enter Valid directory that has PDF files...')
        if output:
            messagebox.showinfo('PDF File Merge','New_Merged_File.pdf created on downloads directory.\n\t\t\t\t Please verify!!')
    except Exception as e:
        logging.error("Error occurred in button on_click function",e)
    else:
        logging.info("No Exception in button on_click function call")
    finally:
        logging.info("Job completed!!")
window.title('Merge PDF files GUI')
l1=Label(window, text="Enter directory path from which pdf files to be choosen and merged: ")
l1.pack()
window.geometry('300x300')
txt=Entry(window,width=100)
txt.pack()
bt=Button(window, text='Search', bg='orange', fg='red', command=on_click)
bt.pack()
listbox.pack(fill=X)
bt1=Button(window, text='Close', bg='blue', fg='yellow', command=window.destroy)
bt1.pack()

window.mainloop()
