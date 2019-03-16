# -*- coding: utf-8 -*-
from __future__ import division
import csv
import json
#import simplejson  # simplejson provides more descriptive error message
import os
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import ElasticNetCV
import pandas as pd
import numpy as np
import scipy.io
from datetime import datetime, timedelta 
import math
from sklearn.metrics import f1_score, precision_recall_fscore_support
from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge
from sklearn import preprocessing
import statsmodels.formula.api as smf

ganglist1 = ['Los Angelitos','ERPAC','Gaitanistas','La Oficina de Envigado','Nueva Generación', 'Los Magníficos','Aguilas Negras','Black Eagles','AUC','United Self-Defense Forces of Colombia','Autodefensas Unidas de Colombia','Nueva Orteguaza','Autodefensas Gaitanistas de Colombia','Ejército Popular de Liberación','EPL','Clan del Golfo','Águilas Negras', 'Los Norteños El Parche', 'Los Tesos', 'Los Yiyos', 'Los Mongolitos', 'Los Jíbaros', 'Los Chamizo', 'Los Chamos','Los Vacasen','La Banda del Negro Orlando','Los Kits Los Daza','Los Paisas','Los Pájaros','El Turco','El Zarco','El Monedita','El Mono','Los Simpson','Los Monsalve','Los Parrado','Los Peluzas','Los Moros','Los Gomelos','Los Rusos','Los Destroyers','Los Nicos','Los Monos','Los Navajas','Los Cucarachos','Los Magníficos','Los Choquis','Los Pitufos','El Caballo','El Beto','Los Nazi','El Coronel','Libertadores del Vichada','Oficina de Envigado','El Flaco','Los Calvos','El Jinete','El Parche','Los Velozas','Los Vampiros','Los Cucarrones','Los Chéveres','Los Cocos','Los Rapados','Los Zepelines','Los Zorreros','Los Galletas','Los Gomelos','Los Puntilleros','Meta Bloc','Puntilla','Los Bollos','Los Daza','AGC','Clan Usuga','Urabeños','Clan del Golfo','Rastrojos','Los Chachos','Los Rapados','Los Norteños','Los Gusanos','Los Canecos','Los Tigres','Los Pablos','Los Paisas','El Caleño','Banda del Gallina','Los Tacheros-Emboladores','bacrim','Otoniel','Black Eagles','Las Águilas Negras',' Úsuga','Bloque Meta',' Los Machos','Renacer','Los Gaitanistas','Nueva Generación','Libertadores del Vichada','The Office of Envigado','Los Urabeños','Pandillas en Santa Isabel','Galán','Santa Matilde y Salazar Gómez','Pandillas en El Guavio','Los Laches y El Consuelo','Los Camellos','Los Chávez','Los Gatos','Los Diablos','Los Crespos','Los Camiones Chapulín','Los Romilocos','El Enano','Los Pecas','Los N.Ns','Los Motas','El Memín','El Vaca Juanito','La 59','La Pulga','El Zapatero Milthon','Los Brothers','Los Memos','Los Kikos']
nbhlist1 = ['Usaquén','Chapinero', 'Santafé','San Cristobal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','los Mártires','Antonio Nariño','Puente Aranda','La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar']	
ldlist1 = ['Paseo los libertadores','Las ferias','El Refugio','Sagrado Corazón','San Blas','Verbenal','Minuto de Dios','San Isidro','La Macarena','Sosiego','La Uribe','Boyacá Real','Prdo Rubio','Las Nieves','20 de Julio','San Cristóbal','Santa Cecilia','Chico Lago','Las Cruces','Gloria','Toberín','Bolivia','Chapinero','Lourdes','Los Libertadores','Los Cedros','Garcés Navas','Usaquén','Engativa','Country Club','Jardín Botánico','Santa Bárbara','Alamos','La Flora','Venecia','Fontibón','Apogeo','Santa Isabel','Danubio','Tunjuelito','Fontibón San Pablo','Bosa occidental','La Sabana','Gran Yomasa','Zona Franca','Bosa central','Comuneros','Ciudad Salitre occidente','El Porvenir','Alfonso López','Granjas de techo','Tintal Sur','Parque Entrenubes','Modelia','Ciudad Usme','Capellanía','Aeropuerto El Dorado','Castilla','La Academia','Los Andes','Galenas','Ciudad Jardín','Américas','Guaymaral','Doce de Octubre','Teusaquillo','Restrepo','Carvajal','San José de Bavaria','Los Alcázares','Parque Simón Bolívar','Kennedy Central','Britalia','Parque Salitre','La Esmeralda','Timiza','El Prado','Quinta Paredes','Tintal Norte','La Alhambra','Ciudad Salitre Oriental','Calandaima','Casa Blanca Suba','Corabastos','Niza','Gran Britalia','La Floresta','Patio Bonito','Suba','Las Margaritas','El Rincón','Bavaria','Tibabuyes','Ciudad Montes','La Candelaria','San José','El Mochuelo','Muzú','Quiroga','Monteblanco','San Rafael','Marco Fidel Suárez','Arborizadota','Zona Industrial','Marruecos','San Francisco','Puente Aranda','Diana Turbay','Lucero','El Tesoro','Ismael Perdomo','Jerusalem','Usaquén','Chapinero','Santa Fe','San Cristóbal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','Los Mártires','Antonio Nariño','Puente Aranda',' 	La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar','Sumapaz']
gmemlist1 = ['Vicente Castaño',' Ramón Navarro Serrano','Megateo', 'Ivan Marquez','Luis Enrique Calle Serna','Octavio Orrego','Sebastián','Carlos Andres Bustos Cortez','Jairo Alirio Puerta Peña','Cuñado','Omar', 'El Paisa', 'Rastrojos', 'Simon Trinidad','Puntilla','Tanja Nijmeijer', 'ERPAC', 'Don Berna','Don Mario','Pablo Beltran','Pastor Alape','Joaquin Gomez','Otoniel','Urabeños', "Daniel 'El Loco' Barrera", 'Fabian Ramirez','EPL','Los Pelusos','Aguilas Negras','Libertadores de Vichada','AGC','Gaitanista Self-Defense Forces of Colombia','Paisas','FIAC','Megateo','Salvatore Mancuso','Romaña','Oficina de Envigado','Pablo Escobar','Franco Jiménez','German','Nicolas Rodriguez Bautista','Gabino','Eliecer Erlinto Chamorro','Antonio Garcia','Miguel Ángel Alfaro','Dámaso López Núñez','Luciano Marin Arango','Ivan Marquez','Cesarin','Roberto Vargas Gutierrez','Gavilan','Fredy Alonzo Mira Perez','Fredy Colas','Licenciado','Jorge 40','Movil 7','Timochenko','Pablito','Abimel Coneo Martínez','Torta','Carlos Marin Guarin','Antonio Garcia','Pablo Beltrán','Gabino','Calle Serna','Pijarbey','Martin Farfan Diaz Gonzalez','Comba','Otoniel','Martín Farfán Díaz González','Pijarbey','Díaz González','Dairo Antonio Úsuga David','Mao','Guillermo Alejandro','Dario Antonio Usuga','Raul Jaramillo','Abeja','Efrain Guzman',' Nariño','Iván Marquéz','Mauricio Jaramillo','El Médico','Pablo Catatumbo','Timoleón Jiménez','Juaquin Gomez','Blanco','Escobar','Orejuela','Úsuga']
newnbh = ['Antioquia','Meta','Envigado','Arauca','Guaviare','Vichada','Valle del Cauca','Sucre','Cqueta','Huila','Putumayo','Quindio','Risaralda','Tolima','Boyaca','Santander','Norte de Santander','Buenaventura','Magdalena','Caquetá','Vichada','Guaviare','Casanare','Uraba','Cordoba','Guajira','Bolivar','Sucre','Cesar','Cauca','Chocó','Tumaco','Nariño']
nbhlist2 = nbhlist1 + ldlist1

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

#df = pd.read_csv("F:\Anaconda\homicide\datasets\homicide_count_2015_06_06_Bogota.csv")
#df['date'] = pd.to_datetime(df['date'], format = )
out = open('elastic-outputs.txt', 'a+')
out.truncate()
out.write('Outputs from Elastic4.py\n')

predfile = open('predictions.txt', 'a+')
predfile.truncate()

exceldict = {}
def read_excel():
	root = os.getcwd()
	file = 'homicide_count_area3_15_16.csv'	#homicide_count_area3_15_16.csv #homicide_count_area1_15_16.csv
	#file = 'F:\Anaconda\homicide\datasets\homicide_count_2015_05_06_07_Bogota.csv'  #homicide_2015_muni_date_homicidios_3.csv
	#filename = os.path.join(root, file)
	with open(file) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			datestring = row[0]
			count = int(row[1])
			dateval = datetime.strptime(datestring, '%d/%m/%Y')
			if dateval in exceldict:
				exceldict[dateval] += count
			else:
				exceldict[dateval] = count

def createinstances(startdate, enddate, dir, features, histdays, leadtime, bucket,gap):
	date = startdate
	diff = enddate - date 
	instancelist = []
	while diff.days >= 0:
		diff = enddate - date
		count = 0
		featuredict = {}
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
		ins = []
		if count > 0:
			for feature in features:
				ins.append(int(featuredict[feature]))
			if date in exceldict:
				tuple = (ins, exceldict[date])
				instancelist.append(tuple)
			else:
				tuple = (ins, 0)
				instancelist.append(tuple)	
		else:
			pass
		date = date + timedelta(days=gap)
		diff = enddate - date
	return instancelist

def mean_absolute_error(y, pred):
	return np.mean(abs(y-pred))
def root_mean_squared_error(y, pred):
	return math.sqrt(np.mean((y-pred)**2))
	
def calc_accuracy(predicted, ytest_dat):
	success = 0
	for i in range(len(ytest_dat)):
		if ytest_dat[i] == predicted[i]:
			success += 1
	accuracy = (success/len(predicted)) * 100
	return accuracy

def intensity(bucket, threshold, pred, test_y):
	pred_result = []
	test_y_result = []
	for i in range(len(pred)):
		temp1 = pred[i:i+bucket]
		temp2 = test_y[i:i+bucket]
		if len(temp1) < bucket:
			pass
		else:
			pred_mean = np.mean(temp1)
			test_y_mean = np.mean(temp2)
			if pred_mean < threshold:
				pred_result.append(0)
			else:
				pred_result.append(1)
			if test_y_mean < threshold:
				test_y_result.append(0)
			else:
				test_y_result.append(1)
	print pred_result
	print test_y_result
	print 'precision, recall: '
	prs =  precision_recall_fscore_support(test_y_result, pred_result,  average='binary', pos_label=1) # pos_label=0
	precision = prs[0]
	recall = prs[1]
	out.write('precision: ' + str(precision) + ' recall: ' + str(recall) + '\n')
	print 'f1 score: '
	f1 =  f1_score(test_y_result, pred_result,  average='binary', pos_label=1 )  #pos_label=0
	print f1
	print 'f1 score: ', f1
	out.write('f1 score: ' + str(f1) + '\n')
	acc = calc_accuracy(pred_result, test_y_result)
	print 'intensity accuracy: ', acc
	out.write('intensity accuracy: ' + str(acc) + '\n')
	
def preprocess(train_x, test_x):
	scaled = preprocessing.MinMaxScaler()
	x_train = scaled.fit_transform(train_x)
	x_test = scaled.transform(test_x)
	print x_train.shape, type(x_train)
	return x_train, x_test
	
def make_string(values, returnstring):
	for v in values:
		returnstring += str(v) + ','
	return returnstring
	
def poisson(train, test, y_test, features, bucket, threshold):
	length = len(features)
	count = 0
	newfeatures = []
	formula = ''
	for i in range(length):
		n = count
		feat = 'f'+str(n)
		newfeatures.append(feat)
		formula += feat + ' + '
		count += 1
	testfeatures = newfeatures
	testframe = pd.DataFrame(test, columns=testfeatures)
	trainfeatures = newfeatures
	trainfeatures.append('y')
	trainframe = pd.DataFrame(train, columns = trainfeatures)
	formula = formula[:-3]
	formula = 'y ~ ' + formula
	model = smf.poisson(formula, data=trainframe).fit(method='bfgs')
	pred = model.predict(testframe)
	predlist = pred.tolist()
	predlist = [int(p) for p in predlist]
	print predlist
	print y_test
	ystring = ''
	predstring = ''
	ystring = make_string(y_test, ystring)
	predstring = make_string(predlist, predstring)
	predfile.write('poisson:')
	predfile.write('y:\n')
	predfile.write(ystring)
	predfile.write('\n')
	predfile.write('\npreds:\n')
	predfile.write(predstring)	

def bayesian_ridge(train_x, train_y, test_x, test_y, bucket, threshold):
	br = BayesianRidge(normalize=True,compute_score=True,n_iter=1000)
	model = br.fit(train_x, train_y)
	train_y = [float(t) for t in train_y]
	test_y = [float(t) for t in test_y]	
	pred = model.predict(test_x)
	pred = [math.ceil(p) for p in pred]
	print 'test_y:'
	print test_y
	print 
	print 'predictions:'
	print pred
	ystring = ''
	predstring = ''
	ystring = make_string(test_y, ystring)
	predstring = make_string(pred, predstring)
	predfile.write('Bayesian Ridge:')
	predfile.write('y:\n')
	predfile.write(ystring)
	predfile.write('\n')
	predfile.write('\npreds:\n')
	predfile.write(predstring)
	test_acc = calc_accuracy(pred, test_y)
	print 'test_y mean: ', np.mean(test_y)
	print 'test accuracy:', test_acc
	out.write('test accuracy: ' + str(test_acc) + '\n')
	yarray = np.array(test_y)
	parray = np.array(pred)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
	str_rmse = str(RMSE)
	str_MAE = str(MAE)
	out.write('RMSE: ' + str_rmse + ' MAE: ' + str_MAE + '\n')

	
def svr(train_x, train_y, test_x, test_y, bucket, threshold):
	svr = SVR(C=0.8, epsilon=0.2)	
	model = svr.fit(train_x, train_y)
	train_y = [float(t) for t in train_y]
	test_y = [float(t) for t in test_y]	
	pred = model.predict(test_x)
	pred = [math.ceil(p) for p in pred]
	print 'test_y:'
	print test_y
	print 
	print 'predictions:'
	print pred
	ystring = ''
	predstring = ''
	ystring = make_string(test_y, ystring)
	predstring = make_string(pred, predstring)
	predfile.write('SVR:')
	predfile.write('y:\n')
	predfile.write(ystring)
	predfile.write('\n')
	predfile.write('\npreds:\n')
	predfile.write(predstring)
	test_acc = calc_accuracy(pred, test_y)
	print 'test_y mean: ', np.mean(test_y)
	print 'test accuracy:', test_acc
	out.write('test accuracy: ' + str(test_acc) + '\n')
	yarray = np.array(test_y)
	parray = np.array(pred)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
	str_rmse = str(RMSE)
	str_MAE = str(MAE)
	out.write('SVR:'+'RMSE: ' + str_rmse + ' MAE: ' + str_MAE + '\n')
		
def find_alpha(train_x, train_y):
	alphas = np.logspace(-5, 1, 60)
	length = len(train_x)
	tr = int(length*0.8)
	ts = int(length*0.2)
	tr_x = train_x[:tr]
	ts_x = train_x[tr:]
	tr_y = train_y[:tr]
	ts_y = train_y[tr:]
	print 'train: ', len(tr_x), len(tr_y)
	print 'test: ', len(ts_x), len(ts_y)
	train_errors = list()			# l1:0.1 alpha: 0.186718109129, l1:0.2 alpha: 0.14773776526, l1:0.3 alpha: 0.0924914727722, l1:0.6 alpha = 0.0731824221908 
	test_errors = list()			# l1:0.4 alpha: 0.0924914727722,l1:0.5 alpha: 0.0731824221908,l1:0.7 alpha:  0.057904439806,l1:0.8 alpha:  0.057904439806
	model = ElasticNet(l1_ratio=0.6, max_iter=10000, normalize=True)  # l1:0.9 alpha: 0.057904439806
	for alpha in alphas:
		model.set_params(alpha=alpha)
		model.fit(tr_x, tr_y)
		train_errors.append(model.score(tr_x, tr_y))
		test_errors.append(model.score(ts_x, ts_y))

	i_alpha_optim = np.argmax(test_errors)
	alpha_optim = alphas[i_alpha_optim]
	print "Optimal regularization parameter : %s",  alpha_optim
	out.write('alpha-optim: ' + str(alpha_optim) + '\n')
	return alpha_optim
	
	
def elastic(train_x, train_y, test_x, test_y, bucket, threshold):
	print 'train_y:'
	print train_y
	#alphas = np.logspace(-5, 1, 60)
	penalties = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
	alpha = 0.001
	alpha_optim = find_alpha(train_x, train_y)
	elastic = ElasticNet(alpha=alpha_optim, l1_ratio=0.6, max_iter=10000, normalize=True) # l1_ratio: 0.6 gives three different numbers
	#model = ElasticNetCV(l1_ratio=penalties,normalize=True,max_iter=10000,cv=None)
	#model = linear_model.LinearRegression()
	train_y = [float(t) for t in train_y]
	test_y = [float(t) for t in test_y]
	model = elastic.fit(train_x, train_y)
	train_acc = model.score(train_x, train_y)
	print 'train accuracy: ', train_acc*100
	print 'train_y mean: ', np.mean(train_y)
	pred = model.predict(test_x)
	pred = [math.ceil(p) for p in pred]
	print 'test_y:'
	print test_y
	print 
	print 'predictions:'
	print 'length of y_test: ', len(test_y)
	ones = [p for p in test_y if p == 1]
	twos = [p for p in test_y if p == 2]
	zeros = [p for p in test_y if p == 0]
	print '0: ', len(zeros), '1: ', len(ones), '2: ', len(twos)
	ystring = ''
	predstring = ''
	ystring = make_string(test_y, ystring)
	predstring = make_string(pred, predstring)
	predfile.write('ElasticNet:')
	predfile.write('y:\n')
	predfile.write(ystring)
	predfile.write('\n')
	predfile.write('\npreds:\n')
	predfile.write(predstring)
	test_acc = calc_accuracy(pred, test_y)
	print 'test_y mean: ', np.mean(test_y)
	print 'test accuracy:', test_acc
	out.write('test accuracy: ' + str(test_acc) + '\n')
	yarray = np.array(test_y)
	parray = np.array(pred)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
	str_rmse = str(RMSE)
	str_MAE = str(MAE)
	out.write('Elastic'+'RMSE: ' + str_rmse + ' MAE: ' + str_MAE + '\n')
	
	
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
		
def flat(inst):
	flattened = []
	for ins in inst:
		ins1 = ins[0]
		ins2 = ins[1]
		ins1.append(ins2)
		flattened.append(ins1)
	return flattened
	
def main():
	read_excel()
	#features_prev = ganglist + nbhlist + entitylist1
	#print type(features_prev[0])
	#featurefile = 'features-precursors10.txt'
	entityfile = 'Ncrime-entities-set1-train-172-to-301.txt'
	#Ncrime-entities-a2-a3-a4-train.txt #Ncrime-entities-a5-a6-train.txt#Ncrime-entities-a1train.txt
	#Ncrime-entities-set1-train.txt
	##tfidffile = 'tfidf_words-05-06-15.txt'
	#featurelist = read_features(featurefile)
	entitylist = read_features(entityfile)
	#tfidflist = read_tfidf(tfidffile)
	features = entitylist #+ tfidflist #featurelist + 
	#features = featurelist
	#features = tfidflist
	#print len(features)
	#print type(features[0])
	feature_unicode = [unicode(word, 'utf-8') for word in features]
	##features = feature_unicode + ganglist + gmemlist  #+ nbhlist 
	##features = list(set(features))
	features = feature_unicode
	#print len(features)
	#print type(features[0])
	#trainstart = datetime.strptime('2015-05-12', '%Y-%m-%d')
	trainstart = datetime.strptime('2015-04-01', '%Y-%m-%d') #argo
	#trainend = datetime.strptime('2015-06-30', '%Y-%m-%d')
	trainend = datetime.strptime('2015-10-31', '%Y-%m-%d') #argo
	#teststart = datetime.strptime('2015-07-12', '%Y-%m-%d')
	teststart = datetime.strptime('2016-01-01', '%Y-%m-%d')  #argo
	#testend = datetime.strptime('2015-07-20', '%Y-%m-%d')
	testend = datetime.strptime('2016-05-30', '%Y-%m-%d')  #argo
	root = os.getcwd()
	#traindir = os.path.join(root, 'crimes-and-nocrimes05-06-bogota')
	traindir = os.path.join(root, 'a5-a6-train')    #a2-a3-a4-train, a5-a6-train, a1train, set1-train, a7train
	#testdir = os.path.join(root, 'crimes-and-nocrimes07-bogota')
	testdir = os.path.join(root, 'a5-a6-test')    #a5-a6-test, a1test, set1-test, a2-a3-a4-test, a7test
	#print dir
	histdays = 5
	leadtime = 1   # leadtime 1, bucket 4, histdays 14: 95.33
	bucket = 2
	traingap = 1
	testgap = 1
	threshold = 5
	traininst = []
	testinst = []
	traininst = createinstances(trainstart, trainend, traindir, features, histdays, leadtime, bucket, traingap)
	testinst = createinstances(teststart, testend, testdir, features, histdays, leadtime, bucket, testgap)
	train_x, train_y = [], []
	for instance in traininst:
		train_x.append(instance[0])
		train_y.append(int(instance[1]))
	test_x, test_y = [], []
	for instance in testinst:
		test_x.append(instance[0])
		test_y.append(int(instance[1]))
	print 'train_x', len(train_x), 'train_y:', len(train_y),'test_x:',len(test_x),'test_y:',len(test_y)
	#scipy.io.savemat('area1reg_te.mat', dict(a1reg_x_te=test_x, a1reg_y_te=test_y))
	##print 'Elastic:'
	##elastic(train_x, train_y, test_x, test_y, bucket, threshold)
	print 'SVR:'
	svr(train_x, train_y, test_x, test_y, bucket, threshold)
	##print 'Bayesian Ridge:'
	##bayesian_ridge(train_x, train_y, test_x, test_y, bucket, threshold)
	#print 'Poisson:'
	#flattrain = flat(traininst)
	#poisson(flattrain, test_x, test_y, features, bucket, threshold)
	#calc_cost(train_x, train_y, test_x, test_y, bucket, threshold)
	

main()
out.close()
predfile.close()