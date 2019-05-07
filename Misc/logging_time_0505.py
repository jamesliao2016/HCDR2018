#!/usr/bin/env python2
# coding:utf-8
import logging
import time
import datetime
# start_time = time.time()

logging.basicConfig(filename='example.log', filemode='w',level=logging.INFO)
# logging.info('Start time is: '+str(datetime.datetime.now()))
start_time = datetime.datetime.now()
logging.info('Start time is: '+str(start_time))
ss = 100
logging.info('So should this '+str(ss))
ss = 200
logging.info('2. So should this '+str(ss))
logging.debug('This message should go to the log file')

for i in range(10):
    j = i*i

end_time = datetime.datetime.now()
logging.info('running time is: '+str((end_time - start_time).seconds))
logging.info('Current time is: '+str(end_time))
# logging.info('So should this')

# logging.warning('And this, too')

'''
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

'''