# Storm Wolf (Jeff Falberg)
# Wiki card scrapper for card names and descriptions

import urllib.request as urr
import urllib.error
from urllib.error import HTTPError
import sys
import re

sys.argv = ["ID conversion.py", "input.txt", "output.sql"]
input_file = sys.argv[1]
output_file = sys.argv[2]


database = open(input_file, "r")
query = open(output_file, "w", encoding='utf-8')
listoflines = database.readlines()
database.close()
listofdata = []
prescript = {'VJMP-JP': 200,
             'WJMP-JP': 203,
             'SJMP-JP': 204,
             '20AP-JP': 213,
             'PP19-JP': 214,
             'SD31-JP': 331,
             'MACR-JP': 912}

for line in listoflines :
    old_line = line
    while(len(line)<9) :
        line = '0' + line
    if len(line)>9 :
        pack = int(line[3:6])
        number = line[6:9]
        pack = list(prescript.keys())[list(prescript.values()).index(pack)]
        line = str(pack) + number
    wiki_url = "http://yugioh.wikia.com/wiki/" + line
    try:
        page = urr.urlopen(wiki_url)
        if page.getcode() == 200 :
            sourcepage = page.read()
            source = sourcepage.decode("utf-8")
            if len(old_line)>9 :
                regexID = re.compile(r"(\d\d\d\d\d\d\d\d)<\/a><\/td><\/tr>")
                patternID = re.compile(regexID)
                try :
                    change_id = re.findall(patternID, source)[0]
                    print(old_line,': ',change_id)
                    query.write("update datas set id="+change_id+" where id="+old_line+";"+"update texts set id="+change_id+" where id="+old_line+";")
                except IndexError :
                    #pass
                    print(old_line,' failed')
                continue
            #query.write('update texts set name="'+card_name+'", desc="'+card_text+'" where id='+old_line+';')
    except urllib.error.HTTPError as err :
        if err.code == 404 :
            continue
        else :
            raise
