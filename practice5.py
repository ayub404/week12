data = """1001:Alice
1002:Bob
1003:Alice
ERROR_READING_LINE
1004: Charlie
1005:Alice
1006:Bob
1007:   
1008:David"""

with open("votes.txt", "w") as f:
    f.write(data)
count = 0
result = {}
with open("votes.txt", 'r') as f, open("results.txt", 'w') as new:

    new.write(f"OFFICIAL ELECTION RESULTS\n")
    new.write('-' * 40 + '\n')

    for line in f:
        line = line.strip()
        if ":" not in line:
            continue
        idd , name = line.split(':')
        name = name.strip()

        if not name:
            continue
        if name not in result:
            result[name] = 0
        result[name] += 1
        count += 1

        

    for name, votes in result.items():
        percentage = (votes / count) * 100
        new.write(f"{name}: {votes} votes ({percentage:.2f}%)\n")
with open("results.txt", 'r') as f:
    print(f.read())
    

        