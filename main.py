# Import pandas plugin
import pandas as pd
pd.set_option('display.max_rows', None)


# Type the exact file name of the database to be analyzed
database_file_name = 'file.csv'

# Reading the database
fin = open(database_file_name, 'r')

countryList = []
denominationList = []
denominationInt = []

for line in fin:
    line = line.strip()
    lineParts = line.split(",")
    country = lineParts[1]
    denomination = lineParts[2]
    if denomination.isdigit():
        denominationInt = int(denomination)
    countryList.append(country)
    denominationList.append(denominationInt)

# Removing the header row
del countryList[0]
del denominationList[0]

# Setting the data we want to analyze
d = {'Country': countryList, 'Denomination': denominationList}

# Creating the data frame
df = pd.DataFrame(d, columns=['Country', 'Denomination'])
df["RankedValue"] = df.groupby("Country")["Denomination"].rank(ascending=1, method='dense')

# Exporting the data
print(df)
csv_data = df.to_csv()
fout = open('export.csv', 'w')
print(csv_data, file=fout)

# Closing files
fin.close()
fout.close()
