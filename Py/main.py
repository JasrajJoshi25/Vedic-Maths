 from customtkinter import *
import voice
import time
from PIL import Image

num1 = None
num2 = None
label = None


def ved_calc(): 
    global num1, num2, label

    try:
        a = int(num1.get())
        b = int(num2.get())
    except:
        label.configure(text="Please enter valid numbers")
        return

    steps = []

    # detect base automatically
    max_num = max(a, b)
    base = 10 ** len(str(max_num))

    steps.append(f"Base = {base}")

    diff_a = a - base
    diff_b = b - base

    steps.append(f"{a} - {base} = {diff_a}")
    steps.append(f"{b} - {base} = {diff_b}")

    # cross subtraction
    left = a + diff_b
    steps.append(f"{a} + ({diff_b}) = {left}")

    # multiply differences
    right = diff_a * diff_b
    steps.append(f"{diff_a} × {diff_b} = {right}")

    digits = len(str(base)) - 1
    right_str = str(abs(right)).zfill(digits)

    steps.append(f"Right side formatted = {right_str}")

    answer = int(str(left) + right_str)

    steps.append(f"Final Answer = {answer}")

    # display steps with delay
    text = ""
    for step in steps:
        text += step + "\n"
        label.configure(text=text)
        app.update()
        time.sleep(1)


def vedicMaths():
    global num1, num2, label

    for widget in app.winfo_children():
        widget.destroy()

    inputFrame = CTkFrame(app, width=950)
    inputFrame.pack(pady=10)

    answerFrame = CTkFrame(app, width=950)
    answerFrame.pack(pady=10)

    CTkLabel(inputFrame, text="Enter Number :", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=10)

    num1 = CTkEntry(inputFrame, font=("Arial", 20, "bold"), width=120)
    num1.grid(row=0, column=1, padx=10)

    CTkLabel(inputFrame, text="Enter Number :", font=("Arial", 20, "bold")).grid(row=1, column=0, padx=10)

    num2 = CTkEntry(inputFrame, font=("Arial", 20, "bold"), width=120)
    num2.grid(row=1, column=1, padx=10)

    CTkButton(
        inputFrame,
        text="Calculate",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65,
        command=ved_calc
    ).grid(row=2, column=0, columnspan=2, pady=10)

    label = CTkLabel(
        answerFrame,
        text="",
        font=("Arial", 20, "bold"),
        justify="left",
        wraplength=850,
        width=950
    )

    label.pack(pady=20)

    CTkButton(
        inputFrame,
        text="Back",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        command=menu,
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65
    ).grid(row=3, column=0, columnspan=2, pady=10)


def about():
    for widget in app.winfo_children():
        widget.destroy()

    mainFrame = CTkFrame(app)
    mainFrame.pack(pady=20)

    imgFrame = CTkFrame(mainFrame)
    imgFrame.grid(row=0, column=0, padx=20)

    textFrame = CTkFrame(mainFrame)
    textFrame.grid(row=0, column=1, padx=20)

    # load image
    img = CTkImage(
        light_image=Image.open(r"C:\Users\joshi\OneDrive\Desktop\JJ_CODE\Vedic Maths\SRC\tirthaji_photo.jpg"),
        size=(250, 250)
    )

    CTkLabel(imgFrame, image=img, text="").pack()

    about_text = """
Jagadguru Swami Bharati Krishna Tirtha (1884–1960) was a rare phenomenon in modern
history—a man who seamlessly united the rigorous logic of a world-class
mathematician with the profound mystical insights of a Vedic seer. Born Venkataraman
Shastri in Tamil Nadu, he displayed a staggering intellectual capacity from childhood,
eventually setting an academic record by earning Master of Arts degrees in seven
different subjects simultaneously by the age of twenty. His mastery spanned
Mathematics, Science, Philosophy, English, History, Sanskrit, and Economics, yet he
chose to dedicate his life to the pursuit of spiritual truth.

His most enduring legacy is the reconstruction of "Vedic Mathematics," a system he
rediscovered during eight years of deep meditation and scriptural study in the forests of
Sringeri. By decoding hidden meanings within the Atharva Veda, he reconstructed
sixteen sutras (word-formulas) that transform complex calculations into simple,
intuitive mental processes.

These formulas, such as Ekadhikena Purvena ("By one more
than the previous one") and Urdhva-Tiryagbhyam ("Vertically and crosswise"),
provide a unified approach to all branches of mathematics, from basic arithmetic
to advanced calculus. And Many More things...
"""

    # SCROLLABLE TEXT AREA
    scrollFrame = CTkScrollableFrame(textFrame, width=550, height=300)
    scrollFrame.pack()

    CTkLabel(
        scrollFrame,
        text=about_text,
        font=("Arial", 18),
        justify="left",
        wraplength=520
    ).pack()

    CTkButton(
        app,
        text="Narrate",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65,
        command=lambda: voice.speak(about_text)
    ).pack(pady=30)

    CTkButton(
        app,
        text="Back",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        command=menu,
        width=600,
        height=60
    ).pack(pady=10)


def menu():
    for widget in app.winfo_children():
        widget.destroy()

    time.sleep(1)

    voice.speak(
        "Welcome to Vedic Maths Poster, we are Group 5, We are here to present our project on Vedic Mathematics. Let's dive in and explore the fascinating work of Bhaarti Krishna together!"
    )

    btnFrame = CTkFrame(app)
    btnFrame.pack(pady=10)

    CTkLabel(btnFrame, text="Menu:", font=("Arial", 40, "bold"),width=950).grid(row=0, column=0, pady=100)

    CTkButton(
        btnFrame,
        text="Numericals",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        command=vedicMaths,
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65
    ).grid(row=1, column=0, pady=10)

    CTkButton(
        btnFrame,
        text="About Tirthji",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        command=about,
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65
    ).grid(row=2, column=0, pady=10)

    CTkButton(
        btnFrame,
        text="Exit",
        font=("Arial", 20, "bold"),
        fg_color="red",
        command=app.destroy,
        corner_radius=15,
        width=600,
        height=65
    ).grid(row=3, column=0, pady=10)


def intro():
    for widget in app.winfo_children():
        widget.destroy()

    teamInfo = """
Group 4:
1. Sonam Dubey          2. Faizan Shaikh
3. Khushali Hirapara    4. Jasraj Joshi
5. Kiran Rani Padhy     6. Raj Pandey
7. Krish Patel          8. Mann Patel
            9. Vasu Patel
"""

    headingFrame = CTkFrame(app)
    headingFrame.pack(pady=10)

    infoFrame = CTkFrame(app)
    infoFrame.pack(pady=10)

    CTkLabel(
        headingFrame,
        text="Bhartiya Krishna Tirthji",
        font=("Arial", 40, "bold"),
        width=960
    ).pack(pady=90)

    CTkLabel(
        infoFrame,
        text=teamInfo,
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    CTkButton(
        infoFrame,
        text="Next =>",
        font=("Arial", 20, "bold"),
        fg_color="#E67300",
        command=menu,
        corner_radius=15,
        hover_color="green",
        width=600,
        height=65
    ).pack(pady=10)


app = CTk()
app.title("Vedic Maths")
app.maxsize(950, 600)
app.minsize(950, 600)
app.configure(bg="#1e1e1e")

headFrame = CTkFrame(app)
headFrame.pack(pady=10)

btnFrame = CTkFrame(app)
btnFrame.pack(pady=10)

CTkLabel(
    headFrame,
    text="Welcome To Vedic Maths Poster",
    font=("Arial", 40, "bold"),
    width=960
).pack(pady=100)

CTkLabel(
    headFrame,
    text="Something Great Inside",
    font=("Arial", 30, "bold")
).pack(pady=10)

CTkButton(
    btnFrame,
    text="Dive In !!",
    font=("Arial", 20, "bold"),
    fg_color="#E67300",
    command=intro,
    corner_radius=15,
    hover_color="green",
    width=600,
    height=65
).pack(pady=10)

app.mainloop()