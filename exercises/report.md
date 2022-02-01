# Report esercitazioni

## 1

### 1.1 - 1.2
In questo esercizio ho provato due calcoli di similarità differenti.
Il primo metodo consiste nel misurare la similarità come rapporto tra 
la cardinalità dell'intersezione tra tutte le definizioni e la lunghezza media delle definizioni.
é stato impossibile applicare questo metodo in quanto l'intersezione tra le definizioni è vuota.
Nel secondo metodo ho calcolato la  frequenza di  ogni parola utilizzata nelle definizioni
e ho calcolato la similarità com rapporto tra la somma delle frequenze associate ad ogni parola,
diviso la lunghezza della definizione.
In questo modo ho regolarizzato i punteggi, pesando la somma delle frequenze in base al numero di parole utilizzate.

I risultati osservati sono stati:

------ SIMILARITIES ------
courage 0.4879659863945578
paper 0.4765134099616857
apprehension 0.4038888888888889
sharpener 0.5873759920634921

------ AGGREGATIONS ------
abstract 0.4459274376417234
concrete 0.5319447010125888
generic 0.48223969817812173
specific 0.4956324404761905

Definire un concetto astratto o generico è meno vincolante rispetto a definire un concetto concreto o specifico.
Le definizioni dei concetti atratti e generici sono caratterizzate da una variabilità più alta di termini,
di conseguenza le frequenze associate ai termini sono più basse.
Al contrario, le definizioni dei concetti concreti e specifici sono caratterizzate da una variabilità più bassa
di termini, di conseguenza le frequenze associate ai termini sono più alte.
Per la misura di similarità che ho scelto quindi i punteggi dei concetti atratti e generici sono più bassi 
rispetto ai concetti concreti e specifici.


### 1.3
In questa esercitazione ho collegato due risorse, wordnet e property norms.
Dal file delle property norms sono state estratte due colonne, "concept" e "feature", le informazioni sono state 
organizzate secondo un dizionario contenente il concetto come chiave e una lista di feature come valore.
Le feature di wordnet sono state estratte andando a prendere aggettivi e nomi dalla descrizione del synset 
ricavato  attraverso l'algoritmo di Lesk.
Il programma mostra quindi il concetto estratto dalle property norms, associato alle feature trovate in wordnet e a 3 
possibili nuove feature prese dalle property norms.
Le feature da aggiungere sono state scelte prendendo le 3 feature più frequenti non presenti in wordnet.

CONCEPT:  flamingo
WORDNET FEATURES:  ['large', 'brackish', 'scarlet', 'bird', 'downbent', 'bill', 'lake']
PROPERTY NORMS FEATURES:  ['feather', 'animal', 'black'] 

CONCEPT:  stool
WORDNET FEATURES:  ['simple', 'back', 'seat', 'arm']
PROPERTY NORMS FEATURES:  ['tall', 'rectangular', 'top']

ONCEPT:  barrel
WORDNET FEATURES:  ['tube', 'bullet', 'travel', 'gun']
PROPERTY NORMS FEATURES:  ['liquid', 'flat', 'metal'] 


### 1.4
In questa esercitazione ho scelto come verbo transitivo "bless".
Abbiamo deciso di costruire il corpus attraverso la piattaforma Sketch engine utilizzando come parole chiave
"bless", "theology" e "religion". 
Così facendo ho ottenuto  un corpus di circa trentamila frasi.
Abbiamo estratto dal corpus tutte le frasi  in cui appariva la parola "bless" e la sua forma passiva "blessed" ottenendo 
così più di mille istanze da esaminare.

L'estrazione del soggetto e del complemento oggeto della frase è stata effettuata attraverso due funzioni.
La funzione di estrazione dell'oggetto prende in input la frase  tokenizzata, 
l'iterazione inizia dal verbo e procede all'indietro  esaminando i termini uno ad uno. 
la funzione seleziona il primo termine che soddisfa la regola di estrazione, ovvero una parola che non sia 
nè un verbo nè un avverbio.
La funzione di estrazione del complemento oggetto funziona in maniera identica, l'unica  differenza è che l'iterazione 
parte dal verbo e procede in avanti nella frase.


Subject              Object              
___________          ___________         
person               person              
cognition            communication       
communication        state               
state                act                 
quantity             group               
attribute            feeling             
plant                attribute           
group                artifact            
artifact             possession          
location             cognition           
act                  phenomenon          
event                relation            
relation             quantity            
Tops                 time                
feeling              plant               
time                 location            
substance            motive              
body                 event               
object               object              
possession           body                
animal               Tops                
shape                substance  

### 1.5
In questo esercizio ho deciso di considerare i 3 termini più frequenti incontrati nelle definizioni come iperonimi 
del  concetto da ricercare.
Abbiamo visitato tutti gli iponimi di questi termini e ho calcolato uno score, sono stati trattenuti quindi
i 5 iponimi con lo score più alto.
Lo score equivale al numero  di termini in comune tra l'insieme delle definizioni e la gloss dell'iponimo in questione.
A questo punto, per ogni concetto ho ottenuto 3 insiemi di iponimi, con un apposita funzione ho scelto 
l'inisieme di iponimi la cui somma degli score è più alta.


TARGET               FORMS               
___________          ____________________________________________________________________________________________________
courage              physical_ability.n.01 - penetration.n.04 - form.n.14 - magical_ability.n.01 - midas_touch.n.01
paper                composite_material.n.01 - paper.n.01 - packing_material.n.01 - aggregate.n.02 - bimetal.n.01
apprehension         apprehension.n.01 - panic.n.01 - creeps.n.02 - intimidation.n.03 - stage_fright.n.01
sharpener            drill.n.01 - jaws_of_life.n.01 - plow.n.01 - upset.n.04 - abrader.n.01


Come possiamo vedere, per "paper" e "apprehension" il task è riuscito, mentre per i concetti "courage" e "sharpener" no.
Abbiamo effettuato diverse prove variando  il numero di iperonimi.
Abbiamo notato che aumentando troppo quuesta quantità i risultati  peggiorano. 
Ciò è dovuto al fatto che la funzione considera termini meno frequenti e considera quindi iponimi più lontani
dai concetti target. 
Questi risultati ci mostrano come gli score degli iponimi legati alle parole
meno frequenti, non siano lontani dagli score degli iponimi legati a parole più frequenti.

## 2

### 2.1

In questa esercitazione ho cercato di implementare una algoritmo di segmentazione simile a quello riportato 
nell'articolo di Marti A Hearst. 

La funzione ha un parametro ovvero il numero di iterazioni da effettuare.
Nella prima iterazione i breakpoint vengono istanziati in maniera che siano quasi equidistanti tra di loro.

l'unità è la frase, quindi inizialmente avremo k segmenti con lo stesso numero di frasi per ognuno di loro.
le tokenizzazione in frasi è stata effettuata con le  funzioni  di libreria nltk. 

La funzione chiave è "find_breakpoints" che è quella che aggiorna i breakpoint esistenti.
la funzione prende in input il breakpoint odierno e a partire da quel punto effettua due ricerche, una in avanti e una 
all'indietro.
l'algoritmo verifica la sovrapposizione tra due frasi alla volta e appena trova  un punto con sovrapposizione zero 
restituisce il breakpoint. 
In questo modo abbiamo trovato un possibile punto in cui è avvenuto un possibile cambio di tema.
la funzione find breakpoint quindi troverà due brakpoint, uno risultate dalla ricerca in avanti e uno risultante dalla 
ricerca all'indietro. A questo punto verrà selezionato il breakpoint più vicino.
Se non vengono trovati punti con sovrapposizione zero, il breakpoint non viene aggiornato.

Una volta trovati i nuovi breakpoint si procede al calcolo della coesione intra-gruppo.
Per fare ciò ho creato dei vettori per ogni frase all'interno del segmento e il punteggio è stato ottenuto
attraverso il prodotto interno di quest'ultimi.
Il punteggio del singolo segmento equivale alla somma delle componenti del vettore ottenuto dal prodotto interno. 

Questo punteggio ci è servito a valutare la qualità della segmentazione.
L'algoritmo effettua n iterazioni e quindi n possinili  segmentazioni.
Ad ogni segmentazione è associato uno score che è la somma dei punteggi intra-gruppo.

A questo punto verrà selezionata la segmentazione con lo score maggiore.

L'algoritmo è stato testato ssu 5 articoli diversi, di seguito vediamo un possibile output:


[15, 29, 39, 49, 59, 59, 79, 83, 104, 112, 120] 3.0642361111111107
[23, 29, 39, 52, 70, 78, 91, 103, 103, 122] 4.053398058252427
[26, 29, 39, 49, 63, 79, 89, 106, 123] 3.6234042553191492
[25, 29, 39, 58, 70, 76, 100, 108, 124] 2.6103896103896105
[26, 29, 39, 55, 63, 93, 111, 126] 2.030578512396694
[25, 29, 39, 50, 53, 94, 100, 111, 124] 1.674964438122333
[26, 29, 39, 43, 47, 83, 85, 98, 107, 122] 2.5419440745672435
[25, 29, 34, 36, 47, 72, 76, 90, 106, 123] 3.6419213973799125
[26, 29, 29, 37, 65, 69, 99, 107, 123] 2.1214351425942963
[25, 26, 28, 60, 95, 112, 128] 2.0869242199108466

Best segments:  [23, 29, 39, 52, 70, 78, 91, 103, 103, 122] 4.053398058252427