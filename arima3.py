from __future__ import division
import pandas as pd
import numpy as np
import math
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import statsmodels.api as sm  
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.stattools import arma_order_select_ic
from statsmodels.tsa.seasonal import seasonal_decompose
import sklearn
from sklearn import metrics



dateparse = lambda dates: pd.datetime.strptime(dates, '%d-%m-%Y')
data = pd.read_csv('datasets/homicides-per-days-15-16.csv.csv', parse_dates=['Days'], index_col='Days',date_parser=dateparse)
# datasets/homicides-per-days-15-16.csv,datasets/homicide_per_days_area1_15_16.csv, homicide_per_days_area2_15_16
ts = data[ 'Homicides' ] 
ts = ts.astype('float64')
# the test set - July
y = ts[214:]
# fit the model on first 61 points - May and June
ts = ts[:214]

ts=ts.replace([np.inf, -np.inf], np.nan)
ts.dropna(inplace=True)

#plt.plot(ts)
#plt.show()

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):   # timeseries tutorial
    #Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=7)  #what would be a good window value?
    rolstd = pd.rolling_std(timeseries, window=7)

    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    #Perform Dickey-Fuller test:
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    #print dfoutput

#print ts	

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
	#print pred
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
			#print pred_mean, test_y_mean
			if pred_mean < 1:
				pred_result.append(0)
			elif pred_mean >= 1 and pred_mean <= 2:
				pred_result.append(1)
			else:
				pred_result.append(2)
			if test_y_mean < 1:
				test_y_result.append(0)
			elif test_y_mean >= 1 and test_y_mean <= 2:
				test_y_result.append(1)
			else:
				test_y_result.append(2)
	#print 'calculations in intensity: '
	print pred_result
	print test_y_result
	f1 =  sklearn.metrics.f1_score(test_y_result, pred_result,average='weighted') #,pos_label=2
	recall = sklearn.metrics.recall_score(test_y_result, pred_result,average='weighted') #,pos_label=2
	precision = sklearn.metrics.precision_score(test_y_result, pred_result,average='weighted') #,pos_label=2
	#roc = sklearn.metrics.roc_auc_score(test_y, predlist)
	acc = sklearn.metrics.accuracy_score(test_y_result, pred_result)
	print 'f1: ', f1, ' recall: ', recall, ' precision: ', precision, ' accuracy: ', acc
	#out.write('f1: ' + str(f1) + ' recall: '+ str(recall)+' precision: '+str(precision)+' acc: '+str(acc))
	yarray = np.array(test_y_result)
	parray = np.array(pred_result)
	yarray = np.array(test_y_result)
	parray = np.array(pred_result)
	RMSE = root_mean_squared_error(yarray, parray)
	MAE = mean_absolute_error(yarray, parray)
	print 'RMSE: ', RMSE, ' MAE: ', MAE
		
def make_string(values, returnstring):
	for v in values:
		returnstring += str(v) + ' '
	return returnstring		

#decomposition = seasonal_decompose(ts)
#trend = decomposition.trend
#seasonal = decomposition.seasonal
#residual = decomposition.resid

#---------------------------------------------------------- work on ts - seasonality ------------------------------------------------------------------------------------------ #
#ts_seasonal_diff = ts - ts.shift(7)							# very stationary
ts_seasonal_diff = ts - ts.shift(1)							# very stationary
#test_stationarity(ts_seasonal_diff.dropna(inplace=False))
ts_seasonal_first_diff = ts_seasonal_diff - ts_seasonal_diff.shift()
#test_stationarity(ts_seasonal_first_diff.dropna(inplace=False))
#ts_2nd_seasonal_diff = ts_seasonal_diff - ts_seasonal_diff.shift(7)
ts_2nd_seasonal_diff = ts_seasonal_diff - ts_seasonal_diff.shift(1)				
#test_stationarity(ts_2nd_seasonal_diff.dropna(inplace=False))
ts_first_diff = ts - ts.shift()
#test_stationarity(ts_first_diff.dropna(inplace=False))
#ts_first_seasonal_diff = ts_first_diff - ts_first_diff.shift(7)
ts_first_seasonal_diff = ts_first_diff - ts_first_diff.shift(1)

#test_stationarity(ts_first_seasonal_diff.dropna(inplace=False))


ts_seasonal_diff=ts_seasonal_diff.replace([np.inf, -np.inf], np.nan)
ts_seasonal_diff.dropna(inplace=True)


ts_seasonal_first_diff=ts_seasonal_first_diff.replace([np.inf, -np.inf], np.nan)
ts_seasonal_first_diff.dropna(inplace=True)

ts_first_seasonal_diff=ts_first_seasonal_diff.replace([np.inf, -np.inf], np.nan)
ts_first_seasonal_diff.dropna(inplace=True)

ts_2nd_seasonal_diff=ts_2nd_seasonal_diff.replace([np.inf, -np.inf], np.nan)
#ts_2nd_seasonal_diff.dropna(inplace=True)
mod_seasonal_ts = sm.tsa.statespace.SARIMAX(ts, trend='n', order = (0,0,0), seasonal_order=(3,0,1,7)) 
#mod_seasonal_ts = sm.tsa.statespace.SARIMAX(ts, trend='n', order = (0,0,0), seasonal_order=(3,0,1,1)) 
#mod_seasonal_ts = sm.tsa.statespace.SARIMAX(ts, trend='n', order = (0,0,0), seasonal_order=(1,0,0,0)) 
#mod_seasonal_ts = sm.tsa.statespace.ARIMA(ts, trend='n', order = (0,0,0)) 
results = mod_seasonal_ts.fit()  
#results.plot_diagnostics(figsize=(15, 12))  # residual is white noise - normally distributed indicating the model is satisfactory
#plt.show()
#plt.plot(ts)
#plt.plot(result.fittedvalues, color='red')  													# AIC  1710.277, BIC 1733.561
#plt.show()
#print results.summary()	


# the following forecast uses model trained on full ts, i.e., original size of 365
'''
ts_forecast = results.predict(start=175, end=364, dynamic=True)
#print ts_forecast
ts_resized = ts[175:365]
print len(ts), len(ts_forecast)
MFE = mean_forecast_err(ts_resized, ts_forecast)
MAE = mean_absolute_err(ts_resized, ts_forecast)
RMSE = mean_squared_error(ts_resized, ts_forecast)**0.5
print 'MFE: ', MFE, ' MAE: ', MAE, ' RMSE: ', RMSE
#print "MFE = ", mean_forecast_err(ts, ts_forecast)	# MFE =   0.263044377151
#print "MAE = ", mean_absolute_err(ts, ts_forecast)	# MAE =  0.104452281572 0.0824342440248
#ts_forecast_all = results.predict()

#RMSE = mean_squared_error(ts, ts_forecast)**0.5
#print 'RMSE =', RMSE	
'''
#pred_uc = results.get_forecast(steps=190)
#pred = results.get_prediction(start='23-06-2015', end='18-07-2015')
#print type(pred_uc)
#print len(ts)
#print pred_uc
#print type(pred)
#print pred
out_f = results.forecast(steps=151, exog=None, alpha=0.5, dynamic=True)
#print out_f
#print type(out_f)
outlist1 = out_f.tolist()
outlist1 = [int(t) for t in outlist1]
outlist = []
for e in outlist1:
	if e < 0:
		outlist.append(0)
	else:
		outlist.append(e)
print outlist
ylist = y.tolist()
ylist = [int(t) for t in ylist]
print ylist
ystring = ''
predstring = ''
ystring = make_string(ylist, ystring)
predstring = make_string(outlist, predstring)
predfile = open('arima_predictions.txt','a+')
predfile.truncate()
predfile.write('arima:')
predfile.write('y:\n')
predfile.write(ystring)
predfile.write('\n')
predfile.write('\npreds:\n')
predfile.write(predstring)
predfile.close()
bucket = 4
threshold = 5
intensity(bucket, threshold, outlist, ylist)
yarray = np.array(ylist)
parray = np.array(outlist)
#print type(yarray), yarray.shape
print 'Normal, outside intensity:'
RMSE = root_mean_squared_error(yarray, parray)
MAE = mean_absolute_error(yarray, parray)
print 'RMSE: ', RMSE, ' MAE: ', MAE

#print ts

#plt.plot(ts, color='blue',label='Original')
#plt.plot(ts_forecast, color='red', label='Forecast')
#plt.legend(loc='best')
#plt.title('In Sample Prediction: MFE = ' + str(mean_forecast_err(ts, ts_forecast)) + '  MAE = '+ str(MAE) + '  RMSE = ' + str(RMSE))
#plt.show()

										# RMSE =  2.53985568429 

#resid_result = results.resid
#fig = plt.figure()
#plt.title('ACF and PACF of Residuals\n')
#ax1 = fig.add_subplot(2,1,1)
#fig = sm.graphics.tsa.plot_acf(resid_result , lags=60, ax=ax1)  # residual is not independent/white noise
#ax2 = fig.add_subplot(2,1,2)
#fig = sm.graphics.tsa.plot_pacf(resid_result , lags=60, ax=ax2)  
#plt.show()

