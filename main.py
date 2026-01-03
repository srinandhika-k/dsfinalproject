from data import load_data
from dataclean import basic_info,statistics,missing_val,outlier
from transformation import transform_data
from stats import meanmedian
from vi import advanced_plots
from kmean import kmeans_clustering



df=load_data()
basic_info(df)
statistics(df)
missing_val(df)
outlier(df)
transform_data(df)
advanced_plots(df)
meanmedian(df)
kmeans_clustering(df)

