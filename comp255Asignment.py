# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:18:01 2019

@author: Tony
"""

"""Import Library"""
import numpy as np 
import pandas as pd 
from scipy import signal
import matplotlib.pyplot as plt 
import math
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import make_scorer, accuracy_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

pd.read_csv("dataset_1.txt")
pd.read_csv("dataset_2.txt")
pd.read_csv("dataset_3.txt")
pd.read_csv("dataset_4.txt")
pd.read_csv("dataset_5.txt")
pd.read_csv("dataset_6.txt")
pd.read_csv("dataset_7.txt")
pd.read_csv("dataset_8.txt")
pd.read_csv("dataset_9.txt")
pd.read_csv("dataset_10.txt")
pd.read_csv("dataset_11.txt")
pd.read_csv("dataset_12.txt")
pd.read_csv("dataset_13.txt")
pd.read_csv("dataset_14.txt")
pd.read_csv("dataset_15.txt")
pd.read_csv("dataset_16.txt")
pd.read_csv("dataset_17.txt")
pd.read_csv("dataset_18.txt")
pd.read_csv("dataset_19.txt")
