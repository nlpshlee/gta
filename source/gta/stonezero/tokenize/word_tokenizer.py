from _init import *

from gta.modules.common_const import *
from gta.modules import file_util


class WordTokenizer :
    def __init__(self) :
        self.vocab = {}
    
    def train(self, in_file_path, encoding, delim, out_file_path) :
        in_file = file_util.open_file(in_file_path, encoding, 'r')

        txt_list = []

        self.vocab = {"<pad>" : 0,
                      "<unk>" : 1,
                      "<sos>" : 2,
                      "<eos>" : 3}

        i = 4
        
        while 1 :
            line = in_file.readline()
            if not line :
                break

            sentence = line.split('\t')[0]
            for word in sentence.split(" "):
                if word not in self.vocab.keys():
                    self.vocab[word] = i
                    i += 1

        
        file_util.write_dict(self.vocab, out_file_path, encoding, delim)
    
    
    def tokenize(self, txt:str, out_file_path, max_length = 30):
        txt_ = "<SOS> " + txt + " <EOS>"
        tokens = txt_.split(" ")
        vocab = {}

        file_util.load_dict(vocab, True, out_file_path, txt_option=TXT_OPTION.UPPER)
        result = []
    
        for i in range(max_length):
            if  i < len(tokens):
                if tokens[i] not in vocab.keys():
                    result.append(vocab["<UNK>"])
                else:
                    result.append(vocab[tokens[i]])
            else:
                result.append(vocab["<PAD>"])
    
        return result
        
        


if __name__ == "__main__" :
    res_dir = '../../../../resources/'
    in_file_path = f'{res_dir}/sample/sejong/output/sentence_freq.dict'
    out_file_path = f"{res_dir}/stonezero/tokenize/word_tokenize.vocab"

    tokenizer = WordTokenizer()
    tokenizer.train(in_file_path, 'UTF-8', '\t', out_file_path)

    text = '지금 우리가 카페에서 공부하고 있는 이유는 앞서 공부를 정말 많이 한 선배들을 어떻게든 따라잡고 나도 한가닥 좀 해보려고 발버둥 치는 것이다.'
    result = tokenizer.tokenize(text, out_file_path)

    print(result)


