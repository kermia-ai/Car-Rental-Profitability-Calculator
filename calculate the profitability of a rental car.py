import tkinter as tk

def calculer_rentabilite():
    try:
        ca_annuel = float(entree_ca_annuel.get())
        frais_mise_en_location = float(entree_frais.get())
        prix_voiture = float(entree_prix_voiture.get())

        rentabilite = ((ca_annuel - frais_mise_en_location) / prix_voiture) * 100

        resultat_label.config(text=f"Rentabilité : {rentabilite:.2f}%")
    except ValueError:
        resultat_label.config(text="Veuillez entrer des valeurs numériques valides.")

fenetre = tk.Tk()
fenetre.title("Calculatrice de rentabilité pour véhicule de location")

tk.Label(fenetre, text="Chiffre d'affaires annuel brut (€):").grid(row=0, column=0, sticky="w")
entree_ca_annuel = tk.Entry(fenetre)
entree_ca_annuel.grid(row=0, column=1)

tk.Label(fenetre, text="Frais de mise en location (€):").grid(row=1, column=0, sticky="w")
entree_frais = tk.Entry(fenetre)
entree_frais.grid(row=1, column=1)

tk.Label(fenetre, text="Prix de la voiture (€):").grid(row=2, column=0, sticky="w")
entree_prix_voiture = tk.Entry(fenetre)
entree_prix_voiture.grid(row=2, column=1)

calculer_btn = tk.Button(fenetre, text="Calculer", command=calculer_rentabilite)
calculer_btn.grid(row=3, column=0, columnspan=2)

resultat_label = tk.Label(fenetre, text="")
resultat_label.grid(row=4, column=0, columnspan=2)

fenetre.mainloop()
