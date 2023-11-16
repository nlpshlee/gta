from _init import *

from gta.stonezero.tokenize.word_tokenizer import WordTokenizer

res_dir = '../../../../resources/'
in_file_path = f'{res_dir}/sample/sejong/output/sentence_freq.dict'
out_file_path = f"{res_dir}/stonezero/tokenize/word_tokenize.vocab"

tokenizer = WordTokenizer()
tokenizer.train(in_file_path, 'UTF-8', '\t', out_file_path)

text = '지금 우리가 카페에서 공부하고 있는 이유는 앞서 공부를 정말 많이 한 선배들을 어떻게든 따라잡고 나도 한가닥 좀 해보려고 발버둥 치는 것이다.'
result = tokenizer.tokenize(text, out_file_path)

print(result)
