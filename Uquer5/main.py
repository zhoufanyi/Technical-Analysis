import MFMC as MC
import pandas as pd
from matplotlib import pylab

import seaborn as sns
startdate = '2008-08-11'
enddate = '2013-08-09'
GOOG = MC.MarketUniverse()
GOOG.initializeFromTickers('GOOG')
#print(AAPL.MKTUNIV)
GOOGStrategy = MC.MAStrategy(GOOG,startdate,enddate,50,120,2)
trade = GOOGStrategy.tradeRetrun()

print(trade)
pylab.figure(figsize=(12,8))
pylab.plot(GOOG.MKTUNIV.loc[startdate:enddate]['close'])
pylab.plot(GOOG.SMA('close',startdate,enddate,120))
pylab.plot(GOOG.SMA('close',startdate,enddate,50))
pylab.show()
pylab.figure(figsize=(12,8))
pylab.plot(trade[['CMarket','CStrategy']])
pylab.show()


#print(marketFactor.tickerToMarketFactorDict['NKE'])

