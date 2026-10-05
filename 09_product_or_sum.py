n1=int(input("Insère un premier nombre entier :"))
n2=int(input("Insère un deuxième nombre entier :"))
produit=n1*n2
somme=n1+n2
if(n1*n2)<=1000:
    print(f"Le résultat de {n1}*{n2} est : {produit}")
else:
    print(f"Le résultat de {n1} + {n2} est : {somme}")
