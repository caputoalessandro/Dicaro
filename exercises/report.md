# Report esercitazioni

## 1

### 1.1 - 1.2
In questo esercizio abbiamo provato due calcoli di similarità differenti.
Il primo metodo consiste nel misurare la similarità come rapporto tra 
la cardinalità dell'intersezione tra tutte le definizioni e la lunghezza media delle definizioni.
é stato impossibile applicare questo metodo in quanto l'intersezione tra le definizioni è vuota.
Nel secondo metodo abbiamo calcolato la  frequenza di  ogni parola utilizzata nelle definizioni
e abbiamo calcolato la similarità com rapporto tra la somma delle frequenze associate ad ogni parola,
diviso la lunghezza della definizione.
In questo modo abbiamo regolarizzato i punteggi, pesando la somma delle frequenze in base al numero di parole utilizzate.

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
Per la misura di similarità che abbiamo scelto quindi i punteggi dei concetti atratti e generici sono più bassi 
rispetto ai concetti concreti e specifici.


### 1.3
In questa esercitazione abbiamo collegato collegato due risorse, wordnet e property norms.
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
In questa esercitazione abbiamo scelto come verbo transitivo "bless".
Abbiamo deciso di costruire il corpus attraverso la piattaforma Sketch engine utilizzando come parole chiave
"bless", "theology" e "religion". 
Così facendo abbiamo ottenuto  un corpus di circa trentamila frasi.
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