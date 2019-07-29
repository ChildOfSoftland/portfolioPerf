"""Модуль содержит класс эффективности портфеля."""

import numpy as np
import pandas as pd
import datetime

weights = pd.read_csv('weights.csv',sep=',', encoding='utf8', parse_dates=['date'], dayfirst=False, index_col='date')
prices = pd.read_csv('prices.csv',sep=',', encoding='utf8', parse_dates=['date'], dayfirst=False, index_col='date')
currencies = pd.read_csv('currencies.csv',sep=',', encoding='utf8', dayfirst=False, index_col='asset')
exchanges = pd.read_csv('exchanges.csv',sep=',', encoding='utf8', parse_dates=['date'], dayfirst=False, index_col='date')

"""Класс Производительность Портфеля."""
class PortfolioPerformance:
    """Метод вычисления производительности активов. Принимаемые данные: начальная и конечная даты"""
    def calculate_asset_performance(start_date, end_date):
        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)
        next_start_date = start_date + datetime.timedelta(days=1)                    
        
        price = prices[start_date : end_date]           
        weight = weights[next_start_date : end_date]
        
        price = price.fillna(method='pad')              
        price = price.fillna(method='bfill')
        weight = weight.fillna(method='pad')
        weight = weight.fillna(method='bfill')

        Ri = pd.DataFrame(columns = price.columns)
        P = pd.Series(1., index = pd.date_range(start_date, end_date))
        
        for i in range(len(price) - 1):                 
            Ri.loc[i] = price.apply(lambda row: (row.iloc[i+1] - row.iloc[i]) / row.iloc[i])         
        Ri.index = pd.date_range(next_start_date, end_date)
        
        Ri = Ri.mul(weight)                             
        R = Ri.sum(axis=1)

        for i in range(len(P) - 1):
            P.iloc[i+1] = P.iloc[i]*(1+R.iloc[i])

        print("Asset Performance:"+ '\n',P)
        return (P)

    """Метод вычисления производительности валют. Принимаемые данные: начальная и конечная даты"""
    def calculate_currency_performance(start_date, end_date):
        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)
        next_start_date = start_date + datetime.timedelta(days=1)

        exchange = exchanges[start_date : end_date]
        weight = weights[next_start_date : end_date]

        exchange = exchange.fillna(method='pad')
        exchange = exchange.fillna(method='bfill')
        weight = weight.fillna(method='pad')
        weight = weight.fillna(method='bfill')
        
        ex = pd.DataFrame(columns = currencies.index)
        CRi = pd.DataFrame(columns = currencies.index)
        CP = pd.Series(1., index = pd.date_range(start_date, end_date))

        for i in range(len(exchange.columns)):
            for j in range(len(currencies)):
                if ((exchange.columns[i] == currencies.iloc[j]).bool()):
                    ex.iloc[ :, j] = exchange.iloc[ :, i]

        for i in range(len(exchange) - 1):
            CRi.loc[i] = ex.apply(lambda row: (row.iloc[i+1] - row.iloc[i]) / row.iloc[i])
        CRi.index = pd.date_range(next_start_date, end_date)
        
        CRi = CRi.mul(weight)
        CR = CRi.sum(axis = 1)

        for i in range(len(CP) - 1):
            CP.iloc[i+1] = CP.iloc[i] * (1 + CR.iloc[i])

        print("Currency Performance:"+ '\n', CP)
        return (CP)

    """Метод вычисления полной производительности. Принимаемые данные: начальная и конечная даты"""
    def calculate_total_performance(start_date, end_date):
        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)
        next_start_date = start_date + datetime.timedelta(days=1)

        price = prices[start_date : end_date]
        exchange = exchanges[start_date : end_date]
        weight = weights[next_start_date : end_date]
        
        price = price.fillna(method='pad')
        price = price.fillna(method='bfill')
        exchange = exchange.fillna(method='pad')
        exchange = exchange.fillna(method='bfill')
        weight = weight.fillna(method='pad')
        weight = weight.fillna(method='bfill')

        ex = pd.DataFrame(columns = currencies.index)
        TRi = pd.DataFrame(columns = currencies.index)
        TP = pd.Series(1., index = pd.date_range(start_date, end_date))

        for i in range(len(exchange.columns)):
            for j in range(len(currencies)):
                if ((exchange.columns[i] == currencies.iloc[j]).bool()):
                    ex.iloc[ :, j] = exchange.iloc[ :, i]
        ex = ex.mul(price)

        for i in range(len(exchange) - 1):
            TRi.loc[i] = ex.apply(lambda row: (row.iloc[i+1] - row.iloc[i]) / row.iloc[i])
        TRi.index = pd.date_range(next_start_date, end_date)
        
        TRi = TRi.mul(weight)
        TR = TRi.sum(axis = 1)

        for i in range(len(TP) - 1):
            TP.iloc[i+1] = TP.iloc[i] * (1 + TR.iloc[i])

        print("Total Performance:"+ '\n', TP)
        return (TP)
