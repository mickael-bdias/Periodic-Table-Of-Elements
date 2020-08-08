import tkinter as root
from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk, Image

import progressBarEuropeAmerica
import periodicTableRoot

progress_english = progressBarEuropeAmerica.ProgressEnglishPage
progress_portuguese = progressBarEuropeAmerica.ProgressPortuguesePage
progress_spanish = progressBarEuropeAmerica.ProgressSpanishPage
periodic_table_root = periodicTableRoot.Elements

languages = {
    'EN': {
        'title': 'Periodic Table of Elements | Industry 4.0 All',
        'select_language': 'Select a language',
        },
    'PT': {
        'title': 'Tabela Periódica dos Elementos | Industry 4.0 All',
        'select_language': 'Selecione um idioma',
        },
    'ES': {
        'title': 'Tabla Periódica de Elementos | Industry 4.0 All',
        'select_language': 'Selecciona un idioma',
        },
    'FR': {
        'title': 'Tableau Périodique des Éléments | Industry 4.0 All',
        'select_language': 'Sélectionnez une langue',
         },
    'IT': {
        'title': 'Tavola Periodica degli Elementi | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'RO': {
        'title': 'Tabelul Periodic al Elementelor | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'DE': {
        'title': 'Periodensystem der Elemente | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'NL': {
        'title': 'Periodiek Systeem der Elementen | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'DK': {
        'title': 'Periodisk Tabel over Elementer | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'FI': {
        'title': 'Aineellinen Jaksollinen Taulukko | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'HU': {
        'title': 'Periódusos Elemek Táblája | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'GR': {
        'title': 'Περιοδικός Πίνακας Στοιχείων | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'CZ': {
        'title': 'Periodická Tabulka Prvků | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'PL': {
        'title': 'Układ Okresowy Pierwiastków | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'RU': {
        'title': 'Периодическая таблица элементов | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'ET': {
        'title': 'الجدول الدوري للعناصر | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'IL': {
        'title': 'לוח יסודות תקופתי | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    'SD': {
        'title': 'Jedwali la Vipindi vya Vipindi | Industry 4.0 All',
        'select_language': 'Seleziona una lingua',
    },
    }


class LangManager:
    def __init__(self):
        self.title = root.StringVar()
        self.select_language = root.StringVar()
        self.update('EN') # set boot language

    def update(self, new_lang):
        for key, value in languages[new_lang].items():
            getattr(self, key).set(value)


#  Setup class who are inheriting everything from the root.Tk class (only at the local class level).
class PeriodicTable(root.Tk):
    # Init (initialize) method
    def __init__(self):
        # Initializing the inherited class
        root.Tk.__init__(self)
        root.Tk.wm_title(self, "Periodic Table of Elements | Industry 4.0 All")
        root.Tk.iconbitmap(self, default="Images/logo.ico")

        # Defining container (which will be filled with a bunch of frames to be accessed later on)
        container = root.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Defining frames
        self.frames = {}
        for frame_window in (MainPage, progress_english, progress_portuguese, progress_spanish, periodic_table_root):
            frame = frame_window(container, self)
            self.frames[frame_window] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Call "show_frame" method to bring a frame of our choosing
        self.show_frame(MainPage)

    def show_frame(self, cont):
        # Defining frame as self.frame, followed by cont, which is the key
        frame = self.frames[cont]
        # Bring our frame to the top for the user to see.
        frame.tkraise()


#  MainPage class who are inheriting from root.Frame
class MainPage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)

        # Select languages - Options menu
        self.lang = LangManager()
        lang_select = root.OptionMenu(self, root.StringVar(value='EN'), *languages, command=self.lang.update)
        lang_select.grid(row=1, column=2)

        title_text = root.Label(self, textvariable=self.lang.title)
        title_text.config(font=("Dubai Medium", 18))
        title_text.grid(row=0, column=0, columnspan=4)

        select_language_text = root.Label(self, textvariable=self.lang.select_language)
        select_language_text.config(font=("Dubai Medium", 13))
        select_language_text.grid(row=1, column=0, columnspan=4)

        select_icon_flag_text = root.Label(self, text="... And click in an icon flag")
        select_icon_flag_text.config(font=("Dubai Medium", 13))
        select_icon_flag_text.grid(row=1, column=3)

        # Frames
        frame_europe = root.LabelFrame(self, padx=7, pady=7)
        frame_europe.grid(row=3, column=0)

        frame_welcome_image = LabelFrame(self, padx=7, pady=7)
        frame_welcome_image.grid(row=3, column=2)

        frame_africa = LabelFrame(self, padx=7, pady=7)
        frame_africa.grid(row=3, column=3)

        # Creating the UK language flag button Widget and put it on screen
        self.uk_welcome = ImageTk.PhotoImage(Image.open("Images/UK-64.png"))
        uk_button = ttk.Button(frame_europe, text="ENGLISH", image=self.uk_welcome, compound=TOP,
                               width=16, command=lambda: controller.show_frame(progress_english))
        uk_button.grid(row=0, column=0, padx=2, pady=2)
        # Creating the Portugal language flag button Widget and put it on screen
        self.portugal_welcome = ImageTk.PhotoImage(Image.open("Images/Portugal-64.png"))
        portugal_button = ttk.Button(frame_europe, text="PORTUGUÊS", image=self.portugal_welcome, compound=TOP,
                                     width=16, command=lambda: controller.show_frame(progress_portuguese))
        portugal_button.grid(row=0, column=1, padx=2, pady=2)
        # Creating the Spain language flag button Widget and put it on screen
        self.spain_welcome = ImageTk.PhotoImage(Image.open("Images/Spain-64.png"))
        spain_button = ttk.Button(frame_europe, text="ESPAÑOL", image=self.spain_welcome, compound=TOP,
                                  width=16, command=lambda: controller.show_frame(progress_spanish))
        spain_button.grid(row=0, column=2, padx=2, pady=2)
        # Creating the France language flag button Widget and put it on screen
        self.france_welcome = ImageTk.PhotoImage(Image.open("Images/France-64.png"))
        france_button = ttk.Button(frame_europe, text="FRANÇAIS", image=self.france_welcome, compound=TOP, width=16)
        france_button.grid(row=0, column=3, padx=2, pady=2)
        # Creating the Italy language flag button Widget and put it on screen
        self.italy_welcome = ImageTk.PhotoImage(Image.open("Images/Italy-64.png"))
        italy_button = ttk.Button(frame_europe, text="ITALIANO", image=self.italy_welcome, compound=TOP, width=16)
        italy_button.grid(row=0, column=4, padx=2, pady=2)
        # Creating the Romania language flag button Widget and put it on screen
        self.romania_welcome = ImageTk.PhotoImage(Image.open("Images/Romania-64.png"))
        romania_button = ttk.Button(frame_europe, text="ROMÂNĂ", image=self.romania_welcome, compound=TOP, width=16)
        romania_button.grid(row=1, column=0, padx=2, pady=2)
        # Creating the Germany language flag button Widget and put it on screen
        self.germany_welcome = ImageTk.PhotoImage(Image.open("Images/Germany-64.png"))
        germany_button = ttk.Button(frame_europe, text="DEUTSCHE", image=self.germany_welcome, compound=TOP, width=16)
        germany_button.grid(row=1, column=1, padx=2, pady=2)
        # Creating the Netherlands language flag button Widget and put it on screen
        self.netherlands_welcome = ImageTk.PhotoImage(Image.open("Images/Netherlands-64.png"))
        netherlands_button = ttk.Button(frame_europe, text="NEDERLANDS", image=self.netherlands_welcome,
                                        compound=TOP, width=16)
        netherlands_button.grid(row=1, column=2, padx=2, pady=2)
        # Creating the Denmark language flag button Widget and put it on screen
        self.denmark_welcome = ImageTk.PhotoImage(Image.open("Images/Denmark-64.png"))
        denmark_button = ttk.Button(frame_europe, text="DANSK", image=self.denmark_welcome, compound=TOP, width=16)
        denmark_button.grid(row=1, column=3, padx=2, pady=2)
        # Creating the Finland language flag button Widget and put it on screen
        self.finland_welcome = ImageTk.PhotoImage(Image.open("Images/Finland-64.png"))
        finland_button = ttk.Button(frame_europe, text="SUOMALAINEN", image=self.finland_welcome, compound=TOP, width=16)
        finland_button.grid(row=1, column=4, padx=2, pady=2)
        # Creating the Hungary language flag button Widget and put it on screen
        self.hungary_welcome = ImageTk.PhotoImage(Image.open("Images/Hungary-64.png"))
        hungary_button = ttk.Button(frame_europe, text="MAGYAR", image=self.hungary_welcome, compound=TOP, width=16)
        hungary_button.grid(row=2, column=0, padx=2, pady=2)
        # Creating the Greece language flag button Widget and put it on screen
        self.greece_welcome = ImageTk.PhotoImage(Image.open("Images/Greece-64.png"))
        greece_button = ttk.Button(frame_europe, text="ΕΛΛΗΝΙΚΑ", image=self.greece_welcome, compound=TOP, width=16)
        greece_button.grid(row=2, column=1, padx=2, pady=2)
        # Creating the Czech Republic language flag button Widget and put it on screen
        self.czech_welcome = ImageTk.PhotoImage(Image.open("Images/Czech-republic-64.png"))
        czech_button = ttk.Button(frame_europe, text="ČEŠTINA", image=self.czech_welcome, compound=TOP, width=16)
        czech_button.grid(row=2, column=2, padx=2, pady=2)
        # Creating the Poland language flag button Widget and put it on screen
        self.poland_welcome = ImageTk.PhotoImage(Image.open("Images/Poland-64.png"))
        poland_button = ttk.Button(frame_europe, text="POLSKIE", image=self.poland_welcome, compound=TOP, width=16)
        poland_button.grid(row=2, column=3, padx=2, pady=2)
        # Creating the Russia language flag button Widget and put it on screen
        self.russia_welcome = ImageTk.PhotoImage(Image.open("Images/Russia-64.png"))
        russia_button = ttk.Button(frame_europe, text="РУССКИЙ", image=self.russia_welcome, compound=TOP, width=16)
        russia_button.grid(row=2, column=4, padx=2, pady=2)

        self.image_welcome = ImageTk.PhotoImage(Image.open("Images/welcome_image.jpg"))
        image_welcome_label = ttk.Label(frame_welcome_image, image=self.image_welcome)
        image_welcome_label.grid(row=0, column=0, padx=1, pady=1)

        # Creating the Egypt language flag button Widget and put it on screen
        self.egypt_welcome = ImageTk.PhotoImage(Image.open("Images/Egypt-64.png"))
        egypt_button = ttk.Button(frame_africa, text="عربى", image=self.egypt_welcome, compound=TOP, width=16)
        egypt_button.grid(row=0, column=0, padx=2, pady=2)
        # Creating the Israel language flag button Widget and put it on screen
        self.israel_welcome = ImageTk.PhotoImage(Image.open("Images/Israel-64.png"))
        israel_button = ttk.Button(frame_africa, text="עִברִי", image=self.israel_welcome, compound=TOP, width=16)
        israel_button.grid(row=0, column=1, padx=2, pady=2)
        # Creating the Tanzania language flag button Widget and put it on screen
        self.tanzania_welcome = ImageTk.PhotoImage(Image.open("Images/Tanzania_64.png"))
        tanzania_button = ttk.Button(frame_africa, text="KISWAHILI", image=self.tanzania_welcome, compound=TOP, width=16)
        tanzania_button.grid(row=0, column=2, padx=2, pady=2)
        # Creating the India language flag button Widget and put it on screen
        self.india_welcome = ImageTk.PhotoImage(Image.open("Images/India-64.png"))
        india_button = ttk.Button(frame_africa, text="नहीं", image=self.india_welcome, compound=TOP, width=16)
        india_button.grid(row=1, column=0, padx=2, pady=2)
        # Creating the Thailand language flag button Widget and put it on screen
        self.thailand_welcome = ImageTk.PhotoImage(Image.open("Images/Thailand-64.png"))
        thailand_button = ttk.Button(frame_africa, text="ไทย", image=self.thailand_welcome, compound=TOP, width=16)
        thailand_button.grid(row=1, column=1, padx=2, pady=2)
        # Creating the Vietnam language flag button Widget and put it on screen
        self.vietnam_welcome = ImageTk.PhotoImage(Image.open("Images/Vietnam-64.png"))
        vietnam_button = ttk.Button(frame_africa, text="Tiếng Việt", image=self.vietnam_welcome, compound=TOP, width=16)
        vietnam_button.grid(row=1, column=2, padx=2, pady=2)
        # Creating the China language flag button Widget and put it on screen
        self.china_welcome = ImageTk.PhotoImage(Image.open("Images/China-64.png"))
        china_button = ttk.Button(frame_africa, text="中文", image=self.china_welcome, compound=TOP, width=16)
        china_button.grid(row=2, column=0, padx=2, pady=2)
        # Creating the South Korea language flag button Widget and put it on screen
        self.korea_welcome = ImageTk.PhotoImage(Image.open("Images/SouthKorea-64.png"))
        korea_button = ttk.Button(frame_africa, text="한국어", image=self.korea_welcome, compound=TOP, width=16)
        korea_button.grid(row=2, column=1, padx=2, pady=2)
        # Creating the Japanese language flag button Widget and put it on screen
        self.japanese_welcome = ImageTk.PhotoImage(Image.open("Images/Japan-64.png"))
        japanese_button = ttk.Button(frame_africa, text="日本語", image=self.japanese_welcome, compound=TOP, width=16)
        japanese_button.grid(row=2, column=2, padx=2, pady=2)

        def popup_main_exit():
            response = messagebox.askyesno("Quit", "Are you sure you want to quit?")
            if response == 1:
                self.quit()

            else:
                messagebox.showinfo("Return", "You will now return to the application screen")

        button_exit = ttk.Button(self, text="Exit", command=popup_main_exit)
        button_exit.grid(row=5, column=0, columnspan=2, pady=5)


# Object of Periodic Table class
app = PeriodicTable()
app.mainloop()
