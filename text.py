import tkinter as tk

languages = {
    'EN': {
        'drink': 'beer',
        'food': 'burger',
        },
    'DE': {
        'drink': 'bier',
        'food': 'wienerschnitzel'
        },
    'ES': {
        'drink': 'cerveza',
        'food': 'taco'
        }
    }


class LangManager:
    def __init__(self):
        self.food = tk.StringVar()
        self.drink = tk.StringVar()

        self.update('EN') # set boot language

    def update(self, new_lang):
        for key, value in languages[new_lang].items():
            getattr(self, key).set(value)


class App(tk.Frame):
    def __init__(self, master=None, **kwargs): # *args is pointless here; tk.Frame takes no further positional arguments.
        tk.Frame.__init__(self, master, **kwargs)

        self.lang = LangManager()
        opt = tk.OptionMenu(self, tk.StringVar(value='EN'), *languages, command=self.lang.update)
        opt.pack()

        self.drink = tk.Label(self, textvariable=self.lang.drink)
        self.drink.pack()

        self.food = tk.Label(self, textvariable=self.lang.food)
        self.food.pack()


root = tk.Tk()
win = App(root)
win.pack()
root.mainloop()