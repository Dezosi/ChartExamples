import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_chart():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 600, loc = 90, scale = 9)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns = ['score']).assign(group = 'Group A')
    
    sns.histplot(data=df_normal_a
                , x='score'
                , bins=50
                , kde= True
                )

    plt.show()
