
# coding: utf-8

# In[1]:


import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.io.json import json_normalize
import lightgbm as lgb
from sklearn.model_selection import KFold
import time
from datetime import datetime
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error


# # Read The Training Data

# In[2]:
from datetime import datetime, timedelta

now = datetime.now()
current_date = str(now)[:10]


df_raw = pd.read_csv('/Users/liaopeng3/.kaggle/train.csv',
                    dtype={'date': str, 'fullVisitorId': str, 'sessionId':str}, nrows=None)
df_test_raw = pd.read_csv('/Users/liaopeng3/.kaggle/test.csv',
                   dtype={'date': str, 'fullVisitorId': str, 'sessionId':str}, nrows=None)
df_raw.shape, df_test_raw.shape


# # Read the Test Data

# In[3]:


df_train = df_raw.copy()


# In[4]:


df_train.columns


# In[5]:


df_test_tmp = df_train.drop_duplicates('fullVisitorId')


# In[6]:


df_test_tmp_join = df_test_tmp.merge(df_test_raw,on='fullVisitorId',how='inner')


# In[7]:


df_test_tmp_join.shape


# # Concatenate the Training and Test Dat

# In[24]:


df_train.columns.difference(df_test_raw.columns)


# In[25]:


df_test_raw.columns.difference(df_train.columns)


# In[26]:


df3 = pd.concat([df_train.drop(['totals.transactionRevenue'],axis=1),df_test_raw],ignore_index=True) 


# In[27]:


df_train.shape


# In[28]:


len_df_train = df_train.shape[0]


# # Split Feature and Label Data

# In[29]:


train_y = df_train['totals.transactionRevenue'].fillna(0).astype(float).apply(lambda x: np.log1p(x))


# # Add Visit Time

# In[30]:


df3['diff_visitId_time'] = df3['visitId'] - df3['visitStartTime']
df3['diff_visitId_time'] = (df3['diff_visitId_time'] != 0).astype(int)


# # Format the Numerous Variables

# In[31]:


list_v = ['totals.hits','totals.pageviews']


# In[32]:


for cols in list_v:
    df3[cols]=df3[cols].astype(float)
    df3[cols]=(df3[cols] - min(df3[cols])) / (max(df3[cols] - min(df3[cols])))

# ##  Drop the Constant Columns

# In[33]:


cols_drop = []
for cols in df3.columns:
    if df3[cols].nunique()==1:
#         print(cols)
        cols_drop.append(cols)
        
df3 = df3.drop(cols_drop,axis=1)


# # Convert Date to Numeric Variables

# In[35]:


format_str = '%Y%m%d' 
df3['date'] = df3['date'].apply(lambda x: datetime.strptime(str(x), format_str))


# In[36]:


df3['date_dayofweek'] = df3['date'].dt.dayofweek
df3['date_year'] = df3['date'].dt.year

df3['date_hour'] = df3['date'].dt.hour

df3['date_month'] = df3['date'].dt.month
df3['date_day'] = df3['date'].dt.day

df3['date_month'] = df3['date'].apply(lambda x:x.month)
df3['date_quarter_month'] = df3['date'].apply(lambda x:x.day//8)
df3['date_weekday'] = df3['date'].apply(lambda x:x.weekday())



# # Visit Time

# In[48]:


df3['visitStartTime'] = df3['visitStartTime'].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)))

df3['visitStartTime'] = pd.to_datetime(df3['visitStartTime'])

df3['quarter_month'] = df3['visitStartTime'].apply(lambda x:x.day//8)

# df3.loc[1020:1025,['visitStartTime','quarter_month']]

df3['quarter_month'].value_counts()

df3['day_month'] = df3['visitStartTime'].apply(lambda x:x.day)


# df3['day_month'].value_counts()

df3['WoY'] = df3['visitStartTime'].apply(lambda x: x.isocalendar()[1])

# df3['WoY'].value_counts()

df3['visit_dayofweek'] = df3['visitStartTime'].dt.dayofweek
df3['visit_year'] = df3['visitStartTime'].dt.year

df3['visit_month'] = df3['visitStartTime'].dt.month
df3['visit_day'] = df3['visitStartTime'].dt.day
df3['visit_hour'] = df3['visitStartTime'].dt.hour


# In[50]:


# df['vis_date'] = pd.to_datetime(df['visitStartTime'], unit='s')
# df['sess_date_dow'] = df['vis_date'].dt.dayofweek
# df['sess_date_hours'] = df['vis_date'].dt.hour
# df['sess_date_dom'] = df['vis_date'].dt.day
# df.sort_values(['fullVisitorId', 'vis_date'], ascending=True, inplace=True)
df3['next_session_1'] = (df3['visitStartTime'] - df3[['fullVisitorId', 'visitStartTime']].groupby('fullVisitorId')['visitStartTime']                         .shift(1)).astype(np.int64) // 1e9 // 60 // 60
df3['next_session_2'] = (df3['visitStartTime'] - df3[['fullVisitorId', 'visitStartTime']].groupby('fullVisitorId')['visitStartTime']                         .shift(-1)).astype(np.int64) // 1e9 // 60 // 60

df3['nb_pageviews'] = df3['date'].map(
    df3[['date', 'totals.pageviews']].groupby('date')['totals.pageviews'].sum()
)

df3['ratio_pageviews'] = df3['totals.pageviews'] / df3['nb_pageviews']


# In[ ]:


df3 = df3.drop('visitStartTime',axis=1)

df3 = df3.drop('date',axis=1)


# # Convert the Object Values to Numeric

for cols in df3.columns:
    if df3[cols].dtypes == object or df3[cols].dtypes== bool:
#         df3[cols] = df3[cols].astype('category')
#         df3["new_"+cols] = df3[cols].cat.codes
        df3["new_"+cols] = pd.factorize( df3[cols])[0]
        df3 = df3.drop(cols,axis=1)
        df3 = df3.rename(columns={"new_"+cols:cols})


# # Clean the Data Again

# ##  Drop the Constant Columns

cols_drop = []
for cols in df3.columns:
    if df3[cols].nunique()==1:
#         print(cols)
        cols_drop.append(cols)
        
df3 = df3.drop(cols_drop,axis=1)


# # Baseline Model

# # Split Feature and Label Data

train_x = df3[:len_df_train]


test_x = df3[len_df_train:]


# # Training Model

param = {'num_leaves': 300,
         'min_data_in_leaf': 30, 
         'objective':'regression',
         'max_depth': -1,
         'learning_rate': 0.005,
         "min_child_samples": 20,
         'boosting_type' : 'gbdt',
         "feature_fraction": 0.9,
         "bagging_freq": 1,
         "bagging_fraction": 0.8 ,
         "bagging_seed": 11,
         "metric": 'rmse',
         "lambda_l1": 1,
         "verbosity": -1}

folds = KFold(n_splits=5, shuffle=True, random_state=15)
oof = np.zeros(len(train_x))
predictions = np.zeros(len(test_x))
start = time.time()
features = list(train_x.columns)
feature_importance_df = pd.DataFrame()

for fold_, (trn_idx, val_idx) in enumerate(folds.split(train_x.values, train_y.values)):
    trn_data = lgb.Dataset(train_x.iloc[trn_idx].values, label=train_y.iloc[trn_idx].values)
    val_data = lgb.Dataset(train_x.iloc[val_idx].values, label=train_y.iloc[val_idx].values)
    
    num_round = 10000
    clf = lgb.train(param, trn_data, num_round, valid_sets = [trn_data, val_data], verbose_eval=100, early_stopping_rounds = 100)
    oof[val_idx] = clf.predict(train_x.iloc[val_idx].values, num_iteration=clf.best_iteration)
    
    fold_importance_df = pd.DataFrame()
    fold_importance_df["feature"] = features
    fold_importance_df["importance"] = clf.feature_importance()
    fold_importance_df["fold"] = fold_ + 1
    feature_importance_df = pd.concat([feature_importance_df, fold_importance_df], axis=0)
    
    predictions += clf.predict(test_x.values, num_iteration=clf.best_iteration) / folds.n_splits

print("CV score: {:<8.5f}".format(mean_squared_error(oof, train_y)**0.5))


# GBDT: CV score:  1.59052 ,
# RF: CV score: 1.64722, 
# DART: CV score: 1.63164 

cols = feature_importance_df[["feature", "importance"]].groupby("feature").mean().sort_values(
    by="importance", ascending=False)[:1000].index

best_features = feature_importance_df.loc[feature_importance_df.feature.isin(cols)]

plt.figure(figsize=(14,10))
sns.barplot(x="importance", y="feature", data=best_features.sort_values(by="importance", ascending=False))
plt.title('LightGBM Features (avg over folds)')
plt.tight_layout()
plt.savefig(current_date+'_lgbm_importances.png')


submission = df_test_raw[['fullVisitorId']].copy()

submission.loc[:, 'PredictedLogRevenue'] = predictions
submission.loc[:, 'PredictedLogRevenue'] = np.expm1(predictions)
grouped_test = submission[['fullVisitorId', 'PredictedLogRevenue']].groupby('fullVisitorId').sum().reset_index()
grouped_test["PredictedLogRevenue"] = np.log1p(grouped_test["PredictedLogRevenue"])
grouped_test["PredictedLogRevenue"] =  grouped_test["PredictedLogRevenue"].apply(lambda x : 0.0 if x < 0 else x)
grouped_test['fullVisitorId']=grouped_test['fullVisitorId'].astype('str')
grouped_test.to_csv(current_date+'_mySubmit_gbdt.csv',index=False)

