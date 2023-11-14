import pandas as pd
df1=pd.read_csv("D:\\projects\\olddatatset\\phishing_site_urls.csv")
print("df1")
print(df1.shape)
print(df1.columns)
df2=pd.read_csv("D:\\projects\\dataset_phishing.csv")
df2=df2.iloc[:,[0,88]]
print("df2")
print(df2.shape)
print(df2.columns)

df1.rename(columns={'URL':'url','Label':'status'},inplace=True)
print('renamed df1 columns',df1.columns)

df1.status[df1.status=='bad']=1
df1.status[df1.status=='good']=0
df2.status[df2.status=='phishing']=1
df2.status[df2.status=='legitimate']=0
print(df1.head)
print(df2.head)

df=pd.concat([df1,df2])

print(df.shape)
print(df.head)
df.to_csv('url_july1.csv',index=False)