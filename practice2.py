log_data = """[INFO] System started successfully
[WARNING] Memory usage high
[ERROR] Database connection failed
[INFO] User logged in
[ERROR] Payment gateway timeout
[INFO] Scheduled backup complete
[ERROR] Disk space critical"""

with open("server_log.txt", "w") as f:
    f.write(log_data)
errors = 0
with open("server_log.txt", 'r') as finder,  open("urgent_alerts.txt", 'w') as urgent:
    for line in finder:
        if 'ERROR' in line:
            errors += 1
            urgent.write(line)
    print(f"Scan complete. Found {errors} errors.")
    print("Please check urgent_alerts.txt")
with open("urgent_alerts.txt", 'r') as f:
    print('-' * 40)
    print(f.read()) 