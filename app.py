import time
from os.path import split
from calculating import Nilakantha, Leibniz_Gregory, Chudnovsky, Brent_Salamin
from grafici import Grafico_ExecutionTime_vs_RequiredPrecision


print ("benvenuto nel miglior calcolatore di cifre decimali del Pi al mondo\n\n")

precision = int(input("quanti decimali vuoi calcolare\n\n"))


algoritmi_disponibili = {
    'a' : Nilakantha,
    'b' : Leibniz_Gregory,
    'c' : Chudnovsky,
    'd' : Brent_Salamin
}


scelta_algoritmo = input("Quale algoritmo preferisci usare ?\n1)Nilakantha -a\n2)Gregory-Leibnitz -b\n3)Chudnovsky con Binary splitting -c\n4)Brent Salamin -d\n\n")
if scelta_algoritmo.lower().strip() not in algoritmi_disponibili:
    raise Exception("valore scelto non corretto")

risultato = 0
funzione = algoritmi_disponibili[scelta_algoritmo]
if scelta_algoritmo == 'c':
    start_time = time.time()
    risultato = Chudnovsky(precision)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"il tuo pi è : {risultato}\n, il tempo impiegato è : {total_time}")

elif scelta_algoritmo == 'd':
    start_time = time.time()
    risultato = Brent_Salamin(precision)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"il tuo pi è : {risultato}\n, il tempo impiegato è : {total_time}")
else:
    start_time = time.time()
    risultato, plot = funzione(precision)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"il tuo pi è : {str(risultato)}\n, il tempo impiegato è : {total_time}")
    Grafico_ExecutionTime_vs_RequiredPrecision(plot)



scelta_file_txt = input("desideri un file .txt? s/n\n\n")


if scelta_file_txt == 's':
    risultato_str = str(risultato)
    with open("risultato.txt", "a") as file: #x indica che debba essere creato il file .txt , a invece scrive alla fine del file
        file.write(risultato_str)






