'''Fibonacci Sequence Calculator
Group members:
EVERYONE!!
'''

# Geen dubbele waarden
# aantal gegeven getallen = aantal_getallen
# geen waarde 0
# eerste waarde 0.5   

## functie: fibonnaci sequence of length x:

def fibonaccilijst(aantal_getallen):
    reeks = [0,1]
    
    while len(reeks) <= aantal_getallen:
        reeks.append(reeks[len(reeks)-2] + reeks[len(reeks)-1])  

    reeks[1] = 0.5
    reeks.remove(0)

    if aantal_getallen == 0:
        return []
    else:
        return reeks



assert len(fibonaccilijst(50)) == 50, 'Fout: aantal retour waarden klopt niet'
assert fibonaccilijst(0) == [], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(1) == [0.5], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(2) == [0.5, 1], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout: teruggegeven waarden kloppen niet'
print(fibonaccilijst(5))
