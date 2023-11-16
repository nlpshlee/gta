from _init import *

from gta.modules import file_util, string_util

from gta.falcon.tokenize.vocab import Vocab

class WordTokenizer :
    def __init__(self) :
        self._vocab = Vocab()

    def _init_vocab(self) :
        self._vocab.init_vocab()
    
    def get_vocab(self) -> Vocab :
        return self._vocab

    def train(self, in_file_path, encoding, delim, do_init_vocab=False) :
        if do_init_vocab :
            self._init_vocab()
        
        in_file = file_util.open_file(in_file_path, encoding, 'r')
        while 1 :
            line = in_file.readline()
            if not line :
                break
            
            line = file_util.preprocess(line)
            temp = string_util.trim(line.split(delim), True)
            line = temp[0]
            
            words = line.split()
            for word in words :
                self._vocab.add(word)

    def write_vocab(self, vocab_file_path, encoding, delim) :
        self._vocab.write_vocab(vocab_file_path, encoding, delim)
    
    def load_vocab(self, vocab_file_path, encoding, delim) :
        self._vocab.load_vocab(vocab_file_path, encoding, delim)
    
    def tokenize(self, line) :
        words = line.split()
        return [self._vocab.get_idx(word) for word in words]
