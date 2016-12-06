# Storm Wolf (Jeff Falberg)
# Wiki card scrapper for card names and descriptions

import urllib.request as urr
import sys
import re

sys.argv = ["Wiki card scrapper.py", "input.txt", "output.sql"]
input_file = sys.argv[1]
output_file = sys.argv[2]


database = open(input_file, "r")
query = open(output_file, "w")
listoflines = database.readlines()
database.close()
listofdata = []

for line in listoflines :
    wiki_url = "http://yugioh.wikia.com/wiki/" + line
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
        card_text = re.sub('(<.*?>)','', card_text)
        card_text = re.sub('"', '""', card_text)
        card_text = re.sub("'", "''", card_text)
        print('update texts set name="'+card_name+'", desc="'+card_text+'" where id='+line+';')
