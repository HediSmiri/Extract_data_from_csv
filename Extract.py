import csv
import os 
import sys

os.system("mkdir extract_info")
csv_file = input("File Name*[.csv] : ")
extract_label = input("Label Extracted : ")
csv_data = []
extracted_label = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        csv_data.append(row)
    if extract_label in csv_data[0]:
        x = csv_data[0].index(extract_label)
        csv_data.remove(csv_data[0])
    else :
        input("Error Check Your Label Name Extracted ^_^\n Try again ..")
        sys.exit(0)
    for row in csv_data:
        extracted_label.append(row[x])
        
extention_type = input("Extenstion Type of Extracted Info : [txt\doc\csv\excel] : ")

print("done.\n Check Your Information in file named extracted")

f = open("extract_info\\"+extract_label+"."+extention_type,"a") 
for i in extracted_label:
    f.write(i+"\n")
f.close()
input("Press any Key To Exit ....")
