import csv
s_log_path = "."
file_name = f"{s_log_path}/palo.log"

with open(file_name, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if 'TRAFFIC' in row:
            print(row)
