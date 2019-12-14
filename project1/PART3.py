#THIS CLASS IS SIMILAR TO LEXICON CLASS, IT READS LEXICON FILE AND PROCESSED DATA FILE
#GET USER ID AND TIME, THEN CONVERT IT TO UNIX, DICTIONARY FILE HELPS ME TO GET THE TRIE

import datetime
import re
import pygtrie
filepath = '/home/aray/Masaüstü/AOLyen.txt'
filepath2 = '/home/aray/Masaüstü/AOL2.txt'
filepath3 = '/home/aray/Masaüstü/Trie.txt'
mytrie = pygtrie.StringTrie()
with open(filepath,"r") as fhand, open(filepath2,"r") as fhand2, open(filepath3,"w") as fout:
  #  readable = datetime.datetime.fromtimestamp(1552346949).isoformat()
    #mylist = []
    count = {}
    k=1
    for line in fhand2.readlines():
        l =line.strip().split("\t")
        mytrie[line[:line.index("\t")]] = k
        k+=1
    for line in fhand.readlines():
        userId = line.split("\t")[:1]
        kelimeler = " ".join(line.strip().split("\t")[1:-1])
        #print(newline)
        wor = re.findall("([A-Z0-9]+)",kelimeler)
        whole =""
        for w in wor:
            whole +=str(mytrie[w])+" "
        #print(wor)
        #words = line.split()[1:-2]
        #print(words)
        unix = line.split("\t")[2].split(" ")
        date = unix[0]
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]
        time = ("".join(unix[1]))
        hour = time.split(":")[0]
        minute = time.split(":")[1]
        seconds = time.split(":")[2]
        fout.write(''.join(userId[0])+"\t"+str(int(datetime.datetime(int(year),int(month),int(day), int(hour), int(minute), int(seconds)).timestamp()))+"\t"+whole +"\n")
        #print(wor)
        #print(var + "\t"+str(count[var][1])+"\t"+ str(count[var][0])+"\n")
    #for i in count:
        #fout.write(user + "\t"+str(count[i][1])+"\t"+ str(count[i][0])+"\n")
        #print(int(datetime.datetime(int(year),int(month),int(day), int(hour), int(minute), int(seconds)).timestamp()))
