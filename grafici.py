import matplotlib.pyplot as plt
import numpy as np

def Grafico_ExecutionTime_vs_RequiredPrecision(plot):
    iterazioni = list(plot.keys())
    tempo = list(plot.values())
    plt.plot(iterazioni,tempo)
    plt.xlabel("ITERAZIONI")
    plt.ylabel("TEMPO TRASCORSO (s)")
    plt.title("GRAFICO ITERAZIONI-TEMPO")
    plt.savefig("plot.jpg")
    plt.show()

