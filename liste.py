import csv
with open('teilnehmer.csv') as csvdatei:
    csv_reader_object = csv.reader(csvdatei)

    zeilennummer = 0
    for row in csv_reader_object:

        if zeilennummer == 0:
            print(f'Spaltennamen sind: {", ".join(row)}')
        else:
            print(f'{row[0]} ist {row[1]} Jahre, {row[2]} und von Beruf: {row[3]}.')
        zeilennummer += 1

    print(f'Anzahl Datensätze: {zeilennummer-1}')