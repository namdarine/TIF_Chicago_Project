## Background
### Understanding of boundaries
When choosing what boundaries to use we had to ensure we would be able to acquire the correct data based on those boundaries and ensure the areas we were working with weren’t too large or small. TIF districts on average are fairly small and generally coincide with census tracts and block groups in relative areas. Therefore we originally chose to work with census tracts as a happy medium for boundary size, however, we later decided block groups would be better to use. The smaller size of block groups made it easier to differentiate whole community areas between TIF and non-TIF.

### Income distribution (Gamma distribution) - Kunwoo
Contents

### Bartlett test of sphericity - JJ
Before conducting Principal Component Analysis (PCA), it's essential to assess whether the data exhibit correlation among variables. For instance, if the data visualized in a scatter plot resemble a circular distribution (Fig. 1), it suggests a lack of correlation among variables, indicating that PCA may not be suitable.
![PCA Background](/_asset/img/Background/Background_PCA.png)

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




### PCA - JJ
Contents

### Clustering, elbow method, silhouette method - Nam
Contents
