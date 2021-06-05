from matchingframework.scores.clusters import Clustering

from scipy.cluster.hierarchy import linkage, fcluster
class HierarchicalClustering(Clustering):

    def __init__(self, threshold):
        self.thresold = threshold

    def analyze(self):
        linkage_matrix = linkage(self.matcher.similarity_matrix, method='complete', metric='cosine')
        self.matcher.clusters = fcluster(linkage_matrix, t=self.thresold, criterion='distance')
        self.add_cluster()

from sklearn.cluster import KMeans
class KMeansClustering(Clustering):

    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    def analyze(self):
        kmeans = KMeans(n_clusters=self.n_clusters)
        kmeans.fit(self.matcher.similarity_matrix)
        self.matcher.clusters = kmeans.labels_
        self.add_cluster()
