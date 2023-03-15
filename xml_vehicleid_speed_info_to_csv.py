import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('vehicles.xml')
root = tree.getroot()

# Open the CSV file for writing
with open('filename.csv', mode='w', newline='') as csv_file:
    # Create a writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['id', 'speed', 'unit'])

    # Loop through all the vehicles in the XML file
    for vehicle in root.findall('.//vehicle'):

        # Extract the vehicle information
        id = vehicle.attrib['id']

        # Extract the speed information
        speed = vehicle.find('speed').text
        unit = vehicle.find('speed').attrib['unit']

        # Write the data to the CSV file
        writer.writerow([id, make, model, speed, unit])
