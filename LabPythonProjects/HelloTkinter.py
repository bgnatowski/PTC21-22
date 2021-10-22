import tkinter as tk


def zmienSlowoNaASCII(slowo):
    kodAsciiZera = ord("0")
    wynik = ""
    for i in range(len(slowo)):
        znak = slowo[i]
        # wynik += f"{znak}={ord(znak)-kodAsciiZera}\n"
        wynik += f"{znak}={ord(znak)}\n"
    return wynik


def show_entry_fields():
    root = tk.Tk()

    wynik = zmienSlowoNaASCII(e1.get())
    T = tk.Text(root, height=20, width=20)
    T.grid(row=1, column=0)
    T.pack()
    T.insert(tk.END, wynik)

    tk.mainloop()


master = tk.Tk()
tk.Label(master,
         text="Podaj slowo").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Podaj litery i ascii', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()



