from matchingframework.scores.similarities import SimilarityScorer

from sklearn.metrics.pairwise import cosine_similarity
class CosineSimilarityScorer(SimilarityScorer):

    def similarity_score(self, vector_matrix):
        """
        Compute cosine similarity distance.
        """
        return 1 - cosine_similarity(vector_matrix)
