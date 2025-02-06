#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generating social range

@author: elaine
modified by Chih-Yi Chen on 2024-05-22
"""

import os
import numpy as np
import pandas as pd
import inspect

def generate_social_score(FNAME='dS103_test',MIN=-30,MAX=0,MEAN=-10,SD=10):

    """
    Generate a social score matrix and save it as a CSV file.

    Parameters:
    FNAME (str): The name of the output file (without extension).
    MIN (int): The minimum value for the random integers.
    MAX (int): The maximum value for the random integers.
    MEAN (int): The desired mean of the generated social scores.
    SD (int): The desired standard deviation of the generated social scores.

    Output:
    A CSV file named '<FNAME>.csv' containing the social score matrix.
    The file will be saved in the current working directory.
    """

    current_file_path = inspect.getfile(inspect.currentframe())
    DIR_CSV_OUTPUT = os.path.dirname(current_file_path)
    for n in range(1):
        social_score = []
        # Set the random seed for reproducibility
        np.random.seed(42)

        # Generate a random set of 20 integers approximately satisfying the conditions
        social_score = np.random.randint(MIN, MAX+1, size=20)

        # Adjust the mean to 0 & standard deviation to 1
        social_score = (social_score - np.mean(social_score)) / np.std(social_score)
     
        social_score = (social_score * SD) + MEAN
        
                
        social_score = np.insert(social_score,(0,5,10,15,20),0)
        social_score = social_score.reshape(5,5)
        social_score = social_score.astype(float)
        
        df_social_score = pd.DataFrame(data = {" ":["S","A","B","C","D"],\
                                                              "S":social_score[0],\
                                                              "A":social_score[1],\
                                                              "B":social_score[2],\
                                                              "C":social_score[3],\
                                                              "D":social_score[4]})
        try:
            output = os.path.join(DIR_CSV_OUTPUT,str(FNAME)+".csv")
            df_social_score.to_csv(output,index=False)
        except:print('error')
        #print(df_social_score)
        n+=1

