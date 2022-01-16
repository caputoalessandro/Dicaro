# Report esercitazione 1 

## 1.1 

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