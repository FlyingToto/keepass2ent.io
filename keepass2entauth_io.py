#!/usr/bin/env python3
import sys, csv

# This script takes a file exported by keepass as a CSV file and extracts the TOTP secrets.

MYKEEPASSFILENAME = sys.argv[1]
if len(sys.argv) < 2:
    print("Usage: python keepass2entauh.py <keepass_file.csv>")
    sys.exit(1)
print("processing file: " + MYKEEPASSFILENAME)
# "Group","Title","Username","Password","URL","Notes","TOTP","Icon","Last Modified","Created"
with open('mytotp_to_import_into_ent', 'w', encoding='utf-8') as outfile:
    with open(MYKEEPASSFILENAME, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'TOTP' in row and row['TOTP'].strip():
                totp_secret = row['TOTP'].strip()
                outfile.write(totp_secret + '\n')
                print(totp_secret)
