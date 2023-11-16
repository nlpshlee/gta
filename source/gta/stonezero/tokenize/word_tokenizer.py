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
