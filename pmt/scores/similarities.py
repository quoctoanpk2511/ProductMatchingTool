from matchingframework.scores.similarities import SimilarityScorer

from sklearn.metrics.pairwise import cosine_similarity
class Cosine_Similarity(SimilarityScorer):

    def similarity_score(self, vector_matrix):
        """
        Compute cosine similarity.
        """
        return cosine_similarity(vector_matrix)
