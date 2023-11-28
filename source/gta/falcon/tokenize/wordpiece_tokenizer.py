from _init import *

from tokenizers import BertWordPieceTokenizer

class WordPieceTokenizer :
    def __init__(self):
        pass
    




res_dir = '../../../../resources'
train_path = f'{res_dir}/sample/korpora/nsmc/nsmc_train.txt'
model_path = f'{res_dir}/falcon/tokenize/wordpiece_tokenize'

# tokenizer = BertWordPieceTokenizer(lowercase=True)
# tokenizer.train(files=[train_path], vocab_size=10000)
# tokenizer.save_model(model_path)

tokenizer = BertWordPieceTokenizer(
    vocab_file=model_path,
    clean_text=True,
    handle_chinese_chars=True,
    strip_accents=False, # Must be False if cased model
    lowercase=False,
    wordpieces_prefix="##"
)