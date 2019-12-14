#THIS IS THE CLASS THAT CREATES A LEXICON AFTER PROCESSING THE DATA
#I USED REGEX TO FIND AALL THE WORDS, WORDS WITH NUMBERS OR JUST NUMBERS
#BY THIS WAY, I DO NOT NEED TO CONCERN ABOUT PUNCTUATION MARKS
import re
from collections import Counter
from collections import OrderedDict
filepath = '/home/aray/Masaüstü/Information Retrieval/Project2' #PATH OF PROCESSED DATA FILE
filepath2 = '/home/aray/Masaüstü/AOL2.txt' # PATH OF LEXICON FILE
with open(filepath,"r") as fhand, open(filepath2,"w") as fout:
    count = {}
    for line in fhand.readlines():
        #userId = line.split()[:1]
        newline = " ".join(line.strip().split("\t")[1:-1])
        #print(newline)
        wor = re.findall("([A-Z0-9]+)",newline)
        #print(wor)
        words = line.split()[1:-2]

        for var in OrderedDict.fromkeys(wor):
            if var in count:
                count[var][0]+= wor.count(var)
                count[var][1]+=1
            else:
                count[var] = [wor.count(var),1]

        #print(var + "\t"+str(count[var][1])+"\t"+ str(count[var][0])+"\n")
    for i in count:
        fout.write(i + "\t"+str(count[i][1])+"\t"+ str(count[i][0])+"\n")
        #print(int(datetime.datetime(int(year),int(month),int(day), int(hour), int(minute), int(seconds)).timestamp()))
