# money-counter

"""
Ben Blum
June 25, 2021
v1

This program ranks the denomination of banknotes by country grouping. 
The ranking ascends and treats duplicates ("ties") as equals.
The program reads data from a csv file of a simplified  database with a count, country, and denomination row

Example of how the csv file should be formatted:
Count,CountryName,Denomination,
0,Afghanistan,10,
1,Afghanistan,10,
2,Afghanistan,500,
...            ...
1694,Zimbabwe,100,
1695,Zimbabwe,500,
1696,Zimbabwe,500,

Place the csv file in the same folder this program is placed in; an export of the data will be put in the same folder
"""
