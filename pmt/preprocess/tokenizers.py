from matchingframework.preprocess.tokenizers import Tokenizer
import re

class TitleTokenizer(Tokenizer):
    """
    Tokenize product title.
    """

    def tokenize_record(self, record):
        tokens = [word.lower() for word in record.split()]
        return tokens

    def normalize_record(self, record):
        nomalized_record = record
        nomalized_record = re.sub('\W', ' ', nomalized_record)
        return nomalized_record

class BrandTokenizer(Tokenizer):
    """
    Tokenize product brand.
    """

    def tokenize_record(self, record):
        tokens = [record.lower()]
        return tokens

    def normalize_record(self, record):
        return record
