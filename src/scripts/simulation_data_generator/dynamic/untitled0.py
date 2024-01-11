#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:40:13 2023

@author: elaine
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # Parameters of the normal distribution
# mean = 0  # Mean value
# std_dev = 10  # Standard deviation

# # Generate a range of x values
# x = np.linspace(-30, 30, 300)

# # Calculate the corresponding y values from the normal distribution
# y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# # Plot the normal distribution
# plt.plot(x, y)
# plt.title('Normal Distribution')
# plt.xlabel('X')
# plt.ylabel('Probability Density')
# plt.grid(True)
# plt.show()


# #####################################################

# import numpy as np
# import matplotlib.pyplot as plt

# # Example dataset
# data = np.random.randn(1000)  # Replace with your own dataset

# # Plot histogram
# plt.hist(data, bins=30, edgecolor='black')
# plt.title('Distribution Histogram')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()




########################################################


import seaborn as sns
import os

#DIR_ROOT = os.getcwd()
social_score_1 = pd.read_csv('dS101.csv',header=0,index_col=(0))
# social_score_1.rename({"Unnamed: 6":"a","Unnamed: 7":"a"}, axis="columns", inplace=True)
# social_score_1 = social_score_1.drop(columns=("a"))
social_score_2 = pd.read_csv('dS102.csv',header=0,index_col=(0))
# social_score_2.rename({"Unnamed: 6":"a","Unnamed: 7":"a"}, axis="columns", inplace=True)
# social_score_2 = social_score_2.drop(columns=("a"))
social_score_3 = pd.read_csv('dS103.csv',header=0,index_col=(0))
# social_score_3.rename({"Unnamed: 6":"a","Unnamed: 7":"a"}, axis="columns", inplace=True)
# social_score_3 = social_score_3.drop(columns=("a"))
fig,(s_1,s_2,s_3,y_ax) = plt.subplots(nrows=1,ncols=4,gridspec_kw={'width_ratios':[1,1,1,0.08]})
s_1.get_shared_y_axes().join(s_2,s_3)
g1 = sns.heatmap(social_score_1,cmap="Greys",square=True,vmin=-26,vmax=35,\
                 xticklabels=False,yticklabels=False,cbar=False,ax=s_1).set(title ='Set 1',xlabel="mean = 0")
g2 = sns.heatmap(social_score_2,cmap="Greys",square=True,vmin=-26,vmax=35,\
                 xticklabels=False,yticklabels=False,cbar=False,ax=s_2).set(title ='Set 2',xlabel="mean = 16")
g3 = sns.heatmap(social_score_3,cmap="Greys",square=True,vmin=-26,vmax=35,\
                 xticklabels=False,yticklabels=False,ax=s_3, cbar_ax=y_ax).set(title ='Set 3',xlabel="mean = -8")

# sns.heatmap(social_score_1,cmap='Greys',square=True,xticklabels=False,yticklabels=False)
# sns.heatmap(social_score_2,cmap='Greys',square=True,xticklabels=False,yticklabels=False)
# sns.heatmap(social_score_3,cmap='Greys',square=True,xticklabels=False,yticklabels=False)


plt.savefig('set1_3_heatmap.png',dpi=400)







