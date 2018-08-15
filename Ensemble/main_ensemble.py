import glob
import pandas as pd
import numpy as np

# USING WEIGHTED AVERAGE RANK METHOD
# Plese refer this discussion for more detials - https://www.kaggle.com/c/home-credit-default-risk/discussion/60934

data = {}

dir1 = '/Users/liaopeng3/code_lib/HCDR2018/Ensemble/'

for path in glob.glob(dir1+"homecredt/*.csv", recursive=True):
    data[path[len(dir1) + 10:-4]] = pd.read_csv(path)

ranks = pd.DataFrame(columns=data.keys())
for key in data.keys():
    ranks[key] = data[key].TARGET.rank(method='min')
ranks['Average'] = ranks.mean(axis=1)
ranks['Scaled Rank'] = (ranks['Average'] - ranks['Average'].min()) / (ranks['Average'].max() - ranks['Average'].min())
ranks.corr()[:1]

weights = [0.1, 0.4, 0.0, 0.0, 0.0, 0.4 , 0.05,0.05]
ranks['Score'] = ranks[['submission_kernel02_other_2', 'tidy_xgb_0.78847', 'submission', 'submission_1','hybridII', 'submission_kernel02', 'submission_kernel02_other','submission_with selected_features']].mul(weights).sum(1) / ranks.shape[0]
submission_lb = pd.read_csv(dir1+"homecredt/submission.csv")
submission_lb['TARGET'] = ranks['Score']
submission_lb.to_csv("WEIGHT_AVERAGE_RANK.csv", index=None)
submission_lb.head()
## WARNING THIS METHOD IS PRONE TO OVERFITTING..

