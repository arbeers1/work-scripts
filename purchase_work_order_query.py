import csv
import os
from aim import Aim
from selenium.common.exceptions import NoSuchElementException

def grab():
    nav.click(Aim._id, "mainForm:PO_VIEW_content:oldPoLineItemsList:0:link1")
    work_list = []
    work_list.append(nav.text(Aim._id, "mainForm:PO_LINE_ITEM_VIEW_content:oldPoDisburList:0:ae_i_poe_p_proposal"))
    work_list.append(str(nav.text(Aim._id, "mainForm:PO_LINE_ITEM_VIEW_content:oldPoDisburList:0:ae_i_poe_p_sort_code")))
    work_phase.append(work_list)
    nav.click(Aim._id, "mainForm:buttonPanel:done")
    nav.click(Aim._id, "mainForm:buttonPanel:bapButton")

#read input search paramaters
file = (os.path.dirname(os.path.abspath(__file__))) + "\cs.csv"
po_codes = ""
list = []
with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
       po_codes += row[1] 
       list.append(row[0])

nav = Aim()
nav.login()

#Navigate Assetworks
nav.click(Aim._text, "Purchasing")
nav.click(Aim._text, "Purhcase Order")
nav.click(Aim._id, "mainForm:buttonPanel:search")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code_SQLOperator", "IN")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code__dataSort", "A")

nav.driver.execute_script('document.getElementById("mainForm:ae_i_poe_e_po_code").value = arguments[0];', po_codes)
nav.click(Aim._id, "mainForm:buttonPanel:executeSearch")

work_phase = []
for x in range(len(list)):
    try:
        nav.click(Aim._text, str(list[x]))
    except NoSuchElementException:
        nav.click(Aim._id, "mainForm:next")
        nav.click(Aim._text, str(list[x]))
    try:
        grab()
    except NoSuchElementException:
        nav.driver.implicitly_wait(3)
        grab()
    print(str(x) + " " + list[x] + " " + work_phase[x][0] + " " + work_phase[x][1])

with open('work_orders.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter =',')
    for x in range(len(list)):
        spamwriter.writerow([list[x], work_phase[x]])


