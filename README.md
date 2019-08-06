Server-side - k-means

To run the code:
<<<<<<< HEAD
$ git clone https://github.com/AmotzL/K_Means.git
$ cd K_Means
$ pip install .
$ python kmeans/kmeans/run.py
=======
1. Clone this repository
2. Go to K_Means-master\kmeans
3. Type: pip install .
4. Go to K_Means-master\kmeans\kmeans
5. Type: python __init__.py
>>>>>>> ea0a66fde28c6ae7d81159b47ef884ec5e5b6da5
6. Go to http://127.0.0.1:5000 or http://localhost:5000
7. Insert the number of the wanted clusters

The program is running the k-means algorithm on the mnist data-set.
For each cluster, the page represents the cluster centroid image, 
five more images that the algorithm tagged the same and their true label.

The mnist data set - A 60,000 train images in size 28x28 of hand 
written digits (0-9) and their labels:
http://yann.lecun.com/exdb/mnist/
