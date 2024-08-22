from tkinter import *
from tkinter import filedialog
from googletrans import Translator
import pyttsx3
from gtts import gTTS
import os

# GUI Creation
window = Tk()
window.title("Language Translator ___RSP___")
window.geometry('640x480+100+100')
window.configure(bg='#FDC3DC')

# Initializing Translator and Speech Engine
translator = Translator()
engine = pyttsx3.init()
engine.setProperty("rate", 150)

Post_lang_Choice = StringVar()
# Setting a default Language for Translation
Post_lang_Choice.set('english')
# Creating a dictionary for the set of Languages available
lang = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
        'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
        'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
        'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
        'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
        'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
        'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
        'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
        'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
        'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
        'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese',
        'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
        'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
        'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
        'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
        'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
        'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
        'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# Putting language values (not the symbol) into the list
languages = [langs for langs in lang.values()]


# Function for Exception of non entry of text
def exc():
    print("Please Enter text first")
    engine.say("Please Enter text first")
    engine.runAndWait()


# Function for Selecting the text File
def TF():
    print("Selecting File....")
    text_file = filedialog.askopenfilename(initialdir=r"C:\Users\nandh\OneDrive\Desktop\Minor project",
                                           title="Select a text File to be translated",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    print(text_file)

    with open(text_file) as text:
        contents = text.read()
        print(contents)
        Input_TextBox.delete('1.0', END)
        Input_TextBox.insert(END, contents)
        text.close()


# Function for Pronouncing the text using pyttsx3
def Pronounce():
    try:
        # Extract language code
        key_list = list(lang.keys())
        val_list = list(lang.values())
        end_lan = Post_lang_Choice.get()
        end_position = val_list.index(end_lan)
        ep = key_list[end_position]

        # Translate the text
        trans = translator.translate(Input_TextBox.get("1.0", END), dest=ep)

        # Get pronunciation or fallback to translated text
        pronunciation_text = trans.pronunciation if trans.pronunciation else trans.text
        print("Pronunciation:", pronunciation_text)
        
        # Speak the text
        engine.say(pronunciation_text)
        engine.runAndWait()
    except Exception as e:
        print("Error in pronunciation:", e)
        exc()


# Function for Pronouncing the text using gTTS
def Pronounce_with_gTTS():
    try:
        # Extract language code
        key_list = list(lang.keys())
        val_list = list(lang.values())
        end_lan = Post_lang_Choice.get()
        end_position = val_list.index(end_lan)
        ep = key_list[end_position]

        # Translate the text
        trans = translator.translate(Input_TextBox.get("1.0", END), dest=ep)

        # Generate speech using gTTS
        tts = gTTS(text=trans.text, lang=ep)
        tts.save("output.mp3")
        os.system("start output.mp3")  # Use "start" on Windows, "open" on macOS, or "xdg-open" on Linux
    except Exception as e:
        print("Error in pronunciation:", e)
        exc()


# Function for Translating the text
def Translate():
    try:
        # Extract language code
        key_list = list(lang.keys())
        val_list = list(lang.values())
        end_lan = Post_lang_Choice.get()
        end_position = val_list.index(end_lan)
        ep = key_list[end_position]
        print(ep)
        
        # Translate the text
        trans = translator.translate(Input_TextBox.get("1.0", END), dest=ep)
        print(trans)
        Translated_TextBox.config(state=NORMAL)
        Translated_TextBox.delete('1.0', END)
        Translated_TextBox.insert(END, trans.text)
        Translated_TextBox.config(state=DISABLED)
    except Exception as e:
        print(e)
        exc()


# Function to clear the text boxes
def clear():
    Input_TextBox.delete('1.0', END)  # Clear input text
    Translated_TextBox.config(state=NORMAL)
    Translated_TextBox.delete('1.0', END)  # Clear translated text
    Translated_TextBox.config(state=DISABLED)


# Creating OptionMenu, Labels and Buttons on the Window for ease
Post_lang_Menu = OptionMenu(window, Post_lang_Choice, *languages)
Post_lang_Menu.config(bg='#EAB543')
Post_lang_Label = Label(window, text="Choose Translate Language",
                        font=('System', 12))
Post_lang_Label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
Post_lang_Menu.grid(row=0, column=1, padx=10, pady=10, sticky=W)

Input_lang_Label = Label(window, text="Enter Text below",
                         font=('System', 16), bg='#FD7272')
Input_lang_Label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Create a Text widget and Scrollbar for input
input_frame = Frame(window)
input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

input_scrollbar = Scrollbar(input_frame)
input_scrollbar.pack(side=RIGHT, fill=Y)

Input_TextBox = Text(input_frame, width=60, height=10, font=('Georgia', 14), yscrollcommand=input_scrollbar.set)
Input_TextBox.pack(side=LEFT, fill=BOTH, expand=True)
input_scrollbar.config(command=Input_TextBox.yview)

# Create a Text widget and Scrollbar for output
output_frame = Frame(window)
output_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

output_scrollbar = Scrollbar(output_frame)
output_scrollbar.pack(side=RIGHT, fill=Y)

Translated_TextBox = Text(output_frame, width=60, height=10, font=('Georgia', 14), yscrollcommand=output_scrollbar.set, state=DISABLED)
Translated_TextBox.pack(side=LEFT, fill=BOTH, expand=True)
output_scrollbar.config(command=Translated_TextBox.yview)

# Creating Buttons
translate_button = Button(window, text="Translate", command=Translate, bg='#6AB04C', font=('System', 12))
translate_button.grid(row=4, column=0, padx=10, pady=10, sticky=W)

clear_button = Button(window, text="Clear", command=clear, bg='#F8C471', font=('System', 12))
clear_button.grid(row=4, column=1, padx=10, pady=10, sticky=W)

file_button = Button(window, text="Select File", command=TF, bg='#FF6F61', font=('System', 12))
file_button.grid(row=5, column=0, padx=10, pady=10, sticky=W)

pronounce_button = Button(window, text="Pronounce", command=Pronounce, bg='#B5EAD7', font=('System', 12))
pronounce_button.grid(row=5, column=1, padx=10, pady=10, sticky=W)

pronounce_gtts_button = Button(window, text="Pronounce with gTTS", command=Pronounce_with_gTTS, bg='#F6C6C6', font=('System', 12))
pronounce_gtts_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=W)

window.mainloop()

