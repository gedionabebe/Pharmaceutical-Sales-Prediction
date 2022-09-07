from aiohttp_retry import logging
import pandas as pd
import logging
import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

def plot_hist(df,column,color):
        sns.displot(data=df, x=column, color=color,
                    kde=True, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

def plot_hist_many(df,columns,color):
        for i,col in enumerate(columns):
            sns.displot(data=df, x=col, color=color[i],
                    kde=True, aspect=2,rug=True)
            plt.title(f'Distribution of {col}', size=20, fontweight='bold')
        plt.show()
        
def plot_count(df, column):
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

def plot_bar(df,x_col,y_col,title,xlabel,ylabel):
        
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()

def plot_heatmap(df,title,cbar=False):
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        plt.show()