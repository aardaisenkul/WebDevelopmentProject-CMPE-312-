import re 
from datetime import datetime
q = True
objfilm = []

while(q):
    Input = input("Please enter file name(enter 'EXIT' for exit)")
    if(Input == "EXIT"):
        q = False
        break
    ini = Input.split(" ")
    if(ini[0] == 'INPUT'):
        print("Loading "+ini[1]+" ...")
        class Film:
          def __init__(self, name, p_Year,r_Date,genre,synopsis,director,stars):
            self.name = name
            self.p_Year = p_Year
            self.r_Date = r_Date
            self.genre=genre
            self.synopsis=synopsis
            self.director=director
            self.stars=stars
        def month_string_to_number(string):
            m = {
                 'jan': '2020-01',
                 'feb': '2020-02',
                 'mar': '2020-03',
                 'apr': '2019-04',
                 'may': '2019-05',
                 'jun': '2019-06',
                 'jul': '2019-07',
                 'aug': '2019-08',
                 'sep': '2019-09',
                 'oct': '2019-10',
                 'nov': '2019-11',
                 'dec': '2019-12'
                }
            s = string.strip()[:3].lower()
            try:
                out = m[s]
                return out
            except:
                raise ValueError('Not a month')



        with open(ini[1],"r",encoding="utf-8") as infile:
                wholetext = ""
                copy = False
                for line in infile:
                    
                    if line.strip():
                        
                        if line.strip() == "Next »":
                            copy = True
                        elif line.strip() == "if (typeof uet == 'function') {":
                           continue
                        elif line.strip() ==  "uet(\"bb\", \"SmallTrailerWidget\", {wb: 1});":
                           continue
                        elif line.strip() ==  "uet(\"be\", \"SmallTrailerWidget\", {wb: 1});":
                           continue
                        elif line.strip() ==  "uex(\"ld\", \"SmallTrailerWidget\", {wb: 1});":
                           continue
                        elif line.strip() ==  "Metascore":
                           continue
                        elif re.search("min$", line.strip()):
                           continue
                        elif re.search("^[0-9][0-9]$", line.strip()):
                           continue
                        elif line.strip() == "}":
                           continue
                        elif line.strip() == "-":
                           continue
                        elif line.strip() == "Watch Trailer":
                           continue
                        elif line.strip() == "if (typeof uex == 'function') {":
                           continue
                        elif line.strip() == "IMDb is your definitive source for discovering the latest new movies coming soon to theaters.":
                            break
                        elif copy:
                            wholetext += (line.strip()+"\n") 
        filmlist = []
        thislist = []
        for line in wholetext.splitlines():
            if(re.search("\(....\)$", line)):       
                thislist.append(line)


        keepCurrentSet = False
        lines = []
        lib = {}

        i = 0

        while(i<len(thislist)):
            infostext=""
            for line in wholetext.splitlines():
                if line.strip() == thislist[i]:
                    keepCurrentSet = True
                try:
                    if line.strip() == thislist[i+1]:
                        keepCurrentSet = False
                except IndexError:
                    if line == "\n":
                        keepCurrentSet = False
                if keepCurrentSet:
                    infostext+=line+"\n"
            lib[thislist[i]]= infostext
            i+=1

        genresslist =[]
        for l in lib:

            genre = re.findall("^(\w+)$|^(\w+\-\w+)$",lib[l],flags=re.MULTILINE)
            genress=""
            for g in genre:
                if g =='':
                    continue
                else:
                    genress += "".join(g).strip()+" "

            genresslist.append( genress )
        #print(genresslist)
        emptylist = []
        for x in range(len(thislist)):
            st = ""
            genreslist = list(filter(None,genresslist[x].strip().split(" ")))
           
            for y in genreslist:
                st += "".join(y)+" "
            emptylist.append(st)       
        #print(genresslist)
                   
            genresslist[x] = emptylist[x].strip().replace(" ",", ") 
        releasedate =[]
        for el in range(len(thislist)):
            bulunacak= ""    
            for line in wholetext.splitlines():
                if(re.search ("(^[A-Z][a-z]*\s\d{1,2})",line.strip())):
                    bulunacak = line
                elif(thislist[el] in line):
                    releasedate.append(bulunacak)
                    break
    

        for el in range(len(releasedate)):
            releasedate[el] = (month_string_to_number(releasedate[el].split(" ")[0])+'-'+str(releasedate[el].split(" ")[1]).zfill(2))



        
        for i in range(len(thislist)):
            filmlist.append(thislist[i].split("(")[0].strip())

        productionyearlist = []

        for i in range(len(thislist)):
            productionyearlist.append(thislist[i][-5:-1:])


        directorslist = []
        for x in range(len(thislist)):
            directos=""
            for line in lib[thislist[x]].splitlines():
                line = line.strip()
                if re.search("^Directors{0,1}:",line):
                        copy = False
                        for linecon in lib[thislist[x]].splitlines():
                            if(line == linecon):
                                copy = True
                            if("Stars:" in linecon):
                                break
                            elif copy:
                                if linecon not in ("Directors:","Director:"):
                                    directos+=linecon
            if('|' in directos):
                directorslist.append(", ".join(directos.split('|')))  
            else:
                directorslist.append(directos) 

        starslist = []
        for x in range(len(thislist)):
            starss=""
            for line in lib[thislist[x]].splitlines():
                line = line.strip()
                if re.search("^Stars{0,1}:",line):
                        copy = False 
                        for linecon in lib[thislist[x]].splitlines():
                            if(line == linecon):
                                copy = True
                            try:
                                if((thislist[x+1] in linecon) or (re.search ("(^[A-Z][a-z]*\s\d{1,2})",linecon))):
                                    copy = False
                                    break
                                elif copy:
                                    if linecon not in ("Stars:"):
                                        starss+=linecon
                            except IndexError:
                                if "\n" in linecon:
                                   copy = False
                                   break
                                elif copy:
                                    if linecon not in ("Stars:"):
                                        starss+=linecon
            starslist.append(starss)
 
        synopsiss= []
        #print(len(genresslist))
        #print((genresslist))
        #for x in range(len(thislist)):
        #    str_list = list(filter(None,genresslist[x].strip().split(" ")))
        #    print(str_list)
        for x in range(len(thislist)):
            genreslist = list(filter(None,genresslist[x].strip().split(" ")))
            ardaaa =(lib[thislist[x]].find(genreslist[-1])) +len((genreslist[-1]))
            #print(str_list)
            ayc =(lib[thislist[x]].find("Director"))
            #print(ardaaa)
            #print(ayc)
            synopsiss.append(lib[thislist[x]][ardaaa:ayc].strip())

             
        #print(filmlist)     
        #print (genresslist)
        #print(releasedate)         
        #print(productionyearlist)
        #print(directorslist)
        #print(starslist)
        #print(thislist)
        #print(synopsiss)

        
        f = 0
        #BURDA FILMLIST YAZIYORDU AMA HEPSİNİ BASTIRMAK İCİN THİSLİST YAPTIM THİSLİST YUKARDA
        for film in thislist:
             film = Film(filmlist[f],productionyearlist[f],releasedate[f],genresslist[f],synopsiss[f],directorslist[f],starslist[f])
             objfilm.append(film)
             f +=1
           
    elif(ini[0] == 'LIST'): 
        if(len(ini)==1):
            print("Listing...")
            for x in range(len(objfilm)):
                print(objfilm[x].name)
            
        elif(len(ini)==2):
            if(ini[1].split(":")[0]=="from"):
                print("Listing "+ini[1]+" ...")
                dat = ini[1].split(":")[1].split("-")
                dayy = dat[2]
                monn = dat[1]
                yee = dat[0]
                for x in range(len(objfilm)):
                    un = False
                    odat = objfilm[x].r_Date.split("-")
                    odayy = odat[2]
                    omonn = odat[1]
                    oyee = odat[0]
                    if( oyee>yee):
                      un = True
                    elif(oyee==yee):

                        if(omonn>monn):
                            un  = True
                        elif(omonn ==monn):
                            if(odayy>=dayy):
                                un = True
                    if(un):
                        print(objfilm[x].name)
            elif(ini[1].split(":")[0]=="genre"):
                genreff = [] 
                print("Listing " +ini[1]+" ...")
                gensearch =  ini[1].split(":")[1].split(',')
                for x in range(len(objfilm)):
                    un = True
                    for a in range(len(gensearch)):
                        if(gensearch[a] in objfilm[x].genre):
                            un = True
                        else:
                            un = False
                            break
                    if(un):
                      genreff.append(objfilm[x].name)
                print(*genreff, sep="\n")
        elif(len(ini)==3):
            print("Listing "+ini[1]+" "+ini[2]+" ...")
            fdat = ini[1].split(":")[1].split("-")
            fdayy = fdat[2]
            fmonn = fdat[1]
            fyee = fdat[0]
            tdat = ini[2].split(":")[1].split("-")
            tdayy = tdat[2]
            tmonn = tdat[1]
            tyee = tdat[0]
            for x in range(len(objfilm)):
                
                un = False
                odat = objfilm[x].r_Date.split("-")
                odayy = odat[2]
                omonn = odat[1]
                oyee = odat[0]
                if( oyee>fyee and tyee>oyee):
                      un = True
                elif(oyee==fyee and tyee==oyee):
                        if(omonn>fmonn):
                            if(tmonn>omonn):
                                un = True
                            elif(tmonn==omonn):
                                if(tdayy>odayy):
                                    un = True
                        elif(omonn ==fmonn):
                            if(odayy>=fdayy):
                                if(tmonn>omonn):
                                    un = True
                                elif(tmonn==omonn):
                                    if(tdayy>odayy):
                                        un = True
                        
                if(un):
                        print(objfilm[x].name)
    elif(ini[0] == 'INFO'):
        print("Info ...")
        fil = Input[5:]
        for x in range(len(objfilm)):
           if(fil in objfilm[x].name):
                print(objfilm[x].name)
                print("Production year: "+objfilm[x].p_Year)
                print("Release date: "+objfilm[x].r_Date)
                print("Genre: "+objfilm[x].genre)
                print("Synopsis: "+objfilm[x].synopsis)
                print("Director: "+objfilm[x].director)
                print("Stars: "+objfilm[x].stars)
