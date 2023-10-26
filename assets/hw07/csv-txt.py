## Take CSV lyrics and move into txt file 
## no punctuation or weird characters 

import csv

lines = []
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

with open('csv/BillieEilish.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for row in spamreader:

        currLine = row[6]

        if currLine == "Lyric":
            next 
        else: 
            for ele in currLine:
                if ele in punc:
                    currLine = currLine.replace(ele, "")

            currLine = currLine + '\r'
            lines.append(currLine)

out = open("txt/billie.txt", "a")
for line in lines:
    out.write(line)
out.close()
        