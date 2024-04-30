## Results
⁤As a result of analyzing Chicago's TIF program, there was a significant difference only in median income. ⁤⁤Therefore, we conducted a more in-depth analysis focusing only on median income data.  
![Median_Income](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Median_income.png)  
[Other_Metrics](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Chicago)  
  
⁤This analysis can be estimated for the entire Chicago area and classified based on race demographics, white, Hispanic, and black populations. ⁤ 

Using k-means clustering with four clusters determined by silhouette score, the following cluster differences were shown:  
![Silhouette_score](https://github.com/namdarine/TIF_Chicago_Project/blob/5ad19cd1fd7f64f51694dd6a56de763e1caed917/_asset/img/Cluster_methods/silhouette_score.png)   
![Cluster_map](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Cluster_Map.png)  
  
Cluster 1: Characterized by a predominance of White residents.  
Cluster 2: Dominated by Black residents.  
Cluster 3: Exhibits a mixed demographic composition.  
Cluster 4: Predominantly Latino.  

Further research has shown that cluster 1, which represents a large number of white areas, has the highest median income.  
![Median_Income_by_Clusters](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Median_income_by_cluster.png)  
  
Finally, the evaluation was conducted to compare the percentage of median internal values between TIF and non-TIF regions in each cluster. In particular, only in cluster 1, there was a significant difference in the central internal ratio between the TIF and non-TIF regions, and a minimal difference was observed in the remaining clusters.    
![TIF_nonTIF](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/tif_nonTIF.png)  

Essentially, the study identified a correlation between race and median income in the context of Chicago's TIF program, and regions with a large number of whites showed the highest median income and the most important median income difference between TIF and non-TIF regions.  