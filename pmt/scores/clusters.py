from matchingframework.scores.clusters import Clustering
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering

class HierarchicalClustering(Clustering):

    def __init__(self, threshold):
        self.threshold = threshold

    def analyze(self):
        self.matcher.linkage_matrix = linkage(1-self.matcher.similarity_matrix, method='complete', metric='cosine')
        hc = AgglomerativeClustering(n_clusters=None, affinity='precomputed', linkage='complete', distance_threshold=self.threshold)
        hc.fit_predict(self.matcher.similarity_matrix)
        self.matcher.clusters = hc.labels_
        self.add_cluster()
