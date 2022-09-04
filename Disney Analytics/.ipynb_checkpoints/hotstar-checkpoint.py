#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:54:06 2021

@author: arpit
"""



import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import plotly as py

df = pd.read_csv('./HOTSTAR.csv')

df = df.dropna(how='any',axis=0) 

print(df.head(1))

df.describe()

