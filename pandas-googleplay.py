import pandas as pd
data=pd.read_csv("googleplaystore.csv")
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("==============================")
#分析遊戲評分
condition=data["Rating"]<=5
Data=data[condition]
print("遊戲評分平均數",Data["Rating"].mean())
print("遊戲評分中位數",Data["Rating"].median())
print("遊戲評分前一千個的平均數",Data["Rating"].nlargest(1000).mean())
#分析遊戲下載量
data["Installs"]=pd.to_numeric(data["Installs"].str.replace(",","").str.replace("+","").replace("Free",""))
condition=data["Installs"]>100000
print("遊戲下載量超過100000的有幾個",data[condition].shape[0])
#關鍵字搜尋應用程式
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword,case=False)
print(data[condition]["App"])

