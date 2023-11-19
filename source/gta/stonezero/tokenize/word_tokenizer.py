from _init import *

from gta.modules.common_const import *
from gta.modules import file_util


class WordTokenizer :
    def __init__(self) :
        self.vocab = {}
        self.id_to_token = {}
    
    def train(self, in_file_path, encoding, delim, out_file_path) :
        in_file = file_util.open_file(in_file_path, encoding, 'r')

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
        self.id_to_token = {self.vocab[key]:key for key in self.vocab.keys()}
            

        
        file_util.write_dict(self.vocab, out_file_path, encoding, delim)

    def load_vocab(self, vocab_file_path, encoding, delim):
        file_util.load_dict(self.vocab, True, vocab_file_path, encoding=encoding, delim=delim, txt_option=TXT_OPTION.UPPER)
        self.id_to_token = {self.vocab[key]:key for key in self.vocab.keys()}
    
    def tokenize(self, txt:str, max_length = 30):
        txt_ = "<SOS> " + txt + " <EOS>"
        tokens = txt_.split(" ")
        
        result = []
    
        for i in range(max_length):
            if  i < len(tokens):
                if tokens[i] not in self.vocab.keys():
                    result.append(self.vocab["<UNK>"])
                else:
                    result.append(self.vocab[tokens[i]])
            else:
                result.append(self.vocab["<PAD>"])
    
        return result
    
    def decode(self, ids:list, decode_special_tokens=False):
        
        result = ""
        if not decode_special_tokens:
            for id in ids:
                if id not in [0, 1, 2, 3]:
                    _id = self.id_to_token[id] + " "
                    result += _id
        else:
            for id in ids:
                _id = self.id_to_token[id]+ " "
                result += _id
        
        return result
            
        
