from main import *

class App:
    def __init__(self, master):
        self.progress_line(master)

    def progress_line(self, master):
        self._progressbar = ttk.Progressbar(master, mode='indeterminate')
        self._progressbar.place(anchor='ne', height="20", width="150",
                                x="175", y="30")
    @property
    def progressbar(self):
        return self._progressbar # return value of private member

class AppMenu(object):
    def __init__(self, master, progressbar):
        self.master = master
        self.menu_bar()
        self.progressbar = progressbar

    def menu_bar(self):
        self.menu_bar = Tkinter.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.create_menu = Tkinter.Menu(self.menu_bar, tearoff=False)
        self.create_menu.add_command(label="do foo", command=self.do_foo)
        self.menu_bar.add_cascade(label="now", menu=self.create_menu)

    def do_foo(self):
        confirm = ConfirmationDialog(self.master, title="Do foo?")
        self.master.update() # needed to completely remove conf dialog
        if confirm.choice:
            foo(self.progressbar)

class ConfirmationDialog(tkSimpleDialog.Dialog):
    def __init__(self, parent, title=None):
        self.choice = False
        tkSimpleDialog.Dialog.__init__(self, parent, title=title)

    def apply(self):
        self.choice = True

def foo(progressbar):
    progressbar.start()
    for _ in range(50):
        time.sleep(.1) # simulate some work
        progressbar.step(10)
        progressbar.update_idletasks()
    progressbar.stop()

master = Tkinter.Tk()
master.title("Foo runner")
app = App(master)
appmenu = AppMenu(master, app.progressbar)
master.mainloop()