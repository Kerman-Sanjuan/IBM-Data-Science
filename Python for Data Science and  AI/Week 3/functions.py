#Some predefined functions
n = [1,2,3,4,5,6,1,3,5,6,3,21,4,5,1]
print(len(n))
print(sum(n))
ordenado = sorted(n)
print(ordenado)
#Example of no-defined function
def suma(a):
    return a+1

print(suma(4)) 
#You can add some documentation under a function to specify its use.
def resta(b):
    """[summary]

    Args:Tienes que meter cosas
        b ([int]): [Metele un numero]
    """    
    return b-1
