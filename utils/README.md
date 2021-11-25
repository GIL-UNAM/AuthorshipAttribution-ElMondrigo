# Introduction to results

This is small sample of the results of the codes in the folder utils with a short explanation of whta the program does.

## Burrows
This code gives a measure of distance from each of the authors identifying a particular style.
```bash
----------------------------------------  BURROWS  ----------------------------------------
Emilio Uranga 1.4728091723219137
Blanco Moheno 1.1941812017297668
Jorge Joseph 0.5492348009363927
Ortega Molina 0.9953845299677827
Ortega Hernandez 1.1667106496153172
El Mondrigo 0.0Alberto Chimal 1.35641298376683
```

## Clustering
This code gives the calsification or grouping in order to identify two things, if the 5 authors actually belong to 5 different groups and if the disputed text falls within one og those 5 grouping.
```
----------------------------------------  CLUSTERING  ----------------------------------------
['Emilio Uranga', 'Blanco Moheno', 'Jorge Joseph', 'Ortega Molina', 'Ortega Hernandez', 'El Mondrigo', 'Alberto Chimal']
[3 2 1 4 5 1 0]
[5 1 3 3 4 0 2]
[1 4 0 2 5 0 3]

```

## Kilgariff
This code gives a distance between two texts and both are compared, the distance between them must be very small or small enough to reach the conclusion that both texts come from the same author.

```
----------------------------------------  KILGARIFF  ----------------------------------------
Emilio Uranga 1781.600260679751
Blanco Moheno 3232.8814937773295
Jorge Joseph 1637.5281663479861
Ortega Molina 2026.9544749326465
Ortega Hernandez 1999.9109841586644
El Mondrigo 0.0
Alberto Chimal 4102.962458475278
```

##  Mendenhall
This code gives us graphs that are stored in the `output_mendehall` folder where they show the average lenght of the words used by the author in his writings,that is, a distribution of the length of words throughout a text.  
For example, this graph.

![](../output_mendenhall/Blanco%20Moheno.png)

## Tagger
This code classifies the rerms of the text acoording to their grammatical function
```
----------------------------------------  TAGGER  ----------------------------------------
esta VERB
es NOUN
una DET
primera ADJ
oracion NOUN
de ADP
primavera NOUN
para SCONJ
destapar VERB
el DET
tubo NOUN
hay AUX
que CONJ
usar VERB
drano NOUN
la DET
fiesta NOUN
fue AUX
en ADP
el DET
zocalo NOUN
de ADP
la DET
ciudad NOUN
```

 # SVM_Chimal and SVM
 This code allows us to use the vector representation of classifyin that preserves most of the useful infromation that gives a binary classification that pairs with the elements of the set to obtain the best parameters.  
 SVM and SVM_Chimal get similar entries since one is attached to Alberto Chimal.  
 This data is saved in the `ouput_SVM` folder in a CSV file.
