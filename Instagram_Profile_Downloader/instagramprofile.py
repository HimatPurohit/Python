import instaloader
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Instagram Profile Downloader")
root.geometry("300x100")

user_var = tk.StringVar()


def profileDownload():
    mod = instaloader.Instaloader()
    # mod.interactive_login(input("Username:"))
    # mod.download_profile(user_entry.get(), profile_pic=False, profile_pic_only=False, fast_update=False, download_stories=False,
    #                 download_stories_only=False, download_tagged=True, download_tagged_only=False, post_filter=None,
    #                 storyitem_filter=None)
    mod.download_profile(user_entry.get(), profile_pic_only=True)
    messagebox.showinfo("Status", "Image Downloaded successfully")


user_label = tk.Label(root, text='Enter Insta Id: ', font=('calibre', 10, 'bold'))
user_entry = tk.Entry(root, textvariable=user_var, font=('calibre', 10, 'normal'))

download_button = tk.Button(root, text='Download', command=profileDownload)

user_label.grid(row=0, column=0)
user_entry.grid(row=0, column=1)
download_button.grid(row=1, column=1)

root.mainloop()
