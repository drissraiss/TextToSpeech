from tkinter import *
from messagebox import showinfo, showwarning, askretrycancel
from textblob import TextBlob
from tkinter import filedialog
from gtts import gTTS
from requests import get
from langdetect import detect


def convert():
    url = "http://www.kite.com"
    file = input1.get()
    folder = input2.get()
    if len(file) == 0 or len(folder) == 0:
        return showwarning('TeToSo', 'Please fill in the fields')
    while True:
        try:
            request = get(url, timeout=5)
            break
        except BaseException:
            tryAgain = askretrycancel(
                'TeToSo', 'Please check your internet connection and try again later')
            if not tryAgain:
                return
    try:

        with open(file, 'rt', encoding='utf-8') as f1:
            myText = f1.read()

        if autoDetect or len(input3.get()) == 0:
            lang = detect(myText)
        else:
            lang = input3.get()

        tts = gTTS(myText, lang=lang)
        tts.save(folder + '/soundText.mp3')
        showinfo('TeToSo', 'Converted successfully')
    except BaseException:
        showwarning('TeToSo', 'Please repeat later')


def selectfile():
    file = filedialog.askopenfilename()
    input1.set(file)


def selectfolder():
    folder = filedialog.askdirectory()
    input2.set(folder)


def isChecked():
    global autoDetect
    if check.get():
        input3.set('')
        entry3.config(state=DISABLED)
        autoDetect = True
    else:
        autoDetect = True
        entry3.config(state=NORMAL)


def notAuto():
    entry3.config(state=ACTIVE)


autoDetect = False

app = Tk()
app.title('TeToSo')
app.geometry('810x400+480+230')
Label(text='Text location : ', font=(
    'Courier', 20, 'bold')).grid(row=0, column=0)
Label(text='Save location : ', font=(
    'Courier', 20, 'bold')).grid(row=1, column=0)
Label(text='Language      : ', font=(
    'Courier', 20, 'bold')).grid(row=2, column=0)

input1 = StringVar()
input2 = StringVar()
input3 = StringVar()

Entry(textvariable=input1, font=('ariel', 18), state=DISABLED,
      width=30).grid(row=0, column=1, columnspan=2, pady=25)
Entry(textvariable=input2, font=('ariel', 18), state=DISABLED,
      width=30).grid(row=1, column=1, columnspan=2, pady=25)
entry3 = Entry(textvariable=input3, font=('ariel', 18),
               width=2)
entry3.grid(row=2, column=1, pady=25)

Button(text='Select file', width=10, font=(20),
       relief=GROOVE,
       cursor='hand2',
       command=selectfile).grid(row=0, column=3, padx=10, pady=10)
Button(text='Select folder', width=10, font=(30),
       relief=GROOVE,
       cursor='hand2',
       command=selectfolder).grid(row=1, column=3, padx=10, pady=10)
Button(text='Convert text to speech', font=('ariel', 20, 'bold'),
       relief=GROOVE,
       cursor='hand2',
       width=35,
       activebackground='#292b2c',
       bg='#fff',
       fg='#292b2c',
       activeforeground='#fff',
       command=convert).grid(row=3, pady=40, columnspan=4, ipady=10)
check = IntVar()
Checkbutton(text='Auto', variable=check, font=('ariel', 18), height=2,
            highlightthickness=3,  onvalue=1, offvalue=0, command=isChecked).grid(row=2, column=2)

app.mainloop()
