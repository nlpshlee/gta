from _init import *

from gta.stonezero.tokenize.word_tokenizer import WordTokenizer

res_dir = '../../../../resources/'
in_file_path = f'{res_dir}/sample/sejong/output/sentence_freq.dict'
out_file_path = f"{res_dir}/stonezero/tokenize/word_tokenize.vocab"
encoding, delim = 'UTF-8', '\t'


tokenizer = WordTokenizer()

# vocab 처음 만들 경우
# tokenizer.train(in_file_path, encoding, delim, out_file_path)

# 학습한 vocab이 있을 경우
tokenizer.load_vocab(out_file_path, encoding, delim)
# print(tokenizer.id_to_token)

text = '지금 우리가 카페에서 공부하고 있는 이유는 앞서 공부를 정말 많이 한 선배들을 어떻게든 따라잡고 나도 한가닥 좀 해보려고 발버둥 치는 것이다.'
result = tokenizer.tokenize(text)

print(result)


# 스페셜 토크는 무시
decoded = tokenizer.decode(result)
print(decoded)

# 스페셜토큰도 디코딩
decoded2 = tokenizer.decode(result, decode_special_tokens=True)
print(decoded2)
