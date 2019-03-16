# -*- coding: utf-8 -*-
from __future__ import division
import csv
import json
#import simplejson  # simplejson provides more descriptive error message
import os
from nltk.tokenize import RegexpTokenizer
from HTMLParser import HTMLParser
import pandas as pd
import numpy as np
import scipy.io
from datetime import datetime, timedelta 
import math
from sklearn.metrics import f1_score, precision_recall_fscore_support
from sklearn.svm import SVR
from sklearn import preprocessing
import statsmodels.formula.api as smf
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn import metrics


#ganglist1 = ['Los Angelitos','ERPAC','Gaitanistas','La Oficina de Envigado','Nueva Generación', 'Los Magníficos','Aguilas Negras','Black Eagles','AUC','United Self-Defense Forces of Colombia','Autodefensas Unidas de Colombia','Nueva Orteguaza','Autodefensas Gaitanistas de Colombia','Ejército Popular de Liberación','EPL','Clan del Golfo','Águilas Negras', 'Los Norteños El Parche', 'Los Tesos', 'Los Yiyos', 'Los Mongolitos', 'Los Jíbaros', 'Los Chamizo', 'Los Chamos','Los Vacasen','La Banda del Negro Orlando','Los Kits Los Daza','Los Paisas','Los Pájaros','El Turco','El Zarco','El Monedita','El Mono','Los Simpson','Los Monsalve','Los Parrado','Los Peluzas','Los Moros','Los Gomelos','Los Rusos','Los Destroyers','Los Nicos','Los Monos','Los Navajas','Los Cucarachos','Los Magníficos','Los Choquis','Los Pitufos','El Caballo','El Beto','Los Nazi','El Coronel','Libertadores del Vichada','Oficina de Envigado','El Flaco','Los Calvos','El Jinete','El Parche','Los Velozas','Los Vampiros','Los Cucarrones','Los Chéveres','Los Cocos','Los Rapados','Los Zepelines','Los Zorreros','Los Galletas','Los Gomelos','Los Puntilleros','Meta Bloc','Puntilla','Los Bollos','Los Daza','AGC','Clan Usuga','Urabeños','Clan del Golfo','Rastrojos','Los Chachos','Los Rapados','Los Norteños','Los Gusanos','Los Canecos','Los Tigres','Los Pablos','Los Paisas','El Caleño','Banda del Gallina','Los Tacheros-Emboladores','bacrim','Otoniel','Black Eagles','Las Águilas Negras',' Úsuga','Bloque Meta',' Los Machos','Renacer','Los Gaitanistas','Nueva Generación','Libertadores del Vichada','The Office of Envigado','Los Urabeños','Pandillas en Santa Isabel','Galán','Santa Matilde y Salazar Gómez','Pandillas en El Guavio','Los Laches y El Consuelo','Los Camellos','Los Chávez','Los Gatos','Los Diablos','Los Crespos','Los Camiones Chapulín','Los Romilocos','El Enano','Los Pecas','Los N.Ns','Los Motas','El Memín','El Vaca Juanito','La 59','La Pulga','El Zapatero Milthon','Los Brothers','Los Memos','Los Kikos']
nbhlist1 = ['Usaquén','Chapinero', 'Santafé','San Cristobal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','los Mártires','Antonio Nariño','Puente Aranda','La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar']	
ldlist1 = ['Paseo los libertadores','Las ferias','El Refugio','Sagrado Corazón','San Blas','Verbenal','Minuto de Dios','San Isidro','La Macarena','Sosiego','La Uribe','Boyacá Real','Prdo Rubio','Las Nieves','20 de Julio','San Cristóbal','Santa Cecilia','Chico Lago','Las Cruces','Gloria','Toberín','Bolivia','Chapinero','Lourdes','Los Libertadores','Los Cedros','Garcés Navas','Usaquén','Engativa','Country Club','Jardín Botánico','Santa Bárbara','Alamos','La Flora','Venecia','Fontibón','Apogeo','Santa Isabel','Danubio','Tunjuelito','Fontibón San Pablo','Bosa occidental','La Sabana','Gran Yomasa','Zona Franca','Bosa central','Comuneros','Ciudad Salitre occidente','El Porvenir','Alfonso López','Granjas de techo','Tintal Sur','Parque Entrenubes','Modelia','Ciudad Usme','Capellanía','Aeropuerto El Dorado','Castilla','La Academia','Los Andes','Galenas','Ciudad Jardín','Américas','Guaymaral','Doce de Octubre','Teusaquillo','Restrepo','Carvajal','San José de Bavaria','Los Alcázares','Parque Simón Bolívar','Kennedy Central','Britalia','Parque Salitre','La Esmeralda','Timiza','El Prado','Quinta Paredes','Tintal Norte','La Alhambra','Ciudad Salitre Oriental','Calandaima','Casa Blanca Suba','Corabastos','Niza','Gran Britalia','La Floresta','Patio Bonito','Suba','Las Margaritas','El Rincón','Bavaria','Tibabuyes','Ciudad Montes','La Candelaria','San José','El Mochuelo','Muzú','Quiroga','Monteblanco','San Rafael','Marco Fidel Suárez','Arborizadota','Zona Industrial','Marruecos','San Francisco','Puente Aranda','Diana Turbay','Lucero','El Tesoro','Ismael Perdomo','Jerusalem','Usaquén','Chapinero','Santa Fe','San Cristóbal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','Los Mártires','Antonio Nariño','Puente Aranda',' 	La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar','Sumapaz']
#gmemlist1 = ['Vicente Castaño',' Ramón Navarro Serrano','Megateo', 'Ivan Marquez','Luis Enrique Calle Serna','Octavio Orrego','Sebastián','Carlos Andres Bustos Cortez','Jairo Alirio Puerta Peña','Cuñado','Omar', 'El Paisa', 'Rastrojos', 'Simon Trinidad','Puntilla','Tanja Nijmeijer', 'ERPAC', 'Don Berna','Don Mario','Pablo Beltran','Pastor Alape','Joaquin Gomez','Otoniel','Urabeños', "Daniel 'El Loco' Barrera", 'Fabian Ramirez','EPL','Los Pelusos','Aguilas Negras','Libertadores de Vichada','AGC','Gaitanista Self-Defense Forces of Colombia','Paisas','FIAC','Megateo','Salvatore Mancuso','Romaña','Oficina de Envigado','Pablo Escobar','Franco Jiménez','German','Nicolas Rodriguez Bautista','Gabino','Eliecer Erlinto Chamorro','Antonio Garcia','Miguel Ángel Alfaro','Dámaso López Núñez','Luciano Marin Arango','Ivan Marquez','Cesarin','Roberto Vargas Gutierrez','Gavilan','Fredy Alonzo Mira Perez','Fredy Colas','Licenciado','Jorge 40','Movil 7','Timochenko','Pablito','Abimel Coneo Martínez','Torta','Carlos Marin Guarin','Antonio Garcia','Pablo Beltrán','Gabino','Calle Serna','Pijarbey','Martin Farfan Diaz Gonzalez','Comba','Otoniel','Martín Farfán Díaz González','Pijarbey','Díaz González','Dairo Antonio Úsuga David','Mao','Guillermo Alejandro','Dario Antonio Usuga','Raul Jaramillo','Abeja','Efrain Guzman',' Nariño','Iván Marquéz','Mauricio Jaramillo','El Médico','Pablo Catatumbo','Timoleón Jiménez','Juaquin Gomez','Blanco','Escobar','Orejuela','Úsuga']
newnbh = ['Antioquia','Meta','Envigado','Arauca','Guaviare','Vichada','Valle del Cauca','Sucre','Cqueta','Huila','Putumayo','Quindio','Risaralda','Tolima','Boyaca','Santander','Norte de Santander','Buenaventura','Magdalena','Caquetá','Vichada','Guaviare','Casanare','Uraba','Cordoba','Guajira','Bolivar','Sucre','Cesar','Cauca','Chocó','Tumaco','Nariño']
nbhlist2 = nbhlist1 + ldlist1

ganglist1 = ['los urabeños','rastrojos','urabeños','galán','ejército popular de liberación','autodefensas unidas de colombia','Los Urabeños','otoniel','auc','epl','el coronel','La Resistencia','Cárteles Unidos']
gmemlist1 = ['calle serna','dario antonio usuga','megateo','don berna','blanco','pastor alape','pablo escobar','escobar','el médico','pablo catatumbo','cuñado','nariño','comba','omar','El Molca','Ramiro Pozos','Nemesio Oseguera','El Mencho']
nbhlist1 = ['san francisco','la y','niza','caracas','une','uraba']
ganglist = []
nbhlist = []
gmemlist = []

for word in ganglist1:
	word = word.lower()
	ganglist.append(unicode(word, 'utf-8'))
for word in newnbh:
	word = word.lower()
	nbhlist.append(unicode(word, 'utf-8'))
for word in gmemlist1:
	word = word.lower()
	gmemlist.append(unicode(word, 'utf-8'))

#print type(ganglist[0])
#print type(nbhlist[0])
#print type(entitylist[0])

#df = pd.read_csv("F:\Anaconda\homicide\datasets\homicide_count_2015_06_06_Bogota.csv")
#df['date'] = pd.to_datetime(df['date'], format = )
out = open('classifier-outputs.txt', 'a+')
out.truncate()
out.write('Outputs from classifier.py\n')

predfile = open('predictions.txt', 'a+')
predfile.truncate()

readstops1, readstops = [], []
stopfile = open('stopwords.txt', 'r')
for line in stopfile:
	line = line.strip()
	readstops1.append(line)

for stopword in readstops1:
	readstops.append(unicode(stopword, 'utf-8'))

def mean_absolute_error(y, pred):
	return np.mean(abs(y-pred))
def root_mean_squared_error(y, pred):
	return math.sqrt(np.mean((y-pred)**2))
	
class MLStripper(HTMLParser):
    def __init__(self):
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
	
exceldict = {}
def read_excel():
	#root = os.getcwd()
	file = 'homicide_count_area3_15_16.csv'	#'homicide_count_area2_15_16.csv', homicide_count_15_16_bogota.csv 
	#file = 'F:\Anaconda\homicide\datasets\homicide_count_area2_15_16.csv'  #homicide_2015_muni_date_homicidios_3.csv
	# homicide_15_16_date_n_homicidios.csv --> all cities, not only bogota, avg homicide: 13
	#filename = os.path.join(root, file)
	with open(file) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			#if row[0] == 'BOGOTA DC (CT)':
				#print row[0],
			datestring = row[0]
			count = int(row[1])
			dateval = datetime.strptime(datestring, '%d/%m/%Y')
			if dateval in exceldict:
				exceldict[dateval] += count
			else:
				exceldict[dateval] = count
			#else:
			#	pass
	#for key, val in exceldict.items():
	#	print key, ': ', val

test_f = open('test_features.txt', 'a+')
test_f.truncate()
def createinstances(startdate, enddate, dir, features, histdays, leadtime, bucket,gap):
	date = startdate
	diff = enddate - date 
	instancelist = []
	while diff.days >= 0: 
		diff = enddate - date
		featuredict = {}
		count = 0
		for feature in features:
			featuredict[feature] = 0
		for file in os.listdir(dir):
			filename = os.path.join(dir, file)
			part = filename[-19:]
			part = part[:10]
			filedate = datetime.strptime(part, '%Y-%m-%d')
			difffile = date - filedate
			if difffile.days >= leadtime and difffile.days < histdays:
				count += 1
				with open(filename) as f:
					for line in f:
						line = line.strip()
						if line:
							jsondata = line
							try:
								dict = json.loads(jsondata)
								for key in dict:
									if key == 'Content' or key == 'content':
										value = dict[key]
										string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
										string = string.lower()
										for feature in features:
											if feature in string:
												featuredict[feature] += 1
									if key == 'content_title':
										
										value = dict[key]
										string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
										string = string.lower()
										for feature in features:
											if feature in string:
												featuredict[feature] += 1
									if key == 'BasisEnrichment':
										
										value = dict[key]
										entities = value.get('entities')
										entityfound = []
										for x in range(len(entities)):
											org = 0
											person = 0
											loc = 0
											item = entities[x]
											for k in item:
												if k == 'neType' and item[k] == 'ORGANIZATION':
													org = 1
												if org == 1 and k == 'expr':
													entityfound.append(item[k]) 
												if k == 'neType' and item[k] == 'LOCATION':
													loc = 1
												if loc == 1 and k == 'expr':
													entityfound.append(item[k])
												if k == 'neType' and item[k] == 'PERSON':
													person = 1
												if person == 1 and k == 'expr':
													entityfound.append(item[k])
												orgval = ''
												if k == 'expr':
													orgval = item[k]
												if k == 'neType' and item[k] == 'ORGANIZATION':
													if orgval:
														entityfound.append(orgval)
												locval = ''
												if k == 'expr':
													locval = item[k]
												if k == 'neType' and item[k] == 'LOCATION':
													if locval:
														entityfound.append(locval)
												pval = ''
												if k == 'expr':
													pval = item[k]
												if k == 'neType' and item[k] == 'PERSON':
													if pval:
														entityfound.append(pval)
										for feature in features:
											if feature in entityfound:
												featuredict[feature] += 1
							except ValueError as e:
								print e, filename
								pass						
			else:
				pass
		if count > 0:
			if bucket==1:
				ins = []
				for feature in features:
					ins.append(int(featuredict[feature]))
				if date in exceldict:
					val = exceldict[date]
					if val < 2:
						tuple = (ins, 0)
						instancelist.append(tuple))
					else:
						tuple = (ins,1)
						instancelist.append(tuple)
				else:
					tuple = (ins, 0)
					instancelist.append(tuple)
			else:
				ins = []
				for feature in features:
					ins.append(int(featuredict[feature]))
					test_f.write(feature.encode('utf-8'))
				newdate = date
				sum = 0
				for time in range(bucket):
					if newdate in exceldict:
						val = exceldict[newdate]
						sum += val
					else:
						val = 0
						sum += val
					newdate = newdate + timedelta(days=1)
				avg = sum/bucket
				if avg < 2:
					tuple = (ins, 0)
					instancelist.append(tuple)
				else:
					tuple = (ins,1)
					instancelist.append(tuple)
		else:
			pass
		date = date + timedelta(days=gap)
		diff = enddate - date
	return instancelist

def read_features(file_to_read):
	newfeatures = []
	with open(file_to_read, 'r') as f:
		for line in f:
			feature = line.strip()
			newfeatures.append(feature)
	return newfeatures

def read_tfidf(tfidffile):
	tfidflist = []
	with open(tfidffile, 'r') as f:
		for line in f:
			line = line.strip()
			words = line.split()
			score = float(words[-1])
			rest = words[:-1]
			string = ' '.join(rest)
			tfidflist.append(string)
	return tfidflist

def calc_tfidf(corpus):
	vectorizer = TfidfVectorizer(min_df=1)
	X = vectorizer.fit_transform(corpus)
	return X
	
def svm(train_x, train_y, test_x, test_y, bucket, threshold):
	print 'train_y:'
	print train_y
	C = 1.0
	model = SVC(kernel='rbf', gamma=0.7, C=C, probability=True).fit(train_x, train_y)  
	probs = model.predict_proba(test_x)
	preds = model.predict(test_x)
	print type(preds)
	print model.score(test_x, test_y)
	print confusion_matrix(preds, test_y)
	predlist = preds.tolist()
	print 'preds: ', predlist
	print 'y_test:', test_y
	print 'length of y_test: ', len(test_y)
	ones = [p for p in test_y if p == 1]
	twos = [p for p in test_y if p == 2]
	zeros = [p for p in test_y if p == 0]
	print '0: ', len(zeros), '1: ', len(ones), '2: ', len(twos)
	f1 =  sklearn.metrics.f1_score(test_y, predlist,pos_label=1) #,pos_label=2  average='weighted'
	recall = sklearn.metrics.recall_score(test_y, predlist,pos_label=1) #,pos_label=2
	precision = sklearn.metrics.precision_score(test_y, predlist,pos_label=1) #,pos_label=2
	acc = sklearn.metrics.accuracy_score(test_y, predlist)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))
	yarray = np.array(test_y)
	parray = np.array(predlist)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
	fpr, tpr, thresholds = metrics.roc_curve(test_y, probs[:,1])
	auc = metrics.auc(fpr, tpr);
	print 'auc: ', auc


def logistic(train_x, train_y, test_x, test_y, bucket, threshold):
	model = LogisticRegression()
	model = model.fit(train_x, train_y)
	preds = model.predict(test_x)
	probs = model.predict_proba(test_x)
	predlist = preds.tolist()
	print 'preds: ', predlist
	print 'y_test:', test_y
	print 'length of y_test: ', len(test_y)
	ones = [p for p in test_y if p == 1]
	twos = [p for p in test_y if p == 2]
	zeros = [p for p in test_y if p == 0]
	print '0: ', len(zeros), '1: ', len(ones), '2: ', len(twos)
	f1 =  sklearn.metrics.f1_score(test_y, predlist,pos_label=1) #,pos_label=2
	recall = sklearn.metrics.recall_score(test_y, predlist,pos_label=1) #,pos_label=2
	precision = sklearn.metrics.precision_score(test_y, predlist,pos_label=1) #,pos_label=2
	acc = sklearn.metrics.accuracy_score(test_y, predlist)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))
	fpr, tpr, thresholds = metrics.roc_curve(test_y, probs[:, 1])
	auc = metrics.auc(fpr, tpr);
	print 'auc: ', auc

	
def svm3(traincorpus, train_y, testcorpus, test_y, bucket, threshold):
	tfidf = TfidfVectorizer(analyzer='word', min_df = 0)
	print 'train_y:'
	print train_y
	traindata = tfidf.fit_transform(traincorpus)
	print len(traincorpus), traindata.shape[0], len(train_y)
	C = 1.0
	model = SVC(kernel='rbf', gamma=0.7, C=C).fit(traindata, train_y)  
	testdata = tfidf.transform(testcorpus)
	preds = model.predict(testdata)
	print model.score(testdata, test_y)
	#print confusion_matrix(preds, y_test)
	predlist = preds.tolist()
	print 'predlist:'
	print predlist
	print 'y_test:'
	print test_y
	print 'length of y_test: ', len(test_y)
	ones = [p for p in test_y if p == 1]
	twos = [p for p in test_y if p == 2]
	zeros = [p for p in test_y if p == 0]
	print '0: ', len(zeros), '1: ', len(ones), '2: ', len(twos)
	f1 =  sklearn.metrics.f1_score(test_y, predlist,average='weighted') #,pos_label=2
	recall = sklearn.metrics.recall_score(test_y, predlist,average='weighted') #,pos_label=2
	precision = sklearn.metrics.precision_score(test_y, predlist,average='weighted') #,pos_label=2
	acc = sklearn.metrics.accuracy_score(test_y, predlist)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))
	yarray = np.array(test_y)
	parray = np.array(predlist)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
	
def multinomial(train_x, train_y, test_x, test_y, bucket, threshold):
	model = MultinomialNB().fit(train_x, train_y)
	preds = model.predict(test_x)
	predlist = preds.tolist()
	f1 =  sklearn.metrics.f1_score(test_y, predlist)
	recall = sklearn.metrics.recall_score(test_y, predlist)
	precision = sklearn.metrics.precision_score(test_y, predlist)
	acc = sklearn.metrics.accuracy_score(test_y, predlist)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))

def multtinomial2(corpus, y, bucket, threshold):
	X = calc_tfidf(corpus)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
	model = MultinomialNB().fit(X_train, y_train)
	preds = model.predict(X_test)
	print model.score(X_test, y_test)
	print confusion_matrix(preds, y_test)
	predlist = preds.tolist()
	f1 =  sklearn.metrics.f1_score(y_test, predlist)
	recall = sklearn.metrics.recall_score(y_test, predlist)
	precision = sklearn.metrics.precision_score(y_test, predlist)
	acc = sklearn.metrics.accuracy_score(y_test, predlist)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))

def createinstances3(startdate, enddate, dir, features, histdays, leadtime, bucket,gap):
	date = startdate
	diff = enddate - date 
	instancelist = []
	docs = []
	y = []
	while diff.days >= 0: 
		diff = enddate - date
		bigline = ''
		for file in os.listdir(dir):
			filename = os.path.join(dir, file)
			part = filename[-19:]
			part = part[:10]
			filedate = datetime.strptime(part, '%Y-%m-%d')
			difffile = date - filedate
			if difffile.days >= leadtime and difffile.days < histdays:
				with open(filename) as f:
					for line in f:
						line = line.strip()
						if line:
							jsondata = line
							stopped_tokens = ''
							try:
								dict = json.loads(jsondata)
								for key in dict:
									if key == 'Content' or key == 'content':
										value = dict[key]
										string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
										plain_string = strip_tags(string)
										if plain_string:
											tokenizer = RegexpTokenizer(r'\w+')
											raw = plain_string.lower()
											tokens = tokenizer.tokenize(raw)
											tokens2 = [x.lower() for x in tokens if x is not None]
											stopped_tokens = [t for t in tokens2 if not t in readstops]
										if stopped_tokens:
											newtext = ' '.join([word for word in stopped_tokens])
											bigline += newtext
							except ValueError as e:
								print e, filename
								pass						
			else:
				pass
		if bigline:		
			if bucket==1:
				docs.append(bigline)
				if date in exceldict:
					val = exceldict[date]
					if val < 2:
						y.append(0)
					elif val >= 2 and val <= 3:
						y.append(1)
					else:
						y.append(2)
				else:
					y.append(0)
			else:
				docs.append(bigline)
				newdate = date
				sum = 0
				for time in range(bucket):
					if newdate in exceldict:
						val = exceldict[newdate]
						sum += val
					else:
						val = 0
						sum += val
					newdate = newdate + timedelta(days=1)
				avg = sum/bucket
				if avg < 2:
					y.append(0)
				elif avg >= 2 and avg <= 3:
					y.append(1)
				else:
					y.append(2)
		else:
			pass
		date = date + timedelta(days=gap)
		diff = enddate - date
	return docs, y
	
def main():
	read_excel()
	#features_prev = ganglist + nbhlist + entitylist1
	entityfile = 'Ncrime-entities-set1-train-172-to-301.txt' #'Ncrime-entities-set1-train-172to252-and-253toend.txt' 
	#'Ncrime-entities-set1-train-first171-172to252.txt' #Ncrime-entities-set1-train-first171
	#'Ncrime-entities-set1-train-mod.txt' #'Ncrime-entities-set1-train.txt' #'Ncrime-entities-set1-train-upto171-153toend.txt' 
	#Ncrime-entities-a2-a3-a4-train.txt #Ncrime-entities-a1train.txt
	#Ncrime-entities-a5-a6-train.txt
	#Ncrime-entities-set1-train.txt
	#tfidffile = 'tfidf_words-05-06-15.txt'
	#featurelist = read_features(featurefile)
	entitylist = read_features(entityfile)
	#tfidflist = read_tfidf(tfidffile)
	features = entitylist    #+ tfidflist #featurelist + 
	#features = featurelist
	#features = tfidflist
	#print len(features)
	#print type(features[0])
	feature_unicode = [unicode(word, 'utf-8') for word in features]
	##features = feature_unicode + ganglist + gmemlist	#+ nbhlist 
	##features = list(set(features))
	features = feature_unicode
	#trainstart = datetime.strptime('2015-05-12', '%Y-%m-%d')
	trainstart = datetime.strptime('2015-04-01', '%Y-%m-%d') #argo
	#trainend = datetime.strptime('2015-06-30', '%Y-%m-%d')
	trainend = datetime.strptime('2015-10-31', '%Y-%m-%d') #argo # 2015-10-31, 2016-01-31
	#teststart = datetime.strptime('2015-07-12', '%Y-%m-%d')
	teststart = datetime.strptime('2016-01-01', '%Y-%m-%d')  #argo # 2016-01-01, 2016-02-01
	#testend = datetime.strptime('2015-07-20', '%Y-%m-%d')
	testend = datetime.strptime('2016-05-30', '%Y-%m-%d')  #argo
	#start = datetime.strptime('2015-05-01', '%Y-%m-%d')
	#end = datetime.strptime('2015-07-31', '%Y-%m-%d')
	root = os.getcwd()
	#traindir = os.path.join(root, 'crimes-and-nocrimes05-06-bogota')
	traindir = os.path.join(root, 'a5-a6-train')    #a2-a3-a4-train, a1train, a5-a6-train, set1-train, a2-a3-a4-train1, a7train
	#testdir = os.path.join(root, 'crimes-and-nocrimes07-bogota')
	#dir = os.path.join(root, 'crimes-05-06-15') #argo: all-05-06-07-15, local: crimes-and-nocrimes05-06-bogota
	testdir = os.path.join(root, 'a5-a6-test')    #a2-a3-a4-test, a1test, a5-a6-test, set1-test, a7test
	#print dir
	histdays = 10
	leadtime = 1   # leadtime 1, bucket 4, histdays 14: 95.33
	bucket = 2
	threshold = 5
	traingap = 1
	testgap = 1
	traininst = []
	testinst = []
	traininst = createinstances(trainstart, trainend, traindir, features, histdays, leadtime, bucket, traingap)
	testinst = createinstances(teststart, testend, testdir, features, histdays, leadtime, bucket,testgap)
	#traincorpus, train_y = createinstances3(trainstart, trainend, traindir, features, histdays, leadtime, bucket,traingap)
	#testcorpus, test_y = createinstances3(teststart, testend, testdir, features, histdays, leadtime, bucket,testgap)
	#print 'traincorpus:', len(traincorpus), 'train_y:', len(train_y)
	#print 'testcorpus:',len(testcorpus),'test_y:', len(test_y)
	#print len(testinst)
	#print 'traininst:'
	#print traininst
	#print
	#print 'testinst:'
	#print testinst
	#flattrain = flat(traininst)
	#elastic(train_x, train_y, test_x, test_y, bucket, threshold)
	##svm3(traincorpus, train_y, testcorpus, test_y,bucket,threshold)
	train_x, train_y = [], []
	for instance in traininst:
		train_x.append(instance[0])
		train_y.append(int(instance[1]))
	test_x, test_y = [], []
	for instance in testinst:
		test_x.append(instance[0])
		test_y.append(int(instance[1]))
	print 'train_x', len(train_x), 'train_y:', len(train_y),'test_x:',len(test_x),'test_y:',len(test_y)
	scipy.io.savemat('area3_tr.mat', dict(a3_x_tr=train_x, a3_y_tr=train_y))
	# area3 has 136 instances, adding 19 more instances of all 0s to make it of similar size to others
	#zeros = [0] * 320
	#for i in range(43):
	#	train_x.append(zeros)
	#	train_y.append(0)
	##print 'after adding more instances: train_x', len(train_x), 'train_y:', len(train_y),'test_x:',len(test_x),'test_y:',len(test_y)
	#scipy.io.savemat('area3_tr.mat', dict(a3_x_tr=train_x, a3_y_tr=train_y))
	#print 'test_y: ', test_y
	#print 'train_y: ', train_y
	#svm2(corpus, y, bucket, threshold)
	#multtinomial2(corpus, y, bucket, threshold)
	#print 
	#print 'feature based: '
	#print
	print 'SVM:'
	svm(train_x, train_y, test_x, test_y, bucket, threshold)
	print 
	print 'Logistic:'
	logistic(train_x, train_y, test_x, test_y, bucket, threshold)
	#multinomial(train_x, train_y, test_x, test_y, bucket, threshold)
	#bayesian_ridge(train_x, train_y, test_x, test_y, bucket, threshold)
	#poisson(flattrain, test_x, test_y, features, bucket, threshold)
	#calc_cost(train_x, train_y, test_x, test_y, bucket, threshold)
	

main()
out.close()
predfile.close()