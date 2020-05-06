import csv
csv_file= open("data/tweet_id.csv, newline=''")
read_csv = csv.reader(csv_file, delimiter=",")

>>> with open('eggs.csv', newline='') as csvfile:
    ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
    ...         print(', '.join(row))
count=0
file1=open("data/tweet_id.txt","a")
day="2020-01-01"