# Import the built-in csv module
import csv

# Reads a CSV file and prints its content line by line.
def read_csv_file(file_path):
	with open(file_path, newline='') as csvfile:
		csvfile_content = csv.reader(csvfile, delimiter=',')
		for line in csvfile_content: 
			print(line)
			value1 = line[0]
			value2 = line[1]

# Call the read_csv_file function
read_csv_file("4.3_file.csv")
print("Done!")