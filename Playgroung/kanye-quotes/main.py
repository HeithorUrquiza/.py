from tkinter import *
import requests

def get_quote():
    global kanye_quote
    resp = requests.get("https://api.kanye.rest")
    resp.raise_for_status()
    kanye_quote = resp.json()["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

kanye_quote = ""
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Playgroung/kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Arial", 25, "bold"), fill="white")
get_quote()
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Playgroung/kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()