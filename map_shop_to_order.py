import csv

result = []
with open('work_orders.csv', newline='') as work_orders:
    order_reader = csv.reader(work_orders, delimiter=",")
    for i in order_reader:
        with open('shops.csv', newline='') as shops:
            shop_reader = csv.reader(shops, delimiter=",")
            work_order = (i[1][i[1].index("'"):i[1].index(",")]).replace("'", "")
            phase = i[1][i[1].index(",") + 3:i[1].index("]") - 1]
            if(work_order == '' and phase == ''):
                result.append([i[0], ''])
            else:
                flag = True
                for j in shop_reader:
                    if(str(work_order) == str(j[0]) and str(phase) == str(j[1])):
                        flag = False
                        result.append([i[0], j[2]])
                        break
                if(flag):
                    result.append([i[0], ''])
with open('final.csv', 'w', newline="") as final:
    writer = csv.writer(final, delimiter=",")
    for x in range(len(result)):
        writer.writerow([result[x][0], result[x][1]])
