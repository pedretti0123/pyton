tupla_traffico_siti = (
    ("Google",
        ("gennaio", ("ricerca", 120000)),
        ("febbraio", ("ricerca", 115000)),
        ("marzo", ("ricerca", 130000)),
        # Altri mesi...
    ),
    ("Facebook",
        ("gennaio", ("social", 90000)),
        ("febbraio", ("social", 85000)),
        ("marzo", ("social", 95000)),
        # Altri mesi...
    ),
    ("Amazon",
        ("gennaio", ("e-commerce", 70000)),
        ("febbraio", ("e-commerce", 65000)),
        ("marzo", ("e-commerce", 75000)),
        # Altri mesi...
    ),
    # Altri siti...
)
somma=0.0

def media_visite():
    for nome,*dati in tupla_traffico_siti:
        if(nome_sito==nome):
            for mese,*informazioni in dati:
                for tipo,num in informazioni:
                    somma=somma+num
                    
    media=somma/3
    print(f" la media è {media}")
def max_visite(tupla_traffico_siti,nome_sito):
    max=0
    for nome,*dati in tupla_traffico_siti:
        if(nome_sito==nome):
            for i in dati:
                if(i[1][1]>max):
                    max=i[1][1]
    return max
nome_sito=str(input("inserisci il nome di un sito(Google,Facebook,Amazon)"))
media_visite()
max_visite()
    
        