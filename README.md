Server-side - k-means

To run the code:
1. $ git clone https://github.com/AmotzL/K_Means.git
2. $ cd K_Means
3. $ pip install .
4. $ python kmeans/kmeans/__init__.py
5. Go to http://127.0.0.1:5000 or http://localhost:5000
6. Insert the number of the wanted clusters

The program is running the k-means algorithm on the mnist data-set.
For each cluster, the page represents the cluster centroid image, 
five more images that the algorithm tagged the same and their true label.

The mnist data set - A 60,000 train images in size 28x28 of hand 
written digits (0-9) and their labels:
http://yann.lecun.com/exdb/mnist/
