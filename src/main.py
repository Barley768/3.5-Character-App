import ui.main_window as mw

if __name__ == "__main__":
    root= mw.tk.Tk()
    app = mw.SimpleCharacterApp(root)
    root.mainloop()