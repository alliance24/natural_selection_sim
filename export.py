import openpyxl
import stats, os
# os.chdir("natural_selection_sim-main/")

def clear(): # Vide le fichier excel
    os.remove("simulations.xlsx")
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "simulations.xlsx"
    wb.save("simulations.xlsx")

def create_sheet():
    workbook = openpyxl.load_workbook("simulations.xlsx")
    workbook.create_sheet(title='Simulation')
    workbook.save("simulations.xlsx")

def load_and_write():
    workbook = openpyxl.load_workbook("simulations.xlsx")
    name_page = workbook.sheetnames[-1] # On récupère le nom de la dernière feuille
    ws = workbook[name_page] # On se place dans la feuille en question
    ws.append(["Génération", "Nombre d'individus départ", "Nombre d'individus en vie", "Nombre de naissances", "Nombre de morts", "Moyenne taille individus", "Moyenne vue individus", "Moyenne vitesse individus", "Nombre de morts total", ])
    workbook.save("simulations.xlsx")

def export():
    workbook = openpyxl.load_workbook("simulations.xlsx")
    name_page = workbook.sheetnames[-1] # On récupère le nom de la dernière feuille
    ws = workbook[name_page] # On se place dans la feuille en question
    ws.append([stats.generation, stats.nb_individus_start, stats.nb_individus_alive, stats.births, stats.nb_individus_dead, stats.individus_moyenne_size, stats.individus_moyenne_view, stats.individus_moyenne_speed, stats.nb_individus_dead_total])
    # print([stats.generation, stats.nb_individus_start, stats.nb_individus_alive, stats.births, stats.nb_individus_dead, stats.individus_moyenne_size, stats.individus_moyenne_view, stats.individus_moyenne_speed, stats.nb_individus_dead_total])
    workbook.save("simulations.xlsx")

