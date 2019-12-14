#THIS CLASS PROCESSES THE DATA
filepath = '/home/aray/Masaüstü/AOL.txt.sorted'
filepath2 = '/home/aray/Masaüstü/AOLyen.txt' #OUT FILE
with open(filepath, "r+") as fp, open(filepath2, "w") as outfile:
    #line = fp.readline()

    arda = "https://"

    #line.strip()

    for line in fp.readlines():
        aa =(line.strip().split("\t"))
        if (aa[1]== "-"):
           continue

        elif arda or arda.upper() in line:
            outfile.write("\t".join(line.split("\t")[0:len(line.split("\t")) - 2:]).upper() + "\n")

        else:
          outfile.write(line.upper() + "\n")

