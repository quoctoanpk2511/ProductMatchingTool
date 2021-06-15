from matchingframework.structures.data import Feature
from pmt.preprocess.tokenizers import TitleTokenizer, BrandTokenizer


class Title(Feature):

    def __init__(self, field_name, weight):
        super().__init__(field_name=field_name, weight=weight)
        self.tokenizer = TitleTokenizer()

class Brand(Feature):

    def __init__(self, field_name, weight):
        super().__init__(field_name=field_name, weight=weight)
        self.tokenizer = BrandTokenizer()
