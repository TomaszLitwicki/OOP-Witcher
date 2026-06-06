import tkinter as tk
from tkinter import messagebox

class Wiedzmin:
    def __init__(self, plansza, start_x, start_y):
        self.plansza = plansza
        self.punkty_ruchu = 3

        self.postac = plansza.create_oval(start_x - 10, start_y - 10, start_x + 10, start_y + 10, fill='red')

    def wykonaj_krok(self, kierunek):
        krok = 20
        x1, y1, x2, y2 = self.plansza.coords(self.postac)

        if self.punkty_ruchu > 0:
            if kierunek == "Up" and y1 - krok >= 10:
                self.plansza.move(self.postac, 0, -krok)
                self.punkty_ruchu -= 1
            elif kierunek == "Down" and y2 + krok <= 390:
                self.plansza.move(self.postac, 0, krok)
                self.punkty_ruchu -= 1
            elif kierunek == "Left" and x1 - krok >= 10:
                self.plansza.move(self.postac, -krok, 0)
                self.punkty_ruchu -= 1
            elif kierunek == "Right" and x2 + krok <= 390:
                self.plansza.move(self.postac, krok, 0)
                self.punkty_ruchu -= 1
            else:
                messagebox.showwarning("Krawędź!", "Dalej nie przejdziesz, zawracaj...")
        else:
            messagebox.showinfo("KONIEC RUCHU", "Nie masz już więcej ruchu, zakończ rundę.")

root = tk.Tk()
root.title("Ruch po mapie")
root.resizable(False, False)

etykieta_pr = tk.Label(root, text = "TWOJA RUNDA - Punkty ruchu: 3", font=("Arial", 12, "bold"))
etykieta_pr.pack(pady=5)

rozmiar_planszy = 400
skok = 20
plansza = tk.Canvas(root, width=rozmiar_planszy, height=rozmiar_planszy, bg ="black")
plansza.pack()

def rysuj_siatke(plansza, skok, rozmiar_planszy):
    for i in range (int(0+skok/2), rozmiar_planszy, skok):
        plansza.create_line(i, 0, i, rozmiar_planszy, fill="gray15")
    for i in range (int(0+skok/2), rozmiar_planszy, skok):
        plansza.create_line(0, i, rozmiar_planszy, i, fill="gray15")
rysuj_siatke(plansza,skok,rozmiar_planszy)


geralt = Wiedzmin(plansza, 200, 200)

def nasluchuj_klawiszy(event):
    geralt.wykonaj_krok(event.keysym)
    etykieta_pr.config(text=f"TWOJA RUNDA - Punkty ruchu: {geralt.punkty_ruchu}")

def koniec_tury(event = None):
    decyzja = messagebox.askyesno("Koniec tury", "Czy chcesz zakończyć turę?")
    if decyzja:
        # Logika ruchu potwora
        geralt.punkty_ruchu = 3
        print("Tura potwora zakończona, Twój ruch!")
        etykieta_pr.config(text=f"TWOJA RUNDA - Punkty ruchu: {geralt.punkty_ruchu}")

def koniec_gry(event = None):
    decyzja = messagebox.askyesno("Koniec gry", "Czy chcesz zakończyć grę i wyjść z programu?")
    if decyzja:
        root.destroy()


root.bind("<KeyPress-Up>", nasluchuj_klawiszy)
root.bind("<KeyPress-Down>", nasluchuj_klawiszy)
root.bind("<KeyPress-Left>", nasluchuj_klawiszy)
root.bind("<KeyPress-Right>", nasluchuj_klawiszy)
root.bind("<KeyPress-r>", koniec_tury)
root.bind("<Escape>", koniec_gry)


tk.Button(root, text="RUNDA", command=koniec_tury).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(root, text="koniec", command=koniec_gry).pack(side=tk.RIGHT, pady=5, padx=10)

root.mainloop()