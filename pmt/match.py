from matchingframework.structures.data import MappingFeature
from matchingframework.preprocess.data_preprocessor import DataPreprocessor
from matchingframework.match.matcher import Matcher
from pmt.utils.readers import MySQLReader
from pmt.scores.vectorizers import TFIDFVectorizer
from pmt.scores.similarities import Cosine_Similarity
from pmt.scores.clusters import HierarchicalClustering
from pmt.data import Title
import environ

env = environ.Env()
environ.Env.read_env(env_file='.env')

def load_data():
    query = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 1 AND cluster_id < 11"
    mysql = MySQLReader(env('DATABASE_HOST'), env('DATABASE_USER'), env('DATABASE_PASSWORD'), env('DATABASE_NAME'), query)
    dataset1 = mysql.read()
    query = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 0 AND cluster_id < 11"
    mysql = MySQLReader(env('DATABASE_HOST'), env('DATABASE_USER'), env('DATABASE_PASSWORD'), env('DATABASE_NAME'), query)
    dataset2 = mysql.read()
    return dataset1, dataset2

def load_features():
    title = Title(field_name='product_title', weight=1)
    mapping_features = MappingFeature()
    mapping_features.join_features = [title]
    mapping_features.left_features = ['product_title']
    mapping_features.right_features = ['product_title']
    return mapping_features

def matching(max_df, min_df, min_ngram, max_ngram, threshold):
    dataset1, dataset2 = load_data()
    mapping_features = load_features()
    stopwords = ['black', 'white', 'grey', 'silver', 'unlocked', 'sim', 'free', 'water', 'dust', 'resistant', 'by',
                 'gold', 'rose', 'space', 'handset', 'only', 'mobile phone', 'phone',
                 'smartphone', 'in', 'mobile', 'single', 'cm', '4g', '4.7', '5.5', '5.8']
    data_preprocessor = DataPreprocessor()
    vectorizer = TFIDFVectorizer(max_df=max_df, min_df=min_df, stop_words=stopwords, ngram_range=(min_ngram, max_ngram))
    similarity_scorer = Cosine_Similarity()
    cluster = HierarchicalClustering(threshold=threshold)

    m = Matcher(data_preprocessor=data_preprocessor,
                vectorizer=vectorizer,
                similarity=similarity_scorer,
                cluster=cluster)
    m.add_data(dataset1, dataset2, mapping_features)
    m.match()
    return m


# def start_match():
#     query1 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 1 AND cluster_id < 11"
#     mysql = DBReader(env('DATABASE_HOST'),
#                      env('DATABASE_USER'),
#                      env('DATABASE_PASSWORD'),
#                      env('DATABASE_NAME'),
#                      query1)
#     dataset1 = mysql.read()
#     query2 = "SELECT * FROM `product-clustering`.product WHERE category_id = 2612 AND product_id % 2 = 0 AND cluster_id < 11"
#     mysql = DBReader(env('DATABASE_HOST'),
#                      env('DATABASE_USER'),
#                      env('DATABASE_PASSWORD'),
#                      env('DATABASE_NAME'),
#                      query2)
#     dataset2 = mysql.read()
#
#     title = Title(field_name='product_title', weight=1)
#
#     mapping_features = MappingFeature()
#     mapping_features.join_features = [title]
#     mapping_features.left_features = ['product_title']
#     mapping_features.right_features = ['product_title']
#
#     stopwords = ['black', 'white', 'grey', 'silver', 'unlocked', 'sim', 'free', 'water', 'dust', 'resistant', 'by',
#                      'gold', 'rose', 'space', 'handset', 'only', 'mobile phone', 'phone',
#                      'smartphone', 'in', 'mobile', 'single', 'cm', '4g', '4.7', '5.5', '5.8']
#
#     data_preprocessor = DataPreprocessor()
#     vectorizer = TFIDFVectorizer(max_df=0.7, min_df=0.01, stop_words=stopwords, ngram_range=(1,3))
#     similarity_scorer = Cosine_Similarity()
#     cluster = HierarchicalClustering(threshold=0.5)
#
#     m = Matcher(data_preprocessor=data_preprocessor,
#                 vectorizer=vectorizer,
#                 similarity=similarity_scorer,
#                 cluster=cluster)
#     m.add_data(dataset1, dataset2, mapping_features)
#     m.match()
#     return m
