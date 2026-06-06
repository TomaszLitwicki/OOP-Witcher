import tkinter as tk
from tkinter import messagebox
import time

class Wiedzmin:
    def __init__(self, plansza, start_x, start_y):
        self.plansza = plansza
        self.xw = start_x
        self.yw = start_y
        self.punkty_ruchu = 3

        self.postac = plansza.create_oval(start_x - 10, start_y - 10, start_x + 10, start_y + 10, fill='red')

    def wykonaj_krok(self, kierunek):
        krok = 20
        x1, y1, x2, y2 = self.plansza.coords(self.postac)

        if self.punkty_ruchu > 0:
            if kierunek == "Up" and y1 - krok >= 10:
                self.plansza.move(self.postac, 0, -krok)
                self.yw -= krok
                self.punkty_ruchu -= 1
                print(f"współrzędne Geralta: ({self.xw}, {self.yw})")
            elif kierunek == "Down" and y2 + krok <= 390:
                self.plansza.move(self.postac, 0, krok)
                self.yw += krok
                self.punkty_ruchu -= 1
                print(f"współrzędne Geralta: ({self.xw}, {self.yw})")
            elif kierunek == "Left" and x1 - krok >= 10:
                self.plansza.move(self.postac, -krok, 0)
                self.xw -= krok
                self.punkty_ruchu -= 1
                print(f"współrzędne Geralta: ({self.xw}, {self.yw})")
            elif kierunek == "Right" and x2 + krok <= 390:
                self.plansza.move(self.postac, krok, 0)
                self.xw += krok
                self.punkty_ruchu -= 1
                print(f"współrzędne Geralta: ({self.xw}, {self.yw})")
            else:
                messagebox.showwarning("Krawędź!", "Dalej nie przejdziesz, zawracaj...")
        else:
            messagebox.showinfo("KONIEC RUCHU", "Nie masz już więcej ruchu, zakończ rundę.")
            


class Potwor:
    def __init__(self, plansza, x, y):
        self.plansza = plansza
        self.xp = x
        self.yp = y
        self.punkty_ruchu = 3
        self.monster = plansza.create_oval(x-10,y-10,x+10,y+10,fill='yellow')

    def ruch_potwora(self):
        krok = 20

        xo = geralt.xw - self.xp
        yo = geralt.yw - self.yp



        while self.punkty_ruchu > 0 and (xo != 0 or yo != 0):

            mozliwe_ruchy = []
            if self.xp + krok <= 380:
                mozliwe_ruchy.append('prawo')
            if self.xp - krok >= 20:
                mozliwe_ruchy.append('lewo')
            if self.yp + krok <= 380:
                mozliwe_ruchy.append('dol')
            if self.yp - krok >= 20:
                mozliwe_ruchy.append('gora')

            print(f"możliwe ruchy potwora: {mozliwe_ruchy}")

            if abs(xo) > abs(yo):
                if xo > 0 and 'prawo' in mozliwe_ruchy:
                    self.plansza.move(self.monster, krok, 0)
                    self.xp += krok
                    self.punkty_ruchu -= 1
                    print(f"współrzędne potwora: ({self.xp}, {self.yp})")
                    plansza.update()
                    time.sleep(1)
                elif xo < 0 and 'lewo' in mozliwe_ruchy:
                    self.plansza.move(self.monster, -krok, 0)
                    self.xp -= krok
                    self.punkty_ruchu -= 1  
                    print(f"współrzędne potwora: ({self.xp}, {self.yp})")
                    plansza.update()
                    time.sleep(1)
            elif abs(yo) > abs(xo):
                if yo > 0 and 'dol' in mozliwe_ruchy:
                    self.plansza.move(self.monster, 0, krok)
                    self.yp += krok
                    self.punkty_ruchu -= 1
                    print(f"współrzędne potwora: ({self.xp}, {self.yp})")
                    plansza.update()
                    time.sleep(1)
                elif yo < 0 and 'gora' in mozliwe_ruchy:
                    self.plansza.move(self.monster, 0, -krok)
                    self.yp -= krok
                    self.punkty_ruchu -= 1
                    print(f"współrzędne potwora: ({self.xp}, {self.yp})")
                    plansza.update()
                    time.sleep(1)
            else:
                pass
            

def rysuj_siatke(plansza, skok, rozmiar_planszy):
    for i in range (int(0+skok/2), rozmiar_planszy, skok):
        plansza.create_line(i, 0, i, rozmiar_planszy, fill="gray15")
    for i in range (int(0+skok/2), rozmiar_planszy, skok):
        plansza.create_line(0, i, rozmiar_planszy, i, fill="gray15")


def nasluchuj_klawiszy(event):
    geralt.wykonaj_krok(event.keysym)
    etykieta_pr.config(text=f"TWOJA RUNDA - Punkty ruchu: {geralt.punkty_ruchu}")

def koniec_tury(event = None):
    decyzja = messagebox.askyesno("Koniec tury", "Czy chcesz zakończyć turę?")
    if decyzja:
        etykieta_pr.config(text=f"RUNDA POTWORA! Czekaj...")
        potwor.punkty_ruchu = 3
        potwor.ruch_potwora()
        geralt.punkty_ruchu = 3
        print("Tura potwora zakończona, Twój ruch!")
        etykieta_pr.config(text=f"TWOJA RUNDA - Punkty ruchu: {geralt.punkty_ruchu}")

def koniec_gry(event = None):
    decyzja = messagebox.askyesno("Koniec gry", "Czy chcesz zakończyć grę i wyjść z programu?")
    if decyzja:
        root.destroy()

root = tk.Tk()
root.title("Ruch po mapie")
root.resizable(False, False)

etykieta_pr = tk.Label(root, text = "TWOJA RUNDA - Punkty ruchu: 3", font=("Arial", 12, "bold"))
etykieta_pr.pack(pady=5)

rozmiar_planszy = 400
skok = 20
plansza = tk.Canvas(root, width=rozmiar_planszy, height=rozmiar_planszy, bg ="black")
plansza.pack()

rysuj_siatke(plansza,skok,rozmiar_planszy)
geralt = Wiedzmin(plansza, 200, 200)
potwor = Potwor(plansza, 20, 20)

root.bind("<KeyPress-Up>", nasluchuj_klawiszy)
root.bind("<KeyPress-Down>", nasluchuj_klawiszy)
root.bind("<KeyPress-Left>", nasluchuj_klawiszy)
root.bind("<KeyPress-Right>", nasluchuj_klawiszy)
root.bind("<KeyPress-r>", koniec_tury)
root.bind("<Escape>", koniec_gry)


tk.Button(root, text="RUNDA", command=koniec_tury).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(root, text="koniec", command=koniec_gry).pack(side=tk.RIGHT, pady=5, padx=10)

root.mainloop()