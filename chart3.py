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

def plot_chart2():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 6)
    normal_data_b = np.random.normal(size = 500, loc = 107, scale = 5)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns=['score']).assign(group = 'A')
    df_normal_b = pd.DataFrame(data = normal_data_b, columns=['score']).assign(group = 'B')
    
    score_data = pd.concat([df_normal_a, df_normal_b], ignore_index=True)
    
    sns.histplot(data=score_data
                , x='score'
                , alpha=.7
                , hue='group'
                , bins=50
                , kde=True
                )
                
    plt.show()
