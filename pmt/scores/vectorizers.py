from matchingframework.scores.vectorizers import FrequencyVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer
class TFIDFVectorizer(FrequencyVectorizer):

    def vectorize_matrix(self, feature, records):
        vectorizer = TfidfVectorizer(max_df=self.max_df,
                                           min_df=self.min_df,
                                           ngram_range=self.ngram_range,
                                           stop_words=self.stop_words,
                                           tokenizer=feature.tokenizer.tokenize_record)
        return vectorizer.fit_transform(feature.tokenizer.normalize(list(records.values())))
