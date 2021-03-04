# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd

# loading dataset 
with open("result/256", 'r') as f:
    data = f.read()
data = data.split(",")

data = [float(x) for x in data]
  
# draw lineplot 
sns.lineplot(x=[i for i in range(20)], y=data) 
plt.show()