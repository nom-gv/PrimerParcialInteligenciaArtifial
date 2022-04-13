# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 02:19:23 2022

@author: NOEMI
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

df = sns.load_dataset('titanic')
df=df.groupby(['who','sex'])['fare'].sum().to_frame().reset_index()

print(df)