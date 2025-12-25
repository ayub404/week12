store_a = """Laptop,5,999.99
Mouse,20,25.00
Keyboard,15,75.00
Monitor,8,300.00"""

store_b = """Laptop,3,999.99
Mouse,35,25.00
Headphones,12,150.00
Keyboard,10,75.00"""

store_c = """Mouse,25,25.00
Monitor,5,300.00
Headphones,8,150.00
Laptop,7,999.99"""

with open("store_a.csv", "w") as f:
    f.write(store_a)

with open("store_b.csv", "w") as f:
    f.write(store_b)

with open("store_c.csv", "w") as f:
    f.write(store_c)    

result = {}
with open("store_a.csv", "r") as f1, open("store_b.csv", "r") as f2, open("store_c.csv", "r") as f3:
    store_a = 0
    store_b = 0
    store_c = 0
    for data in f1:
        
        data = data.strip()
        parts = data.split(',')
        product, u_sold, p_price = parts

        u_sold = int(u_sold)
        p_price = float(p_price)

        store_a = store_a + u_sold

        if product in result:
            result[product]['units_sold'] += u_sold
        else:
            result[product]  = {
                'units_sold': u_sold,
                'price': p_price
            }

    for data in f2:
        data = data.strip()
        parts = data.split(',')
        
        product, u_sold, p_price = parts
        u_sold = int(u_sold)
        p_price = float(p_price)

        store_b = store_b + u_sold

        if product in result:
            result[product]['units_sold'] += u_sold
        else:
            result[product]  = {
                'units_sold': u_sold,
                'price': p_price
            }

    for data in f3:
        data = data.strip()
        parts = data.split(',')
        
        product, u_sold, p_price = parts
        u_sold = int(u_sold)
        p_price = float(p_price)

        store_c = store_c + u_sold


        if product in result:
            result[product]['units_sold'] += u_sold
        else:
            result[product]  = {
                'units_sold': u_sold,
                'price': p_price
            }


if max(store_a, store_b, store_c) == store_a:
    top_store = 'Store A'
elif max(store_a, store_b, store_c) == store_b:
    top_store = 'Store B'
else:
    top_store = 'Store C'

with open("regional_report.txt", 'w') as af:
    final_total = 0
    af.write('=' * 50 + '\n')
    af.write('       REGIONAL SALES CONSOLIDATION         \n')
    af.write('=' * 50 + '\n')
    af.write(f'{"Product":<12}    {"Units Sold":>8}       {"Total Revenue":>8}\n')
    af.write('-' * 50 + '\n')
    for item in result:
        units = result[item]['units_sold']
        subtotal = units * result[item]['price']
        af.write(f"{item:<19}{units:<17}${subtotal:<45.2f}\n")
        final_total += subtotal

    af.write('-' * 50 + '\n')
    af.write(f"{'GRAND TOTAL REVENUE:':<20} ${final_total:<30.2f}\n")
    af.write(f"TOP SELLING STORE: {top_store} ({max(store_a, store_b, store_c)} units sold)\n")
    af.write('=' * 50 )

with open("regional_report.txt", "r") as f:
    print(f.read())







