#!/usr/bin/env python2
# coding:utf-8
import logging
logging.basicConfig(filename='example.log', filemode='w',level=logging.INFO)
ss = 100
logging.info('So should this '+str(ss))
ss = 200
logging.info('2. So should this '+str(ss))
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
