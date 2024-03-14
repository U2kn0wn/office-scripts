import pandas as pd

data=pd.read_excel("./data.xlsx")
data2=data[['S.No.', 'Product & Description', 'Hardware Details']]
print(data2.iloc[0,1].isnumeric())