data = """Apples,50,100
Bananas,120,100
Cherries,5,20
Dates,50,50
Eggs,10,24"""

with open("inventory.csv", "w") as f:
    f.write(data)
with open('inventory.csv', 'r') as f, open("reorder_list.txt", 'w') as new:
    for line in f:
        line = line.strip()
        item, amount, need = line.split(',')
        amount, need = int(amount), int(need)
        if amount < need:
            new.write(f"Item: {item} | Order Amount: {need - amount} \n")
with open("reorder_list.txt", 'r') as new:
    
    print(new.read())
