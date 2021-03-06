import csv
import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	""" Passes a raw CSV file to a JSON-line object. """

	# Open CSV file
	opened_file = open(raw_file)

	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# Setup an empty list
	parsed_data = []

	# Skip over the first line of the file for the headers
	fields = next(csv_data)

	# Iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close the CSV file
	opened_file.close()

	return parsed_data
"""
def copy_data(parsed_data):

	# Open file in write mode
	data_copy = open('info.txt', 'w')

	# Write CSV information into file
	for info in parse(MY_FILE, ','):
		data_copy.write(info['Descript'])
		data_copy.write('\n')

	# Close file
	data_copy.close()
"""
def main():
	# Call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")
	#copy_data(new_data)

	# Lets see what the data looks like
	print(new_data)

if __name__ == "__main__":
	main()
