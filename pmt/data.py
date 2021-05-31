from base.structures.data import Feature
from pmt.tokenizers import TitleTokenizer, PriceTokenizer


class Title(Feature):

    def __init__(self, value, weight):
        super().__init__(value=value, weight=weight)
        self.tokenizer = TitleTokenizer()

class Price(Feature):

    def __init__(self, value, weight):
        super().__init__(value=value, weight=weight)
        self.tokenizer = PriceTokenizer()
