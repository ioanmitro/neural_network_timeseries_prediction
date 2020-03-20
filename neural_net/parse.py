import sys,re
import os.path
import multiprocessing as mp


def getData(filename):f

    if( os.path.exists('./'+filename)):

        # Crawl through the outputacm.txt and when i find a reference
        # we save the year of the paper that had the reference
        with open(filename) as fp:
            ## Get number of papers
            line=fp.readline().strip()
            numOfPapers=line
            indexNow=0
            indexArr=[]
            yearArr=[]
            finalYears=[]
            finalParsing=[]

            for i in range(0,int(numOfPapers)):
                finalYears.append([])
                yearArr.append(0)

            while line:
                title=''
                year=-1
                countRefs=0

                while line and line!='\n':
                    tmp=line
                    line=fp.readline().strip()

                    while line and line!='\n' and (not(line.startswith('#'))):
                        tmp += (' ' + line.strip())
                        line = fp.readline()

                    #Remove non-ASCII characters.
                    tmp = re.sub(r'[^\x00-\x7F]+', ' ', tmp)

                    if tmp.startswith('#t'):
                        year = int(tmp[2:])
                        yearArr[indexNow]=year
                    elif(tmp.startswith("#%")):
                        ref = int(tmp[2:].strip())
                        #Put the years of all references
                        finalYears[ref].append(year)
                        countRefs+=1
                if(countRefs >0 ):
                    #Get year,reference,index
                    indexArr.append(indexNow)

                if indexNow % 100000 == 0:
                    print 'Parsed', indexNow, 'papers'
                indexNow += 1
                line = fp.readline()

        # We get every paper that has citiations
        # dumping all the papers with zero references
        for i in range(0,len(finalYears)):
            if(len(finalYears[i])>0):

                #Count how many citiations
                tempCount=[]
                tempYear=[]
                totalCit=0
                for elem in finalYears[i]:
                    year=elem
                    count=0
                    if(year not in tempYear):
                        for el in finalYears[i]:
                            if(int(el)==int(year)):
                                totalCit+=1
                        tempYear.append(year)

                #Get the first 20 years
                tempCount=[]
                tempYear=[]
                yy=yearArr[i];
                for j in range(0,20):
                    tempCount.append(0)
                    tempYear.append(yy+j);

                whatElement=0
                for ye in tempYear:
                    for el in finalYears[i]:
                        if(int(ye)==int(el)):
                            tempCount[whatElement]+=1
                    whatElement+=1

                # We include to the file the papers that have
                # at least 6 references to other papers
                if(totalCit > 30):
                    finalParsing.append([[i],[tempYear],[tempCount]]);
        return finalParsing,finalYears
    else:
        print "Input file doesn't exists."

if __name__ == '__main__':

    if len(sys.argv)!=1:
        finalParsing,years=getData(sys.argv[1])

        with open('citationsPerPaper.txt', 'w') as f:
            for i in range(0,len(years)):
                if(len(years[i]) >0 ):
                    f.write("%d:%s\n" % (i,years[i]))
        with open('finalParsing.txt', 'w') as f:
            print "After filtering: %s" %len(finalParsing)
            for i in range(0,len(finalParsing)):
                for k in range(0,len(finalParsing[i][1])):
                    for kk in range(0,len(finalParsing[i][1][k])):
                        f.write(str(int(finalParsing[i][2][k][kk])))
                        if kk!=len(finalParsing[i][1][k])-1 :
                            f.write(",")
                    f.write("\n")
    else:
        print "Give the name of the input file."
        sys.exit()
