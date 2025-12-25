data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

with open("expenses.txt", "w") as f:
    f.write(data)
total = 0.0
count = 0
with open("expenses.txt", "r") as f:

    for line in f:
        parts = line.strip().split(',')
        amount = float(parts[1])
        total += amount
        count += 1
    average = total / count

print("--- Expense Report ---")
print(f"Total Transactions: {count}")
print(f"Total Spent: ${total:.2f}")
print(f"Average Expense: ${average:.2f}")