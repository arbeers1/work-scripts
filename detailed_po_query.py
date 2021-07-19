from aim import Aim
from selenium.common.exceptions import NoSuchElementException
import csv

print("Loading file")
list = []
insert_val = ""
with open ("4837.csv",  newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        list.append(row[0])
        insert_val += row[1]

print("Logging in")
nav = Aim()
nav.login()

nav.click(Aim._text, "Purchasing")
nav.click(Aim._text, "Purchase Order")
nav.click(Aim._id, "mainForm:buttonPanel:search")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code__dataSort", "A")
nav.select(Aim._id, "mainForm:ae_i_poe_e_po_code_SQLOperator", "IN")
nav.insert("mainForm:ae_i_poe_e_po_code", insert_val)
nav.click(Aim._id, "mainForm:buttonPanel:executeSearch")

final = []
for x in range(len(list)):
    try:
        if(x % 25 == 0 and x != 0):
            nav.click(Aim._id, "mainForm:next")
        else:
            nav.click(Aim._text, list[x])
            i = 0
            while(True):
                try:
                    current = []
                    current.append(list[x])
                    current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 1))
                    current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 2))
                    current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 3))
                    current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 5))
                    current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 7))
                    list.append(current)
                    print(str(x) + " " + current[0] + " " + current[1] + " " + current[2] + " " + current[3] + " " + current[4] + " " + current[5])
                    i = i + 1
                except IndexError:
                    break
            nav.click(Aim._id, "mainForm:buttonPanel:bapButton")
    except NoSuchElementException:
        nav.wait(3)
        nav.click(Aim._text, list[x])
        i = 0
        while(True):
            try:
                current = []
                current.append(list[x])
                current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 1))
                current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 2))
                current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 3))
                current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 5))
                current.append(nav.table("mainForm:PO_VIEW_content:oldPoLineItemsList", i, 7))
                list.append(current)
                print(str(x) + " " + current[0] + " " + current[1] + " " + current[2] + " " + current[3] + " " + current[4] + " " + current[5])
                i = i + 1
            except IndexError:
                break
        nav.click(Aim._id, "mainForm:buttonPanel:bapButton")

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter =',')
    for x in range(len(list)):
        writer.writerow(list[x])
    
