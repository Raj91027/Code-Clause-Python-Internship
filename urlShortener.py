import tkinter as tk
import pyshorteners
from PIL import Image, ImageTk
import tkinter.messagebox

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")

        # Load the background image
        self.bg_image = Image.open("bg.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)

        self.bg_label.place(relwidth=1, relheight=1)

        self.label_font = ("Helvetica", 14)
        self.button_font = ("Helvetica", 10)
        self.result_font = ("Helvetica", 12)

        self.label = tk.Label(root, text="Enter URL:", font=self.label_font)
        self.label.place(relx=0.2, rely=0.15)

        self.url_entry = tk.Entry(root, font=self.label_font)
        self.url_entry.place(relx=0.4, rely=0.15)

        self.shorten_button = tk.Button(root, text="Shorten", command=self.shorten_url, font=self.button_font)
        self.shorten_button.place(relx=0.45, rely=0.25)

        self.copy_button = tk.Button(root, text="Copy Shortened URL", command=self.copy_shortened_url, font=self.button_font)
        self.copy_button.place(relx=0.35, rely=0.35)

        self.shortened_label = tk.Label(root, text="", font=self.result_font)
        self.shortened_label.place(relx=0.2, rely=0.45)

        # Adjust window size
        self.root.geometry("500x300")

    def shorten_url(self):
        original_url = self.url_entry.get()
        shortened_url = self.shortenurl(original_url)
        self.shortened_label.config(text=f"Shortened URL: {shortened_url}")
        self.copied_url = shortened_url  # Store the shortened URL

    def copy_shortened_url(self):
        try:
            self.root.clipboard_clear()  # Clear the clipboard
            self.root.clipboard_append(self.copied_url)  # Append the URL to clipboard
            self.root.update()  # Force update the clipboard
            tk.messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")
        except:
            tk.messagebox.showerror("Error", "Unable to copy URL to clipboard.")

    def shortenurl(self, url):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
# main
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = URLShortenerApp(root)
    root.mainloop()