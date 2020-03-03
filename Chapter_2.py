# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:27:32 2020

@author: Alberto Viscardi
"""

type( "Hello, Wolrd!" )
# restituisce il tipo della variabile all'interno
# in questo caso una stringa

# una stringa la si può delimitare in vari modi
# ' Questa è una stringa '
# " Anche questa lo è "
# ''' Pure questa '''
# """ E financo questa 
# che ti permette di avere le cose
# su più righe """

# se si usano interi grandi è meglio usare
# la notazione large integer che si ottiene separando
# a gruppi di 3 le cifre con una virgola
# e.g. 
42000
42,000

len( 'hello' )
# la funzione 'len' misura la lunghezza di 
# qualsiasi cosa tu gli dia in ingresso

# le operazioni standard sono con i simboli standard
# mente le potenze si fanno con **,
# e.g. 2 ** 3 è due alla terza 
# mentre // è la parte intera inferiore del rapporto
# e.g. 6 // 4 = 1 ma -6 // 4 = -2
# il % da il resto della divisione intera, i.e.
# ( b * ( a // b ) ) + ( a % b ) = a per b non 0

# int porta qualsiasi cosa a intero,
# ma approssima sempre per difetto
# float fa lo stesso con i floating point
# str porta tutto a stringa

# WARNING le operazioni senza parentesi vengono svolte da destra!
# e.g. 2 ** 3 ** 2 è 2 alla ( 3 alla seconda )
# e non 8 alla seconda

