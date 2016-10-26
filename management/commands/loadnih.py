from myproject.drugdb.models import *
import urllib
from xml.etree import ElementTree as ET

#Management command that adds information drug name and splcode to a database. 
#TODO: Adapt to work without django dependency

print "killing old records"
for obj in SplDrug.objects.all():
    obj.delete()
print "they dead"

#Main process to get records
url = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.xml"
root = ET.parse(urllib.urlopen(url)).getroot()
totalpages = int(root.findall('metadata')[0].find('total_pages').text)
pageno = 1

while pageno < totalpages:
    print "processing page " + str(pageno)
    root = ET.parse(urllib.urlopen(url)).getroot()
    labels = root.findall('spl') #Tag for each unique drug
    for item in labels:
        name = item.find('title').text
        code = item.find('setid').text 
        try:
            print "processing " + name
        except:
            continue
        SplDrug.objects.create(name=name, idcode=code)
        print "processed " + name
    pageno+=1
    url = root.findall('metadata')[0].find('next_page_url').text

print "ended at page " + str(pageno)


