import pandas as pd
import numpy as np

def meanmedian(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    mean= df[numeric_cols].mean()
    median= df[numeric_cols].median()
    
    stats_df = pd.DataFrame({'Mean': mean,'Median': median})
    print(stats_df)