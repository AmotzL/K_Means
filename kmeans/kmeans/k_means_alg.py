
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
import struct
import shutil
import os


path = 'kmeans/static/cluster_images/'


def parse_images(file_path):
    """
    Parse the input byte images file (train or test) into images
    at shape 1x784.
    """
    with open(file_path, 'rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        nrows, ncols = struct.unpack(">II", f.read(8))
        data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        data = data.reshape((size, nrows * ncols))
    return data


def parse_labels(file_path):
    """
    Parse the input byte labels file (train or test) into a list
    of labels corresponding to the images.
    """
    with open(file_path, 'rb') as f:
        magic, size = struct.unpack(">II", f.read(8))
        labels = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    return labels


def k_means(cluster_num, train_images, train_labels):
    """
    Calculate the K-means and crate the result centroid, chosen images
    and their true labels.
    """
    km = KMeans(cluster_num, random_state=0)
    labels = km.fit_predict(train_images)
    labeled_images_pos = {}
    for i in range(len(labels)):
        if labels[i] not in labeled_images_pos:
            labeled_images_pos[labels[i]] = []
        labeled_images_pos[labels[i]].append(i)
    result_centers, result_clusters, result_labels = [], [], []
    for i in range(cluster_num):
        cluster_im = km.cluster_centers_[i].reshape(28, 28)
        result_centers.append(cluster_im)
        cluster_images, cluster_true_labels = [], []
        for j in range(5):
            index = labeled_images_pos[i][j]
            cluster_images.append(train_images[index].reshape(28, 28))
            cluster_true_labels.append(train_labels[index])
        result_clusters.append(cluster_images)
        result_labels.append(cluster_true_labels)
    return result_centers, result_clusters, result_labels


def create_images(centers, clusters, true_labels):
    """
    Create the result images (K centroids and 5 chosen cluster images for each)
    in the static folder.
    """
    result = {}
    app_root = os.getcwd()
    target = os.path.join(app_root, path)
    if os.path.exists(target):
        shutil.rmtree(target)
    os.mkdir(target)
    for i in range(len(centers)):
        cluster_dir_path = 'cluster_' + str(i) + '/'
        cluster_target = target + cluster_dir_path
        centroid_path = path + cluster_dir_path + 'centroid_' + str(i) + '.jpg'
        curr_cluster = 'cluster' + str(i)
        result[curr_cluster] = {'centroid': {'path': centroid_path, 'tag': i}}
        os.mkdir(cluster_target)
        im = Image.fromarray(centers[i].astype(np.uint8))
        im.save(cluster_target + 'centroid_' + str(i) + '.jpg')
        for j in range(5):
            sample_im = Image.fromarray(clusters[i][j])
            sample_im.save(cluster_target + 'sample_image_' + str(j) + '.jpg')
            im_path = path + cluster_dir_path + 'sample_image_' + str(j) + '.jpg'
            result[curr_cluster]['sample' + str(j)] = {'path': im_path, 'tag': str(true_labels[i][j])}
    return result


def run_algorithm(clusters_number):
    """
    Run the K-means algorithm on the mnist data images.
    """
    
    curr = os.getcwd()
    # Train data (60,000 images and labels):
    images = parse_images(curr + '/data/train-images.idx3-ubyte')
    labels = parse_labels(curr + '/data/train-labels.idx1-ubyte')

    # Test data (10,000 images and labels):
    # uncomment in order to run faster on the test data set.
    # images = parse_images(curr + 'kmeans/data/t10k-images.idx3-ubyte')
    # labels = parse_labels(curr + 'kmeans/data/t10k-labels.idx1-ubyte')

    centers_images, cluster_images, labels = k_means(clusters_number, images, labels)
    result = create_images(centers_images, cluster_images, labels)
    return result
