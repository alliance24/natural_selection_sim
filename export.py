from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Simulation"


ws.append(["Mail", "Nom", "Prenom", "Date de naissance", "Mot de passe"])
wb.save("accounts.xlsx")
print("100 %")
print(f"Génération de comptes terminée...")

def export():
    return