from base.preprocess.tokenizers import Tokenizer
import re

class TitleTokenizer(Tokenizer):
    """
    Tokenize product title.
    """

    def tokenize_record(self, record):
        tokens = [word.lower() for word in record.split(' ')]
        return tokens

    def normalize_record(self, record):
        nomalized_record = re.sub('(?<=\d) (?=gb)', '', record)
        return nomalized_record

class PriceTokenizer(Tokenizer):
    """
    Tokenize product price.
    """

    def normalize_record(self, record):
        nomalized_record = re.sub('$đ￥', '', record)
        return nomalized_record
