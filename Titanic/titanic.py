import pandas as pd
from plotnine import *
import plots as plt
import numpy as np

df = pd.read_csv("train.csv")
df.describe()
df.head()
df.columns # 7 col are num, 5 are cat
df.isnull().sum() #age and cabin missing values
df.dtypes

df.Name
    
plt.scatter(df,'Survived','Age')
plt.scatter(df,df.index,'Age')

plt.hist(df,'Cabin',30)
plt.boxplot(df,'Age')

import plotly.plotly as py
from plotly.graph_objs import *

data = {'x': df.Age.values,
        'y': df.Fare.values,
        'z': df.Survived.values,
        'type': 'surface'}

fig = Figure(data=data)
py.plot(fig)


ggplot(df,aes('Age','Fare',color='factor(Pclass)'))+\
geom_point(shape=df.Survived)


from plotly.


