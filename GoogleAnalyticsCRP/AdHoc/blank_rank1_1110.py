#!/usr/bin/env python2
# coding:utf-8

import pandas as pd;pd.read_csv('../input/test_v2.csv', usecols=[4,8], dtype={'fullVisitorId': 'str'}, converters={'totals': lambda t: float(dict(eval(t))['transactionRevenue']) if 'transactionRevenue' in t else 0}).groupby(['fullVisitorId'])['totals'].sum().to_frame(name='PredictedLogRevenue').apply(pd.np.log1p).to_csv('sub.csv')