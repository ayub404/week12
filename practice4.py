data = """  john smith - 1990
SARAH CONNOR - 1984
  kylo REN - 1995
LARA croft - 1992"""

with open("raw_users.txt", "w") as f:
    f.write(data)
with open("raw_users.txt", 'r') as f, open("clean_profiles.txt", 'w') as new:
    for line in f:
        line = line.strip()
        name, birth_year = line.split('-')
        birth_year = int(birth_year)
        new.write(f"Name: {name.title()} (Age: {2025 - birth_year})\n")
with open("clean_profiles.txt", 'r') as f:
    print(f.read())
