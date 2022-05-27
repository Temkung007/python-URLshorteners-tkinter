import pyshorteners
import tkinter as tk


app = tk.Tk()
app.title('URL Shortener with TINYURL')
app.geometry("600x400")
app.config(bg="#A2E4FF")

Font_tuple = ("Comic Sans MS", 20, "bold")
Font_tuple_btn = ("Comic Sans MS", 15, "bold")


def url_tp_short():
    if(len(url.get())):
        tinyurl = pyshorteners.Shortener()
        url_Shortened.set(tinyurl.tinyurl.short(url.get()))


def clear():
    url.delete(0, 'end')
    url_Shortened.set("")


url_Shortened = tk.StringVar()

tk.Label(app, text="Enter URL to Short", bg="#A2E4FF", font=Font_tuple).pack()

url = tk.Entry(app, width=45, bg="#D4EFFA", font=('Arial 16'))
url.pack(pady=10)


tk.Button(app, width=10, command=url_tp_short, text="Short url", font=Font_tuple_btn).pack()

tk.Label(app, text="The Shortened URL is", bg="#A2E4FF", font=Font_tuple).pack(pady=(10, 0))
tk.Entry(app, width=45, textvariable=url_Shortened, bg="#D4EFFA", font=('Arial 16')).pack()

tk.Button(app, width=10, command=clear, text="Clear", font=Font_tuple_btn).pack(pady=10)


app.mainloop()