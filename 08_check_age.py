annee=int(input("Hello, en quelle année est tu né ? "))
age=float(2026-annee)
print(f"A la fin de lannée 2026, tu auras {age} ans !")
if age <12:
    print("Tu es un enfant")
elif (12<age<17):
    print("Tu es un adolescent")
else:
    print("Tu es un adulte")

