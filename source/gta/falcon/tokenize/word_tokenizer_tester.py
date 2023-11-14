from _init import *

from gta.falcon.tokenize.word_tokenizer import WordTokenizer


res_dir = '../../../../resources'
vocab_file_path = f'{res_dir}/falcon/tokenize/word_tokenize.vocab'
encoding, delim = 'UTF-8', '\t'

tokenizer = WordTokenizer()
tokenizer.load_vocab(vocab_file_path, encoding, delim)

text = '내가 나를 알지 못하는 것이 나의 가장 큰 문제이다 娗'

idxs = tokenizer.tokenize(text)
print(f'idxs : {idxs}')

vocab = tokenizer.get_vocab()
tokens = [vocab.get_token(idx) for idx in idxs]
print(f'tokens : {tokens}')