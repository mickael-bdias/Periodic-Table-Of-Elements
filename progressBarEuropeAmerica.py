import random
import time
import tkinter as root
from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk, Image

import messagesEuropeAmerica
import periodicTableRoot

# Variable for the class Elements from the script periodicTableRoot
elements = periodicTableRoot.Elements


# Creating a black text for visual structure. A welcome text will appear in the same spot in each country (at some time)
def black_text(self):
    welcome_blank = Label(self, text=" ")
    welcome_blank.config(font=("Dubai Medium", 12))
    welcome_blank.grid(row=1, column=0, padx=2, pady=2, columnspan=2)


# English page after selected UK language flag button Widget on the MainPage class
class ProgressEnglishPage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        self.parent = parent

        # Creating the UK flag image Label Widget and put it on screen
        self.progress_bar_uk = ImageTk.PhotoImage(Image.open("Images/UK-ProgressBar.jpg"))
        label_uk = Label(self, image=self.progress_bar_uk)
        label_uk.grid(row=0, column=0, padx=2, pady=2)

        # Creating the UK flag image Label Widget and put it on screen
        self.progress_bar_uk1 = ImageTk.PhotoImage(Image.open("Images/london-5297395_1280.jpg"))
        label_uk1 = Label(self, image=self.progress_bar_uk1)
        label_uk1.grid(row=0, column=1, padx=2, pady=2)

        # Call black_text function
        black_text(self)

        # Creating the Progress bar widget
        progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length=1400, mode="determinate")
        progress_bar.grid(row=3, column=0, padx=2, pady=2, columnspan=2)

        # Function for simulate a progress bar. Call by button_start_uk
        def fake_bar():
            # After progress bar, the buttons are destroyed
            button_exit_uk.destroy()
            button_start_uk.destroy()
            # Creating the message Label Widget and put it on screen
            welcome_text_uk = Label(self, text=random.choice(messagesEuropeAmerica.messages_en_uk))
            welcome_text_uk.config(font=("Dubai Medium", 12))
            welcome_text_uk.grid(row=1, column=0, padx=2, pady=2, columnspan=2)

            # Progress bar settings
            progress_bar["maximum"] = 100

            for i in range(101):
                time.sleep(0.04)
                progress_bar["value"] = i
                progress_bar.update()

            progress_bar["value"] = 100
            progress_bar.bell()

            # This button will appear after start is destroyed. If clicked the periodic_table_root will be showed
            button_continue_uk = ttk.Button(self, text="Continue", command=lambda: controller.show_frame(elements))
            button_continue_uk.grid(row=4, column=1, pady=4)

        # This button will initialize the progress bar
        button_start_uk = ttk.Button(self, text="Start", command=fake_bar)
        button_start_uk.grid(row=4, column=0, pady=4)

        # Function for showing the popup_exit_uk and the different options
        def popup_exit_uk():
            response = messagebox.askyesno("Quit", "Are you sure you want to quit?")
            if response == 1:
                self.quit()

            else:
                messagebox.showinfo("Return", "You will now return to the application screen")

        button_exit_uk = ttk.Button(self, text="Exit", command=popup_exit_uk)
        button_exit_uk.grid(row=4, column=1, pady=4)


# Portuguese page after selected Portugal language flag button Widget on the MainPage class
class ProgressPortuguesePage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        self.parent = parent

        # Creating the Portugal flag image Label Widget and put it on screen
        self.progress_bar_portugal = ImageTk.PhotoImage(Image.open("Images/UK-ProgressBar.jpg"))
        label_portugal = Label(self, image=self.progress_bar_portugal)
        label_portugal.grid(row=0, column=0, padx=2, pady=2, columnspan=2)

        # Call black_text function
        black_text(self)

        # Creating the Progress bar widget
        progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length=1000, mode="determinate")
        progress_bar.grid(row=3, column=0, padx=2, pady=2, columnspan=2)

        # Function for simulate a progress bar. Call by button_start_portugal
        def fake_bar():
            button_exit_portugal.destroy()

            # Creating the message Label Widget and put it on screen
            welcome_text_portugal = Label(self, text=random.choice(messagesEuropeAmerica.messages_pt_pt))
            welcome_text_portugal.config(font=("Dubai Medium", 12))
            welcome_text_portugal.grid(row=1, column=0, padx=2, pady=2, columnspan=2)

            # Progress bar settings
            progress_bar["maximum"] = 100

            for i in range(101):
                time.sleep(0.05)
                progress_bar["value"] = i
                progress_bar.update()

            progress_bar["value"] = 100
            progress_bar.bell()
            # After progress bar, the button used is destroyed
            button_start_portugal.destroy()

            # This button will appear after start is destroyed. If clicked the periodic_table_root will be showed
            button_continue = ttk.Button(self, text="Continuar", command=lambda: controller.show_frame(elements))
            button_continue.grid(row=4, column=1, pady=4)

        # This button will initialize the progress bar
        button_start_portugal = ttk.Button(self, text="Iniciar", command=fake_bar)
        button_start_portugal.grid(row=4, column=0, pady=4)

        # Function for showing the button_exit_portugal and the different options
        def button_exit_portugal():
            response = messagebox.askyesno("Sair", "Tens a certeza que queres sair?")
            if response == 1:
                self.quit()

            else:
                messagebox.showinfo("Retornar", "Agora retornarás à tela do aplicativo")

        button_exit_portugal = ttk.Button(self, text="Sair", command=button_exit_portugal)
        button_exit_portugal.grid(row=4, column=1, pady=4)


# Spanish page after selected Spain language flag button Widget on the MainPage class
class ProgressSpanishPage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        self.parent = parent

        # Creating the Spain flag image Label Widget and put it on screen
        self.progress_bar_spain = ImageTk.PhotoImage(Image.open("Images/Czech-republic-64.png"))
        label_spain = Label(self, image=self.progress_bar_spain)
        label_spain.grid(row=0, column=0, padx=2, pady=2, columnspan=2)

        # Call black_text function
        black_text(self)

        # Creating the Progress bar widget
        progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length=1000, mode="determinate")
        progress_bar.grid(row=3, column=0, padx=2, pady=2, columnspan=2)

        # Function for simulate a progress bar. Call by button_start_portugal
        def fake_bar():
            button_exit_spain.destroy()

            # Creating the message Label Widget and put it on screen
            welcome_text_spain = Label(self, text=random.choice(messagesEuropeAmerica.messages_es_es))
            welcome_text_spain.config(font=("Dubai Medium", 12))
            welcome_text_spain.grid(row=1, column=0, padx=2, pady=2, columnspan=2)

            # Progress bar settings
            progress_bar["maximum"] = 100

            for i in range(101):
                time.sleep(0.05)
                progress_bar["value"] = i
                progress_bar.update()

            progress_bar["value"] = 100
            progress_bar.bell()
            # After progress bar, the button used is destroyed
            button_start_spain.destroy()

            # This button will appear after start is destroyed. If clicked the periodic_table_root will be showed
            button_continue = ttk.Button(self, text="Seguir", command=lambda: controller.show_frame(elements))
            button_continue.grid(row=4, column=1, pady=4)

        # This button will initialize the progress bar
        button_start_spain = ttk.Button(self, text="Empezar", command=fake_bar)
        button_start_spain.grid(row=4, column=0, pady=4)

        # Function for showing the button_exit_portugal and the different options
        def button_exit_es_es():
            response = messagebox.askyesno("Salir", "¿Seguro que quieres salir?")
            if response == 1:
                self.quit()

            else:
                messagebox.showinfo("Volver", "Ahora volverás a la pantalla de la aplicación.")

        button_exit_spain = ttk.Button(self, text="Salir", command=button_exit_es_es)
        button_exit_spain.grid(row=4, column=1, pady=4)
