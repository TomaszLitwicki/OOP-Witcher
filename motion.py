import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ruch po mapie")
root.resizable(False, False)

plansza = tk.Canvas(root, width=400, height=400, bg ="black")
plansza.pack()

x, y = 200, 200
postac = plansza.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')
punkty_ruchu = 3


def ruch(event):
    global punkty_ruchu
    krok = 20
    x1, y1, x2, y2 = plansza.coords(postac)

    if punkty_ruchu > 0:
        if event.keysym == "Up" and y1 - krok >= 10 :
            plansza.move(postac, 0, -krok)
            punkty_ruchu -= 1
        elif event.keysym == "Down" and y2 + krok <= 390:
            plansza.move(postac, 0, krok)
            punkty_ruchu -= 1
        elif event.keysym == "Left" and x1 - krok >= 10:
            plansza.move(postac, -krok, 0)
            punkty_ruchu -= 1
        elif event.keysym == "Right" and x2 + krok <= 390:
            plansza.move(postac, krok, 0)
            punkty_ruchu -= 1
        else:
            messagebox.showwarning("Krawędź!", "Dalej nie przejdziesz, zawracaj...")
    else:
        messagebox.showinfo("KONIEC RUCHU", "Nie masz już więcej ruchu, zakończ rundę.")

def koniec_tury():
    global punkty_ruchu
    decyzja = messagebox.askyesno("Koniec tury", "Czy chcesz zakończyć turę?")
    if decyzja:
        # Logika ruchu potwora
        punkty_ruchu = 3
        print("Tura potwora zakończona, Twój ruch!")

def koniec_gry():
    decyzja = messagebox.askyesno("Koniec gry", "Czy chcesz zakończyć grę i wyjść z programu?")
    if decyzja:
        root.destroy()

root.bind("<KeyPress-Up>", ruch)
root.bind("<KeyPress-Down>", ruch)
root.bind("<KeyPress-Left>", ruch)
root.bind("<KeyPress-Right>", ruch)


tk.Button(root, text="RUNDA", command=koniec_tury).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(root, text="koniec", command=koniec_gry).pack(side=tk.RIGHT, pady=5, padx=10)

root.mainloop()