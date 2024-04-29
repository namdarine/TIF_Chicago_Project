## Background
### Understanding of boundaries
When choosing what boundaries to use we had to ensure we would be able to acquire the correct data based on those boundaries and ensure the areas we were working with weren’t too large or small. TIF districts on average are fairly small and generally coincide with census tracts and block groups in relative areas. Therefore we originally chose to work with census tracts as a happy medium for boundary size, however, we later decided block groups would be better to use. The smaller size of block groups made it easier to differentiate whole community areas between TIF and non-TIF.

### Income distribution (Gamma distribution)
The US Census data has a data structure of income as {interval of income : population corresponding to the interval}. Thus, it is crucial to fit a probability distribution to determine on certain statistic. Observing our data, as shown in figure below, it seemed to be most reasonable to use gamma distribution.
![image](https://github.com/namdarine/TIF_Chicago_Project/assets/149856512/435603ea-4a1a-44b6-b7e2-d418deba8f4e)


So, using gamma distribution, we matched the probability of having certain interval of income to the population percentage of that interval.

### Bartlett test of sphericity
Before conducting Principal Component Analysis (PCA), it's essential to assess whether the data exhibit correlation among variables. For instance, if the data visualized in a scatter plot resemble a circular distribution (Fig. 1), it suggests a lack of correlation among variables, indicating that PCA may not be suitable.  ㅤ
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ![PCA Background](/_asset/img/Background/Background_PCA.png)

Thus, prior to applying PCA, it's prudent to examine whether the data meet the assumptions of the analysis. One way to assess this is by evaluating the similarity between the correlation matrix of variables and the identity matrix. This test, known as Bartlett's test of sphericity, helps determine if the variables are essentially uncorrelated, which is a prerequisite for PCA.

The null hypothesis $H_0$ for Bartlett's test of sphericity is stated as:

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
The test statistic follows a chi-square distribution, and if the p-value associated with the test is small (less than 0.05), we reject the null hypothesis, indicating that the variables are not uncorrelated.

This can be formally expressed as:


If \( p < 0.05 \), we reject the null hypothesis, indicating that the variables are not uncorrelated.

Where:
- p : represents the p-value associated with Bartlett's test of sphericity.




### PCA
PCA is a statistical technique used for dimensionality reduction and data visualization. It's based on the idea of transforming the original variables into a new set of variables called principal components. These components are linear combinations of the original variables and are chosen to capture as much of the variance in the data as possible.

Let the Covariance matrix $ X $  be $\ n \times p $.

By using Singular Value Decomposition (SVD),

$$ X = UDV^{T} $$

where $$ U $$ : $ n \times p $, $ D $ : $ p \times p $, $ V $ : $ p \times p $

$ V^{T}V = I_p $,$\    $   $ U^{T}U = I_p $,$\  $ $ D $ : diagonal Matrix

Therefore,

The column vector of $ V $ is the eigenvectors of $ X^{T}X $, and $ D $ is the eigenvalues of $ X^{T}X $.



### Clustering, elbow method, silhouette method
> Clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some specific sense defined by the analyst) to each other than to those in other groups (clusters).

#### K-means Clustering
k-means clustering which we use is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells.

#### Elbow method and Silhouette method
**Elbow Method** is a technique that we use to determine the number of centroids(k) to use in a k-means clustering algorithm. A fundamental step for any unsupervised algorithm is to determine the optimal number of clusters into which the data may be clustered. Since we do not have any predefined number of clusters in unsupervised learning. We tend to use some method that can help us decide the best number of clusters.  In the case of K-Means clustering, we use Elbow Method for defining the best number of clustering. 
  
**Silhouette Method** 
Silhouette analysis can be used to study the separation distance between the resulting clusters. The silhouette plot displays a measure of how close each point in one cluster is to points in the neighboring clusters and thus provides a way to assess parameters like number of clusters visually. This measure has a range of [-1, 1]. Silhouette coefficients near +1 indicate that the sample is far away from the neighboring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary between two neighboring clusters and negative values indicate that those samples might have been assigned to the wrong cluster.

