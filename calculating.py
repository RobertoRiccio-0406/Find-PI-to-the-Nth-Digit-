#this is just a simple test for calculating some ciphers of pi with different
#Python float got around 16 decimal precision
import math
import time
from tqdm import tqdm
from mpmath import sqrt,mp,mpf
import gmpy2




def Nilakantha(precision):
    n = precision * 10  # lo usiamo per Nilakantha che stima una cifra ogni 10 iterazioni
    gmpy2.get_context().precision = int(precision * 3.32)
    pi = gmpy2.mpfr(3)
    sign = gmpy2.mpfr(1)
    start_time = time.time()
    plot = {}
    for i in tqdm(range(2,n+1), colour='red'):
        term = gmpy2.mpfr(4) / (gmpy2.mpfr(2 * i) * gmpy2.mpfr(2 * i + 1) * gmpy2.mpfr(2 * i + 2))
        pi += sign * term
        sign *= gmpy2.mpfr(-1)
        if i % 100 == 0:
            plot[i] = time.time() - start_time

    if i % 100 == 0:
            plot[i] = time.time() -start_time
    return pi,plot


def Leibniz_Gregory(precision):
    n = precision * 10
    gmpy2.get_context().precision = int(precision * 3.32)
    pi = gmpy2.mpfr(0)
    sign = gmpy2.mpfr(1)
    start_time = time.time()
    plot = {}

    for i in tqdm(range(0, n), colour='yellow'):
        term = gmpy2.mpfr(4) / gmpy2.mpfr(2 * i + 1)
        pi += term * sign
        sign *= gmpy2.mpfr(-1)
        if i % 100 == 0:
            plot[i] = time.time() - start_time



def  Chudnovsky_binary_splitting(a,b):
    #caso base in cui k = a, livello più basso OVVERO (0,1)
    if b-a == 1:
        k=a #termine che stiamo calcolando e che vogliamo calcolare
        if k == 0:
            Pk = 1
            Qk = 1
        else: #termine k generico con k > 0
            Pk = -(6*k-5) * (6*k-3) * (6*k-1)
            Qk = (640320**3)*(k**3)
        Tk = Pk * (13591409 + 545140134 * k)

        return Pk,Qk,Tk

    #divido ora a, b a metà

    m = (a+b)//2 #divisione intera

    #effettuo le operazioni del ramo sinistro

    Psx, Qsx, Tsx = Chudnovsky_binary_splitting(a,m)

    #effettuo le operazioni del ramo destro

    Pdx, Qdx, Tdx = Chudnovsky_binary_splitting(m,b)

    #ora devo combinare man mano i risultati dei vari rami

    P = Psx * Pdx
    Q = Qsx * Qdx
    T = (Tsx * Qdx) + (Psx * Tdx)


    return P,Q,T



def Chudnovsky(n_digits):

    #sapendo che ogni termine della serie aggiunge circa 14.18 cifre decimale sappiamo che il numero di termini necessari per ottenere un voluto numero di digits = n_digits/14+2(+2 si aggiunge per sicurezza)
    n_terms = n_digits//14+2

    P,Q,T = Chudnovsky_binary_splitting(0,n_terms)

    '''
    una volta terminato l'albero del binary splitting possiamo finalmente effettuare l'ultima divisione
    '''
    mp.dps = n_digits +10 #dps sta per decimal places ed è la variabile di mpmath che controlla con quanta precisione float vengono fatti i calcoli
    pi = mpf(426880) * sqrt(mpf((10005))) * (Q/T)

    return pi



def Brent_Salamin(precision):
    gmpy2.get_context().precision = int(precision * 3.32) + 64 #altri 64 per sicurezza

    a = gmpy2.mpfr(1)
    b = gmpy2.mpfr(1) / gmpy2.sqrt(gmpy2.mpfr(2))
    t = gmpy2.mpfr("0.25")
    p = gmpy2.mpfr(1)
    n_iter = int(precision * 3.32/2).bit_length() #log2 iterazioni necessarie, bit lenght restituisce il numero di bit necessari a rappresentare un intero

    for i in tqdm(range(1, n_iter), colour="green"):
        a_next = (a + b) / gmpy2.mpfr(2)
        b = gmpy2.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        p *= gmpy2.mpfr(2)
        a = a_next

    pi = (a + b) ** 2 / (gmpy2.mpfr(4) * t)

    return pi
