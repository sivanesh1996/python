from sklearn.linear_model import LinearRegression
import numpy as np

x=[ [6], [8], [10], [14], [18]]
y=[ [7], [9], [13], [17.5], [18]]
model=LinearRegression()
model.fit(x,y)

print('Residual sum of squares: ',np.mean((model.predict(x)-y)**2))
print("Variance: ",np.var([6,8,10,14,18], ddof=1))
print('Covariance: ',np.cov([6,8,10,14,18],[7,9,13,17.5,18])[0][1])
print("X_Mean= ",np.mean(x))
print("Y_Mean: ",np.mean(y))