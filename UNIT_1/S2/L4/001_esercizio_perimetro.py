import math
print(f"Questo è un calcolattore di perimetro")
print(f"Scegli tra le seguenti opzioni")
print(f"1. Quadrato")
print(f"2. Rettangolo")
print(f"3. Cerchio")
print(f"4. Triangolo")


try:
    scelta = int(input("Inserisci la tua scelta: "))
except ValueError:
    print(f"Il valore inserito non è corretto. Riprova.")
    exit()

if scelta == 1:
    lato_quadrato = float(input(f"Inserisci la lunghezza del lato del quadrato"))
    perimetro = 4 * lato_quadrato
    print(f"Il perimetro del quadrato è {perimetro}")
        
elif scelta == 2:
    try:
        base_rettangolo = float(input(f"Inserisci la lunghezza della base del rettangolo: "))
        altezza_rettangolo = float(input(f"Inserisci l'altezza del rettangolo: "))
        perimetro = (base_rettangolo + altezza_rettangolo) * 2
        print(f"Il perimetro del rettangolo è {perimetro}.")
    except ValueError:
        print(f"Il valore inserito non è corretto. Riprova.")

elif scelta == 3:
        try:
            raggio_cerchio = float(input(f"Inserisci la lunghezza del raggio del cerchio: "))
            circonferenza = 2 * math.pi * raggio_cerchio
            print(f"La circonferenza del cerchio è di {circonferenza}")
        except ValueError:
            print(f"Il valore inserito non è corretto. Riprova.")

elif scelta == 4:
    try:
        lato_triangolo = float(input(f"Inserisci la base del triangolo: "))
        perimetro = lato_triangolo * 3
        print(f"Il perimetro del triangolo è di {perimetro}")
    except ValueError:
        print(f"Il valore inserito non è corretto. Riprova.")

else:
    print(f"Scelta non valida")