print("Insère un nombre de secondes : ")

secondes_totales=str("insère un nombre de secondes : ")
heures = secondes_totales // 3600
reste = secondes_totales % 3600

minutes = reste // 60
secondes = reste % 60

print(f"{heures}heures{minutes}minutes{secondes}secondes")