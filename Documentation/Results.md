## Results
An investigation into Chicago's Tax Increment Financing (TIF) program revealed a significant variation solely in median income. Consequently, a more in-depth analysis focusing solely on median income data was undertaken.  
![Median_Income](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Median_income.png)  
[Other_Metrics](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Chicago)  
  
The findings of this analysis can be extrapolated to Chicago as a whole, prompting a categorization based on community areas defined by racial demographics: White, Hispanic, and Black populations.  

Employing k-means clustering with four clusters determined by the silhouette score, the following cluster distinctions emerged:  
![Silhouette_score](https://github.com/namdarine/TIF_Chicago_Project/blob/5ad19cd1fd7f64f51694dd6a56de763e1caed917/_asset/img/Cluster_methods/silhouette_score.png)   
![Cluster_map](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Cluster_Map.png)  
  
Cluster 1: Characterized by a predominance of White residents.  
Cluster 2: Dominated by Black residents.  
Cluster 3: Exhibits a mixed demographic composition.  
Cluster 4: Predominantly Latino.  

Further examination delved into assessing median income within each cluster, uncovering Cluster 1, representing White-majority regions, as exhibiting the highest median income.  
![Median_Income_by_Clusters](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Median_income_by_cluster.png)  
  
Lastly, an evaluation was conducted to compare the percentage of median interior values between TIF and non-TIF areas within each cluster. Notably, only Cluster 1 exhibited a substantial disparity in median interior percentages between TIF and non-TIF regions, with minimal differences observed across the remaining clusters.    
![TIF_nonTIF](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/tif_nonTIF.png)  

In essence, the study identified a correlation between race and median income within the context of Chicago's TIF program, with White-majority areas demonstrating the highest median incomes and the most significant difference in median interior values between TIF and non-TIF regions.  
