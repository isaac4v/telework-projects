import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123456)

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))

ts = ts.cumsum()

ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))
df = df.cumsum()
df.plot()
plt.show()

df3 = pd.DataFrame(np.random.randn(1000,2),columns=['B','C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A',y='B')
plt.show()

df2 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df2.plot.bar()
plt.show()

df2.plot.bar(stacked=True)
plt.show()

df.diff().hist(color='b',alpha=0.5,bins=50)
plt.show()

df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a',y='b',c='c',s=df['c']*200,cmap='hsv')
plt.show()

df = pd.DataFrame(np.random.randn(1000,2),index=None,columns=['a','b'])
df['b']=df['b']+np.arange(1000)
df.plot.hexbin(x='a',y='b',gridsize=25)
plt.show()