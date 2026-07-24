# Ce code est destiné à être exécuté avec Python 2

def python2_only_function():
    print "Ceci est une fonction Python 2 !"
    
    # Exemple de xrange (Python 2)
    print "Nombres de 0 à 4 avec xrange (Python 2):"
    for i in xrange(5):
        print i,
    print "\n"
    
    # Exemple de division entière (Python 2)
    a = 5
    b = 2
    resultat_division = a / b
    print "5 / 2 en Python 2 (division entière) :", resultat_division
    
    # Classe de style "old-style" (implicite en Python 2)
    class MyClass:
        def __init__(self, value):
            self.value = value
        def show_value(self):
            print "La valeur est :", self.value
            
    obj = MyClass(10)
    obj.show_value()

python2_only_function()
