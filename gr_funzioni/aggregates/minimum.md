# minimum

Restituisce il valore minimo aggregato da un campo o espressione.

## Sintassi

minimum(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)

## Argomenti

* _<span style="color:red;">expression</span>_ sotto espressione o campo da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato

## Esempi

* ` minimum("j_tot_femmine", "COD_REG")  → valore minimo di "j_tot_femmine", raggruppato per il campo "COD_REG"`

![](/img/aggregates/minimum/minimum1.png)

## nota bene

La sintassi prevede due possibilità:
1. quella classica, senza l'uso dei paramentri denominati (l'ordine è fondamentale);
    1. minimum(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)
2. con i parametri denominati (l'ordine non è più fondamentale): 
    1. minimum(_<span style="color:red;">filter:=</span> ,<span style="color:red;">expression:=</span> ,<span style="color:red;">group_by:=</span>_)


## esempio:

Selezionare le Province con minor area per ogni Regione

`$area = minimum(expression:=$area,group_by:="COD_REG")`

![](/img/aggregates/minimum/minimum2.png)
--
