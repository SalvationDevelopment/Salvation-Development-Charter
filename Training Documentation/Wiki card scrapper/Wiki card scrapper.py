# Storm Wolf (Jeff Falberg)
# Wiki card scrapper for card names and descriptions

import urllib.request as urr
import urllib.error
from urllib.error import HTTPError
import sys
import re

sys.argv = ["Wiki card scrapper.py", "input.txt", "output.sql"]
input_file = sys.argv[1]
output_file = sys.argv[2]


database = open(input_file, "r")
query = open(output_file, "w", encoding='utf-8')
listoflines = database.readlines()
database.close()
listofdata = []

for line in listoflines :
    while(len(line)<9) :
        line = '0' + line
    wiki_url = "http://yugioh.wikia.com/wiki/" + line
    try:
        page = urr.urlopen(wiki_url)
        if page.getcode() == 200 :
            sourcepage = page.read()
            source = sourcepage.decode("utf-8")
            regexName = re.compile(r"data\">\n(.*)</td>")
            patternName = re.compile(regexName)
            card_name = re.findall(patternName, source)[0]
            card_name = re.sub('"', '""', card_name)
            card_name = re.sub("'", "''", card_name)
            regexText = re.compile(r";;\">\n(.*)")
            patternText = re.compile(regexText)
            card_text = re.findall(patternText, source)[0]
            card_text = re.sub('(?!<br>|</br>)(<.*?>)','', card_text)
            card_text = re.sub('"', '""', card_text)
            card_text = re.sub("'", "''", card_text)
            card_text = re.sub('<br>', '\n', card_text)
            card_text = re.sub('</br>', '\n', card_text)
            #print('Processing: '+line)
            print('update texts set name="'+card_name+'", desc="'+card_text+'" where id='+line+';')
            query.write('update texts set name="'+card_name+'", desc="'+card_text+'" where id='+line+';')
    except urllib.error.HTTPError as err :
        if err.code == 404 :
            continue
        else :
            raise
