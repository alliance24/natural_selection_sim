# # import openpyxl

# # data_frame = pd.read_excel('simulations.xlsx')

# import os, stats
# os.chdir("natural_selection_sim-main/")
# import pandas as pd

# workbook = pd.read_excel("simulations.xlsx")

# # Créer un DataFrame avec une ligne de données
# data = [{"Génération": stats.generation, "Nombre d'individus départ": stats.nb_individus_start, "Nombre d'individus en vie": stats.nb_individus_alive, "Nombre de naissances": stats.births, "Nombre de morts": stats.nb_individus_dead, "Moyenne taille individus": stats.individus_moyenne_size, "Moyenne vue individus": stats.individus_moyenne_view, "Moyenne vitesse individus": stats.individus_moyenne_speed, "Nombre de morts total": stats.nb_individus_dead_total}]
# data_frame_to_export = pd.DataFrame.from_records(data)
# data_frame_to_export.to_excel("simulations.xlsl")
import openpyxl, os, stats
os.chdir("natural_selection_sim-main/")

os.remove("simulations.xlsx")
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "simulations.xlsx"

ws.append([stats.generation, stats.nb_individus_start, 3])
wb.save("simulations.xlsx")