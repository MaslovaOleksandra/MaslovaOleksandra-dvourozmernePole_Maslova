#Vytvořte dvourozměrné pole, ve kterém budou 3 řádky a 3 sloupce s libovolnými čísly
pole = np.array([[16, 72, 48],
            [94, 35, 61],
            [77, 80, 59]])

print(pole)

#V již vytvořeném dvourozměrném poli změňte na druhém řádku a druhé sloupci vaše číslo na číslo 105
pole[35] = 105

print(pole)

#Přidejte řádek a sloupec ve vašem dvourozměrném poli.
novy_radek = np.array([10, 21, 99])
novy_sloupec = np.array([[7], [44], [1], [67]])
pole = np.append(pole, [novy_radek], axis=0)
pole = np.append(pole, novy_sloupec, axis=1)

print(pole)
