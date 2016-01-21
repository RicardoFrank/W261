#!/Users/Ricardo/AppData/Local/Dato/Dato Launcher/
import sys
import re
count = 0
#WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[2]
findword = sys.argv[1]

with open (filename, "r") as myfile:
    input_file = myfile.read()
    print re.findall(findword, input_file)
    #occurrences = re.findall(findword, input_file)
    #output = []
    #[output.append(x) for x in occurrences]
    #print output
    
    #print "woot"
    
    #split -b1k myfile chunk
    #for file in chunk*
    #do
        #grep -i findword $file | wc -l > $file.tmp &
    #done
    #wait
#Please insert your code