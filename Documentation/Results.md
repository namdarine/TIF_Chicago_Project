## Results
After analyzing the gathered data pertaining to the Chicago TIF (Tax Increment Financing) project, it was found that only the median income exhibits a significant variance. Following this observation, the decision was made to conduct a deeper examination focusing solely on the median income data.  
![Median_Income](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Others/Median_income_increase_graph_in_Chicago.png)  
![Other_Metrics](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Chicago)  
  
The outcomes of this analysis can be understood within the context of Chicago as a whole, thus prompting a classification based on community areas categorized by race, namely White, Hispanic, and Black populations.

Utilizing k-means clustering with four clusters based on the silhouette score, the following cluster distinctions were made:
![Silhouette_score](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Cluster_methods/silhouette_score.png)   
![Cluster_map](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Cluster_Map.png)  
  
Cluster 1: Characterized by a predominance of White residents.
Cluster 2: Dominated by Black residents.
Cluster 3: Exhibits a mixed demographic composition.
Cluster 4: Predominantly Latino.

Further scrutiny was directed towards assessing the median income within each cluster, revealing Cluster 1, representing White-dominant regions, to possess the highest median income.  
![Median_Income_by_Clusters](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/Median_income_by_cluster.png)  
  
Lastly, an examination was conducted to compare the percentage of median interior values between TIF and Non-TIF regions within each cluster. Notably, only Cluster 10 exhibited a notable disparity in median interior percentages between TIF and non-TIF regions, with minimal differences observed across the remaining clusters.  
![TIF_nonTIF](https://github.com/namdarine/TIF_Chicago_Project/blob/1341c569e33aec66e149b434c80433a4ac737530/_asset/img/tif_nonTIF.png)  
