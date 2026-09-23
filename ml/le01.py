import pandas as pd
from sklearn.linear_model import LinearRegression

#建立資料
df = pd.DataFrame({
  "坪數": [10, 20, 30, 40, 50],
  "房價": [300,500,700,900,1100]
})
print(df)
#build X and y
X = df[["坪數"]]
y = df["房價"]

#建立模型
model=LinearRegression()
#訓練
model.fit(X,y)

print("截距:", model.intercept_)
print("斜率",model.coef_ [0])
####################################
#畫圖

