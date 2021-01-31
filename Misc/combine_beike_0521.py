#utf-8
import pandas as pd
import glob

# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/sz/20200521"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/sz/20200524"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/sz/20200620"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/sz/20200629"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/cd/20200521"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/gz/20200521"
# val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/sz/20210106"
val_p = "/Users/jamesliao2018/GIT/lianjia-beike-spider/data/ke/xiaoqu/gz/20210124"
all_files = glob.glob(val_p + "/*.csv")

li = []

for filename in all_files:
    print(filename)
    try:
        df = pd.read_csv(filename, header=None,encoding="utf-8")
        df.columns=['date','district','street','estate','price','quantity']
        df = df[df.quantity!="0套在售二手房"]
        df = df[df.price!="暂无"]
        df['p2'] = df['price'].apply(lambda x: x[:-4])
        df['num2'] = df['quantity'].apply(lambda x: x[:-6])
        li.append(df)
    except:
        print(filename)

print(len(li))

frame = pd.concat(li, axis=0, ignore_index=True)

frame.columns = ['日期','城区','街道','小区','均价','数量','均价平方','在售数量']
# frame.to_csv("beike_scrape_0521_cd.csv",index=False,encoding="gb18030")
# frame.to_csv("beike_scrape_0521_gz.csv",index=False,encoding="gb18030")
# frame.to_csv("beike_scrape_0524_sz.csv",index=False,encoding="gb18030")
# frame.to_csv("beike_scrape_0620_sz.csv",index=False,encoding="gb18030")
# frame.to_csv("beike_scrape_20210106_sz.csv",index=False,encoding="gb18030")
frame.to_csv("beike_scrape_20210124_gz.csv",index=False,encoding="gb18030")
