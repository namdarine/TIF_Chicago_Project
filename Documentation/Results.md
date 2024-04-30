## Results
⁤As we analyzed Chicago's TIF program, a significant difference was displayed in median income. ⁤⁤Therefore, we conducted a more in-depth analysis focusing mainly on median income.
![Median_Income](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Median_income.png)  
[Other_Metrics](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Chicago)  
  
⁤This analysis was conducted for the Chicago area and classified regions based on racial demographics and TIF and non-TIF districts. ⁤ 

Using k-means clustering with four clusters determined by the silhouette score, the following cluster differences were formed:  
![Silhouette_score](https://github.com/namdarine/TIF_Chicago_Project/blob/5ad19cd1fd7f64f51694dd6a56de763e1caed917/_asset/img/Cluster_methods/silhouette_score.png)   
![Cluster_map](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Cluster_Map.png)  
  
Cluster 1: Characterized by areas of predominantly White residents.  
Cluster 2: Predominantly Black residents.  
Cluster 3: Exhibits mixed racial composition.  
Cluster 4: Predominantly Latino residents.    

Further analysis has shown that cluster 1 has the highest median income.  
![Median_Income_by_Clusters](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Median_income_by_cluster.png)  
  
Finally, an evaluation was conducted to compare the percentage of median income increase between TIF and non-TIF regions in each cluster. In particular, only in cluster 1 was a significant difference in the ratio between the TIF and non-TIF regions, and a minimal difference was observed in the remaining clusters.    
![TIF_nonTIF](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/tif_nonTIF.png)  

Essentially, this study identified a correlation between race and median income in the context of Chicago's TIF program, regions with higher populations of White residents showed the highest median income and, more importantly, median income difference between TIF and non-TIF regions.  
