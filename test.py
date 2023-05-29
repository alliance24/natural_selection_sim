import openpyxl
import stats, os
os.chdir("natural_selection_sim-main/")

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "test"
ws['A1'] = 1
ws.append(["hello"])
wb.save("simulations.xlsx")

