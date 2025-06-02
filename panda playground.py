# panda playground

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_df = pd.read_excel('C:/Users/Connor/Code/Excel/Finance_data.xlsx','Sheet1',index_col=0,na_values=['NA'])

if data_df.isinstance is not None:
    
    print(data_df.mean())


