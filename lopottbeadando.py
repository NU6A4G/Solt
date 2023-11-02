import tkinter as tk
from tkinter import font as tkFont
import sqlite3
import os
import csv

class AdatbazisKezelo:
    def __init__(self, ablak):
        self.ablak = ablak
        self.ablak.title("Adatbázis Kezelő")
        self.ablak.geometry("660x320")
        if not os.path.exists("data.db"):
            self.uj_adatbazis_letrehozas()

        self.db = sqlite3.connect("data.db")
        self.cursor = self.db.cursor()

        self.ablak.configure(bg="#f0f0f0")

        self.rekordok_lista = tk.Listbox(self.ablak, bg="white", selectbackground="blue", font=("Helvetica", 12))
        self.rekordok_lista.pack(fill="both", expand=True, padx=5, pady=5)

        self.torol_gomb = tk.Button(self.ablak, text="Rekord törlése", command=self.torol_rekord, bg="#FF5733", fg="white", font=("Helvetica", 12))
        self.torol_gomb.pack(side="bottom", pady=5)  # A "Rekord törlése" gomb alulra helyezése

        self.uj_rekord_gomb = tk.Button(self.ablak, text="Új rekord", command=self.uj_rekord, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.uj_rekord_gomb.pack(side="bottom", pady=5)

        # Korábban mentett adatok betöltése
        self.frissit_lista()

    def uj_adatbazis_letrehozas(self):
        self.db = sqlite3.connect("data.db")
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS adatok (id INTEGER PRIMARY KEY, nev TEXT, email TEXT)''')
        self.db.commit()

    def uj_rekord(self):
        rekord_dialog = tk.Toplevel(self.ablak)
        rekord_dialog.title("Rekord hozzáadása")

        nev_cimke = tk.Label(rekord_dialog, text="Név:", font=("Helvetica", 12))
        nev_cimke.pack()

        nev_mezo = tk.Entry(rekord_dialog)
        nev_mezo.pack()

        email_cimke = tk.Label(rekord_dialog, text="E-mail:", font=("Helvetica", 12))
        email_cimke.pack()

        email_mezo = tk.Entry(rekord_dialog)
        email_mezo.pack()

        mentes_gomb = tk.Button(rekord_dialog, text="Mentés", command=lambda: self.mentes_es_frisstes(nev_mezo.get(), email_mezo.get(), rekord_dialog), font=("Helvetica", 12))
        mentes_gomb.pack()

    def torol_rekord(self):
        kijelolt_index = self.rekordok_lista.curselection()
        if kijelolt_index:
            kijelolt_index = kijelolt_index[0]
            rekord_id = self.rekordok_lista.get(kijelolt_index).split(' - ')[0]
            self.cursor.execute("DELETE FROM adatok WHERE id=?", (rekord_id,))
            self.db.commit()
            self.frissit_lista()

    def mentes_es_frisstes(self, nev, email, rekord_dialog):
        self.cursor.execute("INSERT INTO adatok (nev, email) VALUES (?, ?)", (nev, email))
        self.db.commit()
        rekord_dialog.destroy()
        self.frissit_lista()

    def frissit_lista(self):
        self.rekordok_lista.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM adatok")
        rekordok = self.cursor.fetchall()
        for rekord in rekordok:
            self.rekordok_lista.insert(tk.END, f"{rekord[0]} - {rekord[1]} - {rekord[2]}")

        # Adatok mentése CSV fájlba
        self.mentes_csv()

    def mentes_csv(self):
        self.cursor.execute("SELECT * FROM adatok")
        rekordok = self.cursor.fetchall()
        with open('adatok.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['ID', 'Név', 'E-mail'])
            csv_writer.writerows(rekordok)

if __name__ == "__main__":
    root = tk.Tk()
    alkalmazas = AdatbazisKezelo(root)
    root.mainloop()