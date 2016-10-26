from django.shortcuts import *
from django.db.models import *
from drugdb.models import *
from django.template import Context, loader
from django.http import HttpRequest
import xml.etree.ElementTree as ET
import sys
import requests
from lxml import etree, objectify
import re
from bs4 import BeautifulSoup
import json

def Main(request):
    dictionaries = {}
    return render(request, 'main.html', dictionaries)

def Search(request):
    query = request.GET.get('q', '')
    exploded = query.split(" ")
    q_objects = Q()
    for term in exploded:
        q_objects &= Q(name__icontains=term)

    if query:
        qset = (
            q_objects
        )
        results = SplDrug.objects.filter(qset)
        
    else:
        results = []

    dictionaries = { 'results': results, 'query': query, }
    return render_to_response('search.html', dictionaries)

#def Drug(request, code):
#    address = {}
#    baseurl = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/'
#    f = urllib2.urlopen( baseurl+code+".xml" ).read()
#    xmlstring = str(re.sub('xmlns="urn:hl7-org:v3"', '', f))
#    tree = ET.ElementTree(ET.fromstring(xmlstring))
#    address_element = tree.getroot()
#    address = dict((e.tag, e.text) for e in address_element.getchildren())

#    t = loader.get_template('drug.html')
#    c = Context({'code': code, 'address': address })
#    return HttpResponse(t.render(c))    

def Drug(request, code):
    fdabaseurl = 'https://api.fda.gov/drug/label.json?search=set_id:'
    nihbaseurl = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/'
    suffix = '/media.xml'


    #result on openfda
    result = requests.get(fdabaseurl+code).json()
    r = result['results'][0]

    nihr = requests.get(nihbaseurl+code+suffix)
    soup = BeautifulSoup(nihr.text, "lxml")
    images = []
    for child in soup.media:
        images.append(child.url.text)


    dictionaries = { 'result': result, 'r': r, 'images': images, }
    return render_to_response('drug.html', dictionaries)

    #baseurl = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/'
    #serializers.urllib2.urlopen(baseurl+code+".xml"))
    #tree = ET.parse(urllib2.urlopen(baseurl+code+".xml"))
    #f = urllib2.urlopen( baseurl+code+".xml" ).read()
    #xmlstring = str(re.sub('xmlns="urn:hl7-org:v3"', '', f)) ##This removes the namespace
    #tree = ET.parse(f)
    #root = tree.getroot()

    #baseurl = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/'
    #soup = BeautifulSoup(urllib2.urlopen(baseurl+code+".xml"))
    #try:
    #    packager = soup.find_all('name')[0].text
    #except:
    #    packager = []
    #try:
    #    category = soup.find("code")['displayname']
    #except:
    #    category = []
    #try:
    #    boxed_warning = soup.find("section", id="splSectionBlackBox").text
    #except:
    #    boxed_warning = []
    #try:
    #    description = soup.find("section", id="splSectionDescription").text
    #except:
    #    description = []
    #dictionaries = { 'description': description, 'boxed_warning': boxed_warning, 'code': code, 'packager': packager, 'category': category, }



