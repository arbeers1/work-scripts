import csv
import os
from aim import Aim
from selenium.common.exceptions import NoSuchElementException

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

nav.click(Aim._text, "Purchasing")
nav.click(Aim._text, "Purchase Order")
nav.click(Aim._id, "mainForm:buttonPanel:search")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code_SQLOperator", "IN")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code__dataSort", "A")

nav.driver.execute_script('document.getElementById("mainForm:ae_i_poe_e_po_code").value = arguments[0];', po_codes)
#navdriver.find_element_by_id("mainForm:ae_i_poe_e_po_code").send_keys(po_codes) <-This is equiv to line above, but much slower
nav.click(Aim._id, "mainForm:buttonPanel:executeSearch")

cost = []
for x in range(len(list)):
    try:
        nav.click(Aim._text, str(list[x]))
    except NoSuchElementException:
        nav.click(Aim._id, "mainForm:next")
        nav.click(Aim._text, str(list[x]))
    cost.append(nav.text(Aim._id, "mainForm:PO_VIEW_content:totText"))
    nav.click(Aim._id, "mainForm:buttonPanel:bapButton")
    print(str(x) + " " + list[x] + " " + cost[x])

with open('result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter =',')
    for x in range(len(list)):
        spamwriter.writerow([list[x], cost[x]])
