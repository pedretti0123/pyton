tupla_performance = (
    ("Mario Rossi", 12.5, 95, "2023-10-01"),
    ("Luca Bianchi", 11.8, 97, "2023-10-01"),
    ("Gianna Neri", 13.1, 90, "2023-10-02"),
    ("Sofia Verdi", 12.2, 96, "2023-10-02"),
    ("Carlo Marroni", 14.0, 88, "2023-10-03"),
    ("Paola Lilla", 11.9, 98, "2023-10-03"),
)

def totale_punti(tupla_performance):
    tot=0
    somma=0
    for nome,tempo,punteggio,giorno in tupla_performance:
        tot= tot+punteggio
    return tot
def media_tempo(tupla_performance):
    media=0
    somma=0
    for nome,tempo,punteggio,giorno in tupla_performance:
        media=(somma+tempo)/len(tupla_performance)
    return media


def miglior_punteggio(tupla_performance3):
    max=0
    for tupla in tupla_performance:
        if(tupla[2]>max):
            max=tupla[2]
    for i in tupla_performance:
        if(max==i[2]):
            return i
while True:
    print(f"1. guarda il totale dei punti")
    print(f"2. vedi la media del tempo")
    print(f"3.vedi la tupla con il miglior punteggio")
    print(f"4. ESCI")
    n=int(input())
    if(n==1):
        tot=totale_punti(tupla_performance)
        print(f"il totale dei punti di tutti i giocatori è {tot}")
    elif(n==2):
        media=media_tempo(tupla_performance)
        print(f"la media dei tempi registrati è {round(media)}")
    elif(n==3):
        print(miglior_punteggio(tupla_performance))
    else:
        break