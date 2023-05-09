# import os
# import tarfile
# import urllib
import matplotlib.pyplot as plt
import numpy as np  
from zlib import crc32
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

#Download the Data
PATH = "AM/housing.csv"
      
import pandas as pd 
      
def load_housing_data(housing_path=PATH):
    return pd.read_csv(housing_path)

#Take a Quick Look at the Data Structure
housing = load_housing_data()
print(housing.head())
print(housing.info())


