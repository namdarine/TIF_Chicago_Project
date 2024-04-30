## Background
### Understanding of boundaries
When choosing what boundaries to use we had to ensure we would be able to acquire the correct data based on those boundaries and ensure the areas we were working with weren’t too large or small. TIF districts on average are fairly small and generally coincide with census tracts and block groups in relative areas. Therefore we originally chose to work with census tracts as a happy medium for boundary size, however, we later decided block groups would be better to use. The smaller size of block groups made it easier to differentiate whole community areas between TIF and non-TIF. The figure below shows the difference in areas of each boundary option.
![Unknown](https://github.com/namdarine/TIF_Chicago_Project/assets/105746802/9851f3dd-9cd3-4647-8627-72d7aafefd6d)


### Income distribution (Gamma distribution)
The US Census data has a data structure of income as {interval of income : population corresponding to the interval}. Thus, it is crucial to fit a probability distribution to determine on certain statistic. Observing our data, as shown in figure below, it seemed to be most reasonable to use gamma distribution.
![image](https://github.com/namdarine/TIF_Chicago_Project/assets/149856512/435603ea-4a1a-44b6-b7e2-d418deba8f4e)


So, using gamma distribution, we matched the probability of having certain interval of income to the population percentage of that interval.

### Bartlett test of sphericity
Before doing Principal Component Analysis (PCA), it is important to determine whether the data is correlated or not. Let's say the data is like this.
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ![PCA Background](/_asset/img/Background/Background_PCA.png)   
It is ambiguous to choose Principle components. It implies a lack of connection between variables, showing that PCA may not be appropriate.  ㅤ  
Therefore, it is crucial to determine whether the data is correleated or not. One approach to test this is to compare the correlation and identity matrices. This test, known as Bartlett's test of sphericity, determines whether the variables are uncorrelated.

The null hypothesis $H_0$ for Bartlett's test of sphericity is:

$$
H_0: \text{The variables in the dataset are uncorrelated}
$$

This can be expressed more formally as:

$$
H_0: \Sigma = I
$$

$$
H_1: \Sigma \neq I
$$

Where:
- $\Sigma$ represents the correlation matrix of the variables.
- $I$ represents the identity matrix.

The null hypothesis asserts that the correlation matrix $\Sigma$ is equal to the identity matrix $I$, indicating that the variables in the dataset are essentially unrelated or uncorrelated.
If the p-value  is less than 0.05, we reject the null hypothesis, which means the variables are not uncorrelated.

This can be formally expressed as:


If \( p < 0.05 \), we reject the null hypothesis, indicating that the variables are not uncorrelated.

Where:
- p : represents the p-value associated with Bartlett's test of sphericity.




### PCA
PCA is a statistical approach for dimensionality reduction. It is based on the concept of changing the original variables into a new set of variables known as principle components. These components are linear combinations of the original variables, selected to capture as much volatility in the data as feasible.

Let the Covariance matrix  $X$ be $\ n \times p $.

By using Singular Value Decomposition (SVD),

$$ X = UDV^{T} $$

where $U$ : $n \times p$, $D$ : $p \times p$, $V$ : $p \times p$

$V^{T}V = I_p$, $U^{T}U = I_p$, $D$ : diagonal Matrix

The column vector of $V$ is the eigenvectors of $X^{T}X$, and $D$ is the eigenvalues of $X^{T}X$.

$$X = UDV^{T} \rightarrow XV = UD\ \ in\ \   V^{T}V = I_p$$
Therefore, PCScore = $XV = UD$

To determine the number of Priciple Components, you have to decide what percentage of variance you want to account for.
Let's say we reduce the dimensionality of the entire dataset to the point where it explains, for example, 90% of the variance.

There are $p$ eigen values $\lambda_1, \lambda_2, \lambda_3, ... , \lambda_p$
$$\frac{\displaystyle\sum_{j=1}^{m} \lambda_j}{\displaystyle\sum_{i=1}^{p} \lambda_i} = 0.9$$
where $m$ is the number of Priciple Components.  
In Python, there is a library for plotting the graph,     
ㅤㅤㅤㅤㅤ![PCA](https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Background/Determine_the_number_of_Prinicipal_Components.png)

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ


### Clustering, elbow method, silhouette method
> Clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some specific sense defined by the analyst) to each other than to those in other groups (clusters).

#### K-means Clustering
k-means clustering which we use is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells.
  
#### DBSCAN Clustering
<U>Density-based spatial clustering of applications with noise</U> (DBSCAN) is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander and Xiaowei Xu in 1996.[1] It is a **density-based** clustering non-parametric algorithm: given a set of points in some space, it groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away). DBSCAN is one of the most common, and most commonly cited, clustering algorithms.
  
DBSCAN requires to specify the minimum number of points.  
  
<img src=https://github.com/namdarine/TIF_Chicago_Project/blob/main/_asset/img/Background/DBSCAN.png width="300" height="300"/>  

  
**eps** : $\epsilon$, defines the neighborhood around a data point. If the distance between two data points is lower than or eaqual to 'eps', then they are considered neighbors. If the eps value is chosen too small then a large part of the data will be considered as an outlier. If it is chosen very large then the clusters will merge and the majority of the data points will be in the same clusters.  
  
**minPts** : Minimum number of neighbors (data points) within eps radius. The larger the dataset, the larger value of MinPts must be chosen. As a general rule, the minimum MinPts can be derived from the number of dimensions D in the dataset as, MinPts >= D+1. But it should be at least 3.  
  
#### Elbow method and Silhouette method
**Elbow Method** is a technique that we use to determine the number of centroids(k) to use in a k-means clustering algorithm. A fundamental step for any unsupervised algorithm is to determine the optimal number of clusters into which the data may be clustered. Since we do not have any predefined number of clusters in unsupervised learning. We tend to use some method that can help us decide the best number of clusters.  In the case of K-Means clustering, we use Elbow Method for defining the best number of clustering. 
  
**Silhouette Method** 
Silhouette analysis can be used to study the separation distance between the resulting clusters. The silhouette plot displays a measure of how close each point in one cluster is to points in the neighboring clusters and thus provides a way to assess parameters like number of clusters visually. This measure has a range of [-1, 1]. Silhouette coefficients near +1 indicate that the sample is far away from the neighboring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary between two neighboring clusters and negative values indicate that those samples might have been assigned to the wrong cluster.

