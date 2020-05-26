# Rappresentazione Grafica di un Segnale Sinusoidale
Rappresentazione Grafica Di Un Segnale Sinusoidale Con Python 3 E La Fantastica Libreria Matplotlib

Ricordando che un segnale sinusoidale può essere descritto da equazioni del tipo: y(t) = V_max * sin(ω*t + φ), dove: V_max è l'ampiezza o il valore massimo del segnale, ω è la pulsazione che si calcola ω = 2*π*f, dove f è la frequenza che indica il numero di volte in cui il periodo si ripete in 1 secondo, t è la variabile indipendente e φ è la fase del segnale.

Nello script si importano le librerie matplotlib e numpy che saranno utili rispettivamente per la rappresentazione del grafico della funzione e per l'uso di funzioni o costanti come sin(x), pi (π), ect...
Inoltre si usa anche la libreria math che attraverso la funzione radians(), converte la fase da gradi a radianti.

Inizialmente si chiede l'inserimento del Valore Massimo o dell'Ampiezza del segnale sinusoidale il cui valore viene memorizzato all'interno della variabile V_max.
Subito dopo viene richesto l'inserimento dello sfasamento del segnale espresso in gradi e, se il segnale non avesse sfasamento, cioè φ = 0, basterà dunque digitare il valore 0 (zero) o lasciare il campo vuoto e premere INVIO.

Successivamente considero un periodo T a mia scelta, ad esempio 4 secondi e sapendo che f = 1/T => f = 0.25 Hz [Hertz] (frequenza). Usando la funzione arange() della libreria numpy si può creare un array o vettore il quale conterrà i valori da 0.0 a 10.0 incrementati ogni volta di 0.01 e questi valori rappresenteranno i valori istantanei della variabile indipendente t.
Come da definizione la pulsazione ω sarà ω=2*π*f dove la frequenza f è stata calcolata precedentemente, mentre la fase φ sarà opportunamente convertita da gradi a radianti.
Infine si scrive l'equazione della sinusoide che avrà il seguente aspetto: y = V_max * sin(ω*t). La fase φ non è presente e questo perchè se si considera il valore T/4 = π/2 e T/2 = π (quindi π/2 = 1 e π = 2), allora la retta di equazione parallela all'asse delle ordinate (y) sarà data dalla proporzione:
π/2 : 1 = φ : x cioè x = φ/(π/2)
che indicherà il punto esatto dello sfasamento e quindi da dove parte il segnale sinusoidale.
Tutto il resto è solo parte "decorativa" di matplotlib!

Created By Antonio Bernardini Copyright© 2020
