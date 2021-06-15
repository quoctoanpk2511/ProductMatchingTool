from matchingframework.structures.data import MappingFeature
from matchingframework.preprocess.data_preprocessor import DataPreprocessor
from matchingframework.match.matcher import Matcher
from pmt.utils.readers import MySQLReader
from pmt.utils.writers import MySQLWriter
from pmt.scores.vectorizers import TFIDFVectorizer
from pmt.scores.similarities import CosineSimilarityScorer
from pmt.scores.clusters import HierarchicalClustering
from pmt.structures.data import Title, Brand
import environ

env = environ.Env()
environ.Env.read_env(env_file='.env')
db_host = env('DATABASE_HOST')
db_user = env('DATABASE_USER')
db_passwd = env('DATABASE_PASSWORD')
db_name = env('DATABASE_NAME')

def load_data():
    query = "SELECT * FROM test_tiki_product WHERE sales_page = 'tiki'"
    mysql = MySQLReader(db_host, db_user, db_passwd, db_name, query)
    dataset1 = mysql.read()
    query = "SELECT * FROM test_tiki_product WHERE sales_page = 'sendo'"
    mysql = MySQLReader(db_host, db_user, db_passwd, db_name, query)
    dataset2 = mysql.read()
    return dataset1, dataset2

def load_features():
    title = Title(field_name='title', weight=0.5)
    brand = Brand(field_name='brand', weight=0.5)
    mapping_features = MappingFeature()
    mapping_features.join_features = [title, brand]
    mapping_features.left_features = ['name', 'brand']
    mapping_features.right_features = ['name', 'brand']
    return mapping_features

def matching():
    dataset1, dataset2 = load_data()
    mapping_features = load_features()
    data_preprocessor = DataPreprocessor()
    stopwords = ['freeship', 'hàng', 'nhập', 'khẩu', 'chính', 'hãng', 'sale', 'model', 'rẻ']
    vectorizer = TFIDFVectorizer(max_df=0.7, min_df=0.01, stop_words=stopwords, ngram_range=(1, 3))
    similarity_scorer = CosineSimilarityScorer()
    cluster = HierarchicalClustering(threshold=0.4)

    m = Matcher(data_preprocessor=data_preprocessor,
                vectorizer=vectorizer,
                similarity=similarity_scorer,
                cluster=cluster)
    m.add_data(dataset1, dataset2, mapping_features)
    m.match()
    return m

def update_cluster(m):
    mysql = MySQLWriter(db_host, db_user, db_passwd, db_name, dataset=m.left_data)
    mysql.update(table_name='test_tiki_product', pk='pid')

    mysql = MySQLWriter(db_host, db_user, db_passwd, db_name, dataset=m.right_data)
    mysql.update(table_name='test_tiki_product', pk='pid')
