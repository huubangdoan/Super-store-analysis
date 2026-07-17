import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def first_look(df, cols):
    print(df.head(10))
    print(df.tail(10))
    print(df.info())
    print(df.dtypes)
    print(df.nunique())
def exportFile(df, name):
    df.to_csv(f"data\processed\{name}.csv") 

if __name__ == "__main__":
    df=pd.read_csv(r"data\raw\SampleSuperstore.csv")
    cols=df.columns.to_list()
    first_look(df,cols)
    exportFile(df[cols].describe(), "describeSuperstore")