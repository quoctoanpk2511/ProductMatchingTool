from base.preprocess.tokenizers import DefaultTokenizer
import re


class TitleTokenizer(DefaultTokenizer):
    """
    Tokenize product title.
    """

    def normalize_record(self, record):
        nomalized_record = re.sub('(?<=\d) (?=gb)', '', record)
        return nomalized_record

class PriceTokenizer(DefaultTokenizer):
    """
    Tokenize product price.
    """

    def normalize_record(self, record):
        nomalized_record = re.sub('$đ￥', '', record)
        return nomalized_record
