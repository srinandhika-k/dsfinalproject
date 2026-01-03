def basic_info(df):
    print("\n First 5 rows: \n", df.head())
    print("\nDataset Info:\n")
    print(df.info())

def statistics(df):
    print("Stastical Information about the dataset:\n", df.describe())

def missing_val(df):
    print("Missing values in the dataset:\n", df.isnull().sum())

def outlier(df):
    numeric=df.select_dtypes(include='number')
    q1=numeric.quantile(0.25)
    q3=numeric.quantile(0.75)
    iqr=q3-q1
    print("\nInter quantile value:",iqr)
    lower=q1-1.5*iqr
    upper=q3+1.5*iqr
    outliers=numeric[(numeric<lower)|(numeric>upper)]
    print("\n Outliers in the dataset:")
    print(outliers)