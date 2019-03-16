# -*- coding: utf-8 -*-
from __future__ import division
# if doc_similarity>threshold1, then newsim = gangsim + nbhsim + gmemsim 

import json
# import simplejson  # simplejson provides more descriptive error message
import os
# import datefinder
from html.parser import HTMLParser
# from html.parser import HTMLParser
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from gensim import corpora, models, similarities
from pprint import pprint
import datetime
import numpy as np
from collections import defaultdict

readstops1, readstops = [], []
stopfile = open('exp1/stopwords-es.txt', 'r', encoding='UTF-8')
for line in stopfile:
    line = line.strip()
    readstops1.append(line)

for stopword in readstops1:
    readstops.append(stopword)

stemmer = SnowballStemmer("spanish")

ganglist1 = ['Bandas Criminales', 'BACRIM', 'Los Urabeños', 'Los Rastrojos', 'ERPAC', 'FARC', ' ELN',
             ' Ejército de Liberación Nacional', 'Fuerzas Armadas Revolucionarias de Colombia', 'FARC–EP',
             'Fuerzas Armadas Revolucionarias de Colombia—Ejército del Pueblo', 'Los Angelitos', 'Los Magníficos',
             'Los Norteños El Parche', 'Los Tesos', 'Los Yiyos', 'Los Mongolitos', 'Los Jíbaros', 'Los Chamizo',
             'Los Chamos', 'Los Vacasen', 'La Banda del Negro Orlando', 'Los Kits Los Daza', 'Los Paisas',
             'Los Pájaros', 'El Turco', 'El Zarco', 'El Monedita', 'El Mono', 'Los Simpson', 'Los Monsalve',
             'Los Parrado', 'Los Peluzas', 'Los Moros', 'Los Gomelos', 'Los Rusos', 'Los Destroyers', 'Los Nicos',
             'Los Monos', 'Los Navajas', 'Los Cucarachos', 'Los Magníficos', 'Los Choquis', 'Los Pitufos', 'El Caballo',
             'El Beto', 'Los Nazi', 'El Coronel', 'Los Calvos', 'El Jinete', 'El Parche', 'Los Velozas', 'Los Vampiros',
             'Los Cucarrones', 'Los Chéveres', 'Los Cocos', 'Los Rapados', 'Los Zepelines', 'Los Zorreros',
             'Los Galletas', 'Los Gomelos', 'Los Bollos', 'Los Daza', 'Los Chachos', 'Los Rapados', 'Los Norteños',
             'Los Gusanos', 'Los Canecos', 'Los Tigres', 'Los Pablos', 'Los Paisas', 'El Caleño', 'Banda del Gallina',
             'Los Tacheros-Emboladores', 'Pandillas en Santa Isabel', 'Galán', 'Santa Matilde y Salazar Gómez',
             'Pandillas en El Guavio', 'Los Laches y El Consuelo', 'Los Camellos', 'Los Chávez', 'Los Gatos',
             'Los Diablos', 'Los Crespos', 'Los Camiones Chapulín', 'Los Romilocos', 'El Enano', 'Los Pecas',
             'Los N.Ns', 'Los Motas', 'El Memín', 'El Vaca Juanito', 'La 59', 'La Pulga', 'El Zapatero Milthon',
             'Los Brothers', 'Los Memos', 'Los Kikos']
nbhlist1 = ['Usaquén', 'Chapinero', 'Santafé', 'San Cristobal', 'Usme', 'Tunjuelito', 'Bosa', 'Kennedy', 'Fontibón',
            'Engativá', 'Suba', 'Barrios Unidos', 'Teusaquillo', 'los Mártires', 'Antonio Nariño', 'Puente Aranda',
            'La Candelaria', 'Rafael Uribe Uribe', 'Ciudad Bolívar']
ldlist1 = ['Paseo los libertadores', 'Las ferias', 'El Refugio', 'Sagrado Corazón', 'San Blas', 'Verbenal',
           'Minuto de Dios', 'San Isidro', 'La Macarena', 'Sosiego', 'La Uribe', 'Boyacá Real', 'Prdo Rubio',
           'Las Nieves', '20 de Julio', 'San Cristóbal', 'Santa Cecilia', 'Chico Lago', 'Las Cruces', 'Gloria',
           'Toberín', 'Bolivia', 'Chapinero', 'Lourdes', 'Los Libertadores', 'Los Cedros', 'Garcés Navas', 'Usaquén',
           'Engativa', 'Country Club', 'Jardín Botánico', 'Santa Bárbara', 'Alamos', 'La Flora', 'Venecia',
           'Fontibón', 'Apogeo', 'Santa Isabel', 'Danubio', 'Tunjuelito', 'Fontibón San Pablo', 'Bosa occidental',
           'La Sabana', 'Gran Yomasa', 'Zona Franca', 'Bosa central', 'Comuneros', 'Ciudad Salitre occidente',
           'El Porvenir', 'Alfonso López', 'Granjas de techo', 'Tintal Sur', 'Parque Entrenubes', 'Modelia',
           'Ciudad Usme', 'Capellanía', 'Aeropuerto El Dorado', 'Castilla', 'La Academia', 'Los Andes', 'Galenas',
           'Ciudad Jardín', 'Américas', 'Guaymaral', 'Doce de Octubre', 'Teusaquillo', 'Restrepo', 'Carvajal',
           'San José de Bavaria', 'Los Alcázares', 'Parque Simón Bolívar', 'Kennedy Central', 'Britalia',
           'Parque Salitre', 'La Esmeralda', 'Timiza', 'El Prado', 'Quinta Paredes', 'Tintal Norte', 'La Alhambra',
           'Ciudad Salitre Oriental', 'Calandaima', 'Casa Blanca Suba', 'Corabastos', 'Niza', 'Gran Britalia',
           'La Floresta', 'Patio Bonito', 'Suba', 'Las Margaritas', 'El Rincón', 'Bavaria', 'Tibabuyes',
           'Ciudad Montes', 'La Candelaria', 'San José', 'El Mochuelo', 'Muzú', 'Quiroga', 'Monteblanco',
           'San Rafael', 'Marco Fidel Suárez', 'Arborizadota', 'Zona Industrial', 'Marruecos', 'San Francisco',
           'Puente Aranda', 'Diana Turbay', 'Lucero', 'El Tesoro', 'Ismael Perdomo', 'Jerusalem', 'Usaquén',
           'Chapinero', 'Santa Fe', 'San Cristóbal', 'Usme', 'Tunjuelito', 'Bosa', 'Kennedy', 'Fontibón', 'Engativá',
           'Suba', 'Barrios Unidos', 'Teusaquillo', 'Los Mártires', 'Antonio Nariño', 'Puente Aranda',
           ' 	La Candelaria', 'Rafael Uribe Uribe', 'Ciudad Bolívar', 'Sumapaz']
nbh = nbhlist1 + ldlist1
gmemlist1 = ['Vicente Castaño', 'Ivan Marquez', 'Luis Enrique Calle Serna', 'El Paisa', 'Rastrojos', 'Simon Trinidad',
             'Puntilla', 'Tanja Nijmeijer', 'ERPAC', 'Don Berna', 'Don Mario', 'Pablo Beltran', 'Pastor Alape',
             'Joaquin Gomez', 'Otoniel', 'Urabeños', "Daniel 'El Loco' Barrera", 'Fabian Ramirez', 'EPL', 'Los Pelusos',
             'Aguilas Negras', 'Libertadores de Vichada', 'AGC', 'Gaitanista Self-Defense Forces of Colombia', 'Paisas',
             'FIAC', 'Megateo', 'Salvatore Mancuso', 'Romaña', 'Oficina de Envigado', 'Pablo Escobar', 'Timochenko',
             'Pablito', 'Carlos Marin Guarin', 'Antonio Garcia', 'Pablo Beltrán', 'Gabino', 'Calle Serna', 'Pijarbey',
             'Martin Farfan Diaz Gonzalez', 'Comba', 'Otoniel', 'Dario Antonio Usuga', 'Efrain Guzman', ' Nariño',
             'Iván Marquéz', 'Mauricio Jaramillo', 'El Médico', 'Pablo Catatumbo', 'Timoleón Jiménez', 'Juaquin Gomez']

ganglist = []
nbhlist = []
gmemlist = []

featurefile = open('features-precursors10.txt', 'a+')
featurefile.truncate()
precursorfile = open('precursors10.txt', 'a+')
precursorfile.truncate()
pretfidf = open('precursor-tfidf-10.txt', 'a+')
pretfidf.truncate()
f_entityfile = open('feature-entities10.txt', 'a+')
f_entityfile.truncate()

for word in ganglist1:
    word = word.lower()
    ganglist.append(word)
for word in nbh:
    word = word.lower()
    nbhlist.append(word)
for word in gmemlist1:
    word = word.lower()
    gmemlist.append(word)


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def calc_similarity(joinedtext, stringdict1, date, titlelist, stringlist, datelist, sourcedict, granddict):
    returntitles, featurelist, featureentities = [], [], []
    documents = []
    for st in stringlist:
        documents.append(st)
    documents.append(joinedtext)
    topic_num = int(len(documents) / 2)  # number of topics matters. Play with it.
    if topic_num <= 0:  # we cannot deal with 0 topics
        topic_num = 1
    if topic_num >= 50:  # set different values here, and see what you get
        topic_num = 50
    # print 'topic_num: ', topic_num
    texts = [[word for word in document.lower().split()] for document in documents]
    frequencyl = defaultdict(int)
    for text in texts:
        for token in text:
            frequencyl[token] += 1
    textsl = [[token for token in text if frequencyl[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(textsl)
    corpus = [dictionary.doc2bow(text) for text in textsl]
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=topic_num, id2word=dictionary, passes=20)  # try with LDA
    doc = joinedtext
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lda = ldamodel[vec_bow]
    index = similarities.MatrixSimilarity(ldamodel[corpus])
    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    titles = []
    strings = []
    for items in sims:
        if items[1] >= 0.9:  # for tfidf the similarity is very low. The highest was 0.05 in the small corpus of 31 documents.
            if items[0] < len(titlelist):  # do it in progression and calculate words of high tf-idf from crimes and nocrimes take iintersect of
                testtitle = titlelist[items[0]]  # these features and crime high tfidf minus no-crime high-tfidf
                newsim = 0
                # print 'start date and title: ', sourcedict['date'], ': ', sourcedict['title']
                # print 'date and testtitle: ', datelist[items[0]], ': ', testtitle
                newdict = granddict[testtitle]
                targetgangs = newdict['gang']
                targetnbh = newdict['nbh']
                targetentities = newdict['gmem']
                targetentities2 = newdict['entity']
                sourcegangs = sourcedict['gang']
                sourcenbh = sourcedict['nbh']
                sourceentities = sourcedict['gmem']
                gangintersect = list(set.intersection(set(sourcegangs), set(targetgangs)))
                nbhintersect = list(set.intersection(set(sourcenbh), set(targetnbh)))
                entityintersect = list(set.intersection(set(sourceentities), set(targetentities)))
                ganglenint, nbhlenint, entitylenint = len(gangintersect), len(nbhintersect), len(entityintersect)
                gangunion = list(set.union(set(sourcegangs), set(targetgangs)))
                nbhunion = list(set.union(set(sourcenbh), set(targetnbh)))
                entityunion = list(set.union(set(sourceentities), set(targetentities)))
                ganglenunion, nbhlenunion, entitylenunion = len(gangunion), len(nbhunion), len(entityunion)
                if ganglenunion == 0:
                    gangsim = 0
                else:
                    gangsim = ganglenint / ganglenunion
                if nbhlenunion == 0:
                    nbhsim = 0
                else:
                    nbhsim = nbhlenint / nbhlenunion
                if entitylenunion == 0:
                    entitysim = 0
                else:
                    entitysim = entitylenint / entitylenunion
                newsim = gangsim + nbhsim + entitysim  # the similarity score
                if newsim > 0:  # play with the threshold
                    tuple = (datelist[items[0]], testtitle)
                    returntitles.append(tuple)
                    for g in targetgangs:
                        featurelist.append(g)
                    for n in targetnbh:
                        featurelist.append(n)
                    for e in targetentities:
                        featurelist.append(e)
                    for e2 in targetentities2:
                        featureentities.append(e2)
                titles.append(titlelist[items[0]])
    featurelist = list(set(featurelist))
    # precursorfile.write('start date and title:\n')
    # precursorfile.write(sourcedict['date'] + ': ' + sourcedict['title'] + '\n')
    # pretfidf.write(sourcedict['title'])
    # pretfidf.write('\n')
    return returntitles, featurelist, featureentities


# calc_target_lda_words(titles, strings)



def check_similarity(joinedtext, date, entry, sourcedict):
    daten = datetime.datetime.strptime(date, '%Y-%m-%d')
    root1 = os.getcwd()
    dir = os.path.join(root,'bogotest2')  # local drive: 'crimes-and-nocrimes05-06-bogota', argo: 'bogota-all-2015-05-06'
    orgdict = {}
    persondict = {}
    stringdict1 = {}
    temptitle = []
    titlelist = []
    datelist = []
    granddict = {}
    stringlist = []
    for file in os.listdir(dir):
        linecount = 0
        filename = os.path.join(dir,file)  # need to create an absolute path: F:\Anaconda\homicide\datasets\Text_data\newdata\test4\crime2015-06\rss-content-enriched-2015-06-01-04-21-28
        entry = filename[-19:]
        x = linecount
        entry = entry + '_' + str(x)
        if entry in stringdict1.keys():
            pass
        else:
            stringdict1[entry] = []
        with open(filename,encoding='UTF-8') as f:
            entitydict = {}
            for line in f:
                check1, check2, texts, stopped_tokens, stopped_lemmas, lemmas3, orgs, orgs1, persons, glist1, nlist1, elist1, gmlist1 = [], [], [], [], [], [], [], [], [], [], [], [], []
                newtext = ' '
                newdate = ''
                datestring = ' '
                diff = -1
                linecount += 1
                line = line.strip()
                if line:
                    jsonData = line
                    try:
                        dict = json.loads(jsonData)
                        for key in dict:
                            if key == 'date':
                                value = dict[key]
                                dateval = value
                                datestring = str(dateval)
                                newdate = datetime.datetime.strptime(dateval, '%Y-%m-%d')
                                diff = daten - newdate
                            if key == 'Content' or key == 'content':
                                value = dict[key]
                                string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
                                string = string.lower()
                                plain_string = strip_tags(string)
                                for gang in ganglist:
                                    if gang in string:
                                        glist1.append(gang)
                                for nbh in nbhlist:
                                    if nbh in string:
                                        nlist1.append(nbh)
                                for gmem in gmemlist:
                                    if gmem in string:
                                        gmlist1.append(gmem)
                                if plain_string:
                                    tokenizer = RegexpTokenizer(r'\w+')
                                    raw = plain_string.lower()
                                    tokens = tokenizer.tokenize(raw)
                                    tokens2 = [x.lower() for x in tokens if x is not None]
                                    stopped_tokens = [t for t in tokens2 if not t in readstops]
                                    texts = [stemmer.stem(x) for x in stopped_tokens if x is not None]
                            if key == 'content_title':
                                value = dict[key]
                                titlem = value.lower()
                                title = value.encode('utf-8')
                                entitydict[title] = []
                                for gang in ganglist:
                                    if gang in titlem:
                                        glist1.append(gang)
                                for nbh in nbhlist:
                                    if nbh in titlem:
                                        nlist1.append(nbh)
                                for gmem in gmemlist:
                                    if gmem in titlem:
                                        gmlist1.append(gmem)
                            if key == 'BasisEnrichment':
                                value = dict[key]
                                lemmas = []
                                tokens = value.get('tokens')  # tokens is a list of dictionaries
                                found = 0
                                for x in range(len(tokens)):  # for each dictionary
                                    item = tokens[x]  # take each dictionary to item
                                    for key in item:  # for each key in that dictionary
                                        if key == 'lemma':
                                            lemmas.append(item[key])
                                if lemmas:
                                    lemmas2 = [l.lower() for l in lemmas if l is not None]
                                    stopped_lemmas = [l for l in lemmas2 if not l in readstops]
                                    lemmas3 = [stemmer.stem(x) for x in stopped_lemmas if x is not None]
                                entities = value.get('entities')
                                for x in range(len(entities)):
                                    org, person, loc = 0, 0, 0
                                    item = entities[x]
                                    for k in item:
                                        if k == 'neType' and item[k] == 'ORGANIZATION':
                                            org = 1
                                        if org == 1 and k == 'expr':
                                            elist1.append(item[k])
                                        if k == 'neType' and item[k] == 'PERSON':
                                            person = 1
                                        if person == 1 and k == 'expr':
                                            elist1.append(item[k])
                                        if k == 'neType' and item[k] == 'LOCATION':
                                            # print k, item[k]
                                            loc = 1
                                        if loc == 1 and k == 'expr':
                                            elist1.append(item[k])
                                        orgval = ''
                                        if k == 'expr':
                                            orgval = item[k]
                                        if k == 'neType' and item[k] == 'ORGANIZATION':
                                            if orgval:
                                                elist1.append(orgval)
                                        locval = ''
                                        if k == 'expr':
                                            locval = item[k]
                                        if k == 'neType' and item[k] == 'LOCATION':
                                            if locval:
                                                elist1.append(locval)
                                        pval = ''
                                        if k == 'expr':
                                            pval = item[k]
                                        if k == 'neType' and item[k] == 'PERSON':
                                            if pval:
                                                elist1.append(pval)
                                orgs1 = list(set(orgs))
                                persons1 = list(set(persons))
                                elist1 = [e.lower() for e in elist1]
                                for gang in ganglist:
                                    if gang in elist1:
                                        glist1.append(gang)
                                for nbh in nbhlist:
                                    if nbh in elist1:
                                        nlist1.append(nbh)
                                for gmem in gmemlist:
                                    if gmem in elist1:
                                        gmlist1.append(gmem)
                                glist1 = list(set(glist1))
                                nlist1 = list(set(nlist1))
                                elist1 = list(set(elist1))
                                gmlist1 = list(set(gmlist1))
                            orglist = []
                            if stopped_tokens:
                                newtext = ' '.join([word for word in stopped_tokens if word not in readstops])
                            else:
                                newtext = ' '.join([word for word in stopped_lemmas if word not in readstops])
                            for key, val in orgsdict.items():
                                if val >= count:
                                    orglist.append(key)
                    except ValueError as e:
                        print(e)
                        pass
                found = 0
                if diff.days > 0 and diff.days <= 14:
                    for key, val in stringdict1.items():
                        lists = val
                        if newtext in lists:
                            found = 1
                    if found == 0:
                        stringdict1[entry].append(newtext)
                        stringlist.append(newtext)
                        titlelist.append(title)
                        datelist.append(datestring)
                        granddict[title] = {}
                        granddict[title]['gang'] = glist1
                        granddict[title]['nbh'] = nlist1
                        granddict[title]['entity'] = elist1
                        granddict[title]['gmem'] = gmlist1
                        granddict[title]['date'] = datestring
    # print 'calling calc_similarity...\n'
    returntitles, featurelist, featureentities = calc_similarity(joinedtext, stringdict1, date, titlelist, stringlist,
                                                                 datelist, sourcedict, granddict)
    if returntitles:
        precursorfile.write('Precursors: \n')
        for title in returntitles:
            precursorfile.write(title[0] + ': ' + title[1])
            precursorfile.write('\n')
            pretfidf.write(title[1])
            pretfidf.write('\n')
    precursorfile.write('\n')
    pretfidf.write('\n')
    if featurelist:
        for item in featurelist:
            featurefile.write(item.encode('utf-8'))
            featurefile.write('\n')
    if featureentities:
        for item in featureentities:
            f_entityfile.write(item.encode('utf-8'))
            f_entityfile.write('\n')


print('Running.')  # program starts running from here
count = 1
orgsdict = {}
personsdict = {}
titledict = {}
titlelist = []
topicdict = {}
datelist = []

root = os.getcwd()
crimedir = os.path.join(root,'bogotest1')  # crimedir:  F:\Anaconda\homicide\datasets\Text_data\newdata\test4\crime2015-06
# set your start article directory
# crimedir = os.path.join(root, 'bogota-allcrimes-2015-05-06') #argo
for file in os.listdir(crimedir):
    sourcedict = {}
    linecount = 0
    filename = os.path.join(crimedir,file)  # need to create an absolute path: F:\Anaconda\homicide\datasets\Text_data\newdata\test4\crime2015-06\rss-content-enriched-2015-06-01-04-21-28
    if (filename != 'bogota-allcrimes-2015-05-06'):  # ('dir' not in filename):
        with open(filename, encoding='UTF-8') as f:
            joinedtext = ' '
            for line in f:
                linecount += 1
                joinedtext = ' '
                line = line.strip()
                if line:
                    jsonData = line
                    sourcedict = {}
                    glist, nlist, elist, gmlist, flist, fentities = [], [], [], [], [], []
                    lemmas2, tokens2, texts, lemmas3, stopped_tokens, stopped_lemmas = [], [], [], [], [], []
                    stringdict = {}
                    try:
                        dict = json.loads(jsonData)
                        for key in dict:
                            entry = filename[-19:]  # index using the filename to make each unique
                            x = linecount
                            entry = entry + '_' + str(x)
                            if key == 'Content' or key == 'content':  # this is the actual news content
                                value = dict[key]
                                string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
                                string = string.lower()
                                plain_string = strip_tags(string)
                                for gang in ganglist:
                                    if gang in string:
                                        glist.append(gang)
                                for nbh in nbhlist:
                                    if nbh in string:
                                        nlist.append(nbh)
                                for gmem in gmemlist:
                                    if gmem in string:
                                        gmlist.append(gmem)
                                if plain_string:
                                    tokenizer = RegexpTokenizer(r'\w+')
                                    raw = plain_string.lower()
                                    tokens = tokenizer.tokenize(raw)
                                    tokens2 = [x.lower() for x in tokens if x is not None]
                                    stopped_tokens = [t for t in tokens2 if not t in readstops]  # remove stopwords
                                    texts = [stemmer.stem(x) for x in stopped_tokens if x is not None]  # stem the words
                            if key == 'content_title':  # title of the news article
                                value = dict[key]
                                titlemain = value.lower()
                                title = value.encode('utf-8')
                                precursorfile.write('start date and title:\n')
                                precursorfile.write(str(title))  # you can also write the date to keep tract of the article dates
                                precursorfile.write('\n')
                                pretfidf.write(str(title))
                                pretfidf.write('\n')
                                for gang in ganglist:  # check for gangnames
                                    if gang in titlemain:
                                        glist.append(gang)
                                        flist.append(gang)
                                for nbh in nbhlist:  # check for neighborhood names
                                    if nbh in titlemain:
                                        nlist.append(nbh)
                                        flist.append(nbh)
                                for gmem in gmemlist:  # check for gangmembers
                                    if gmem in titlemain:
                                        gmlist.append(gmem)
                                        flist.append(gmem)
                            if key == 'BasisEnrichment':
                                value = dict[key]
                                lemmas = []
                                tokens = value.get('tokens')  # tokens is a list of dictionaries
                                found = 0
                                for x in range(len(tokens)):  # for each dictionary
                                    item = tokens[x]  # take each dictionary to item
                                    for key in item:  # for each key in that dictionary
                                        if key == 'lemma':
                                            lemmas.append(item[key])
                                if lemmas:
                                    lemmas2 = [l.lower() for l in lemmas if l is not None]
                                    stopped_lemmas = [l for l in lemmas2 if not l in readstops]
                                    lemmas3 = [stemmer.stem(x) for x in stopped_lemmas if x is not None]
                                entities = value.get('entities')
                                for x in range(len(entities)):
                                    org, person, loc = 0, 0, 0
                                    item = entities[x]
                                    for k in item:  # we want to know each organization, person, and locations mentioned int he article
                                        if k == 'neType' and item[k] == 'ORGANIZATION':
                                            org = 1
                                        if org == 1 and k == 'expr':
                                            elist.append(item[k])
                                            fentities.append(item[k])
                                        if k == 'neType' and item[k] == 'PERSON':
                                            person = 1
                                        if person == 1 and k == 'expr':
                                            elist.append(item[k])
                                            fentities.append(item[k])
                                        if k == 'neType' and item[k] == 'LOCATION':
                                            loc = 1
                                        if loc == 1 and k == 'expr':
                                            elist.append(item[k])
                                            fentities.append(item[k])
                                        orgval = ''
                                        if k == 'expr':
                                            orgval = item[k]
                                        if k == 'neType' and item[k] == 'ORGANIZATION':
                                            if orgval:
                                                elist.append(orgval)
                                                fentities.append(item[k])
                                        locval = ''
                                        if k == 'expr':
                                            locval = item[k]
                                        if k == 'neType' and item[k] == 'LOCATION':
                                            if locval:
                                                elist.append(locval)
                                                fentities.append(item[k])
                                        pval = ''
                                        if k == 'expr':
                                            pval = item[k]
                                        if k == 'neType' and item[k] == 'PERSON':
                                            if pval:
                                                elist.append(pval)
                                                fentities.append(item[k])
                                elist = [e.lower() for e in elist]
                                for gang in ganglist:
                                    if gang in elist:
                                        glist.append(gang)
                                        flist.append(gang)
                                for nbh in nbhlist:
                                    if nbh in elist:
                                        nlist.append(nbh)
                                        flist.append(nbh)
                                for gmem in gmemlist:
                                    if gmem in elist:
                                        gmlist.append(gmem)
                                        flist.append(gmem)
                                glist = list(set(glist))
                                nlist = list(set(nlist))
                                elist = list(set(elist))
                                gmlist = list(set(gmlist))
                                flist = list(set(flist))
                            if key == 'date':
                                value = dict[key]
                                date = str(value)
                            if stopped_tokens:
                                joinedtext = ' '.join([word for word in stopped_tokens if word not in readstops])
                            else:
                                joinedtext = ' '.join([word for word in stopped_lemmas if word not in readstops])
                    except ValueError as e:
                        print(e)
                        pass
                stringdict[entry] = joinedtext
                sourcedict['title'] = title
                sourcedict['date'] = date
                sourcedict['gang'] = glist
                sourcedict['nbh'] = nlist
                sourcedict['gmem'] = gmlist
                sourcedict['entity'] = elist
                if flist:
                    for item in flist:
                        featurefile.write(str(item.encode('utf-8')))
                        featurefile.write('\n')
                if fentities:
                    for item in fentities:
                        f_entityfile.write(str(item.encode('utf-8')))
                        f_entityfile.write('\n')

                # for key, val in sourcedict.items():
                #	print key, ': ', val
                # print
                check_similarity(joinedtext, date, entry, sourcedict)  # calling to check similarity

featurefile.close()
precursorfile.close()
f_entityfile.close()
pretfidf.close()
stopfile.close()
