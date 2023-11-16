from _init import *

from gta.falcon.tokenize.word_tokenizer import WordTokenizer


res_dir = '../../../../resources'
train_file_path = f'{res_dir}/sample/sejong/output/sentence_freq.dict'
vocab_file_path = f'{res_dir}/falcon/tokenize/word_tokenize.vocab'
encoding, delim = 'UTF-8', '\t'

# vocab 파일 생성
tokenizer1 = WordTokenizer()
tokenizer1.train(train_file_path, encoding, delim)
tokenizer1.write_vocab(vocab_file_path, encoding, delim)

# vocab 파일 로드 후, 토크나이징 수행
tokenizer2 = WordTokenizer()
tokenizer2.load_vocab(vocab_file_path, encoding, delim)

text = '내가 나를 알지 못하는 것이 나의 가장 큰 문제이다 娗'

idxs = tokenizer2.tokenize(text)
print(f'idxs : {idxs}')

vocab = tokenizer2.get_vocab()
tokens = [vocab.get_token(idx) for idx in idxs]
print(f'tokens : {tokens}')
