from _init import *

from gta.modules.common_const import *
from gta.modules import string_util, container_util, file_util

class VOCAB_TOKEN :
    PAD = '<pad>'
    BOS = '<s>'
    EOS = '</s>'
    UNK = '<unk>'

class Vocab :
    def __init__(self, pad=VOCAB_TOKEN.PAD, bos=VOCAB_TOKEN.BOS, eos=VOCAB_TOKEN.EOS, unk=VOCAB_TOKEN.UNK) :
        self._pad = pad
        self._bos = bos
        self._eos = eos
        self._unk = unk
        self._txt_option = TXT_OPTION.LOWER

        self._token_to_idx = {}
        self._idx_to_token = {}
        self._idx = 0
        self.init_vocab()
    
    def init_vocab(self) :
        self._token_to_idx.clear()
        self._token_to_idx[self._pad] = 0
        self._token_to_idx[self._bos] = 1
        self._token_to_idx[self._eos] = 2
        self._token_to_idx[self._unk] = 3
        self._idx = len(self._token_to_idx)
        self._init_idx_to_token()
    
    def _init_idx_to_token(self) :
        self._idx_to_token.clear()

        for token in self._token_to_idx.keys() :
            idx = self._token_to_idx[token]
            self._idx_to_token[idx] = token

    def _refine_token(self, token) :
        return string_util.refine_txt(token, self._txt_option)
    
    def add(self, token) :
        token = self._refine_token(token)
        
        if not token in self._token_to_idx.keys() :
            self._token_to_idx[token] = self._idx
            self._idx_to_token[self._idx] = token
            self._idx += 1
    
    def get_size(self) :
        return len(self._token_to_idx)
    
    def get_idx_pad(self) :
        return self._token_to_idx[self._pad]

    def get_idx_bos(self) :
        return self._token_to_idx[self._bos]
    
    def get_idx_eos(self) :
        return self._token_to_idx[self._eos]
    
    def get_idx_unk(self) :
        return self._token_to_idx[self._unk]
    
    def get_idx(self, token) :
        token = self._refine_token(token)
        
        if token in self._token_to_idx.keys() :
            return self._token_to_idx[token]
        return self._token_to_idx[self._unk]

    def get_token(self, idx) :
        if idx in self._idx_to_token.keys() :
            return self._idx_to_token[idx]
        return self._unk
    
    def get_tokens(self, do_sort=True) :
        if do_sort :
            return container_util.sorted_dict_key(self._token_to_idx).keys()
        else :
            return self._token_to_idx.keys()
    
    def write_vocab(self, vocab_file_path, encoding, delim, do_sort_token=False, do_sort_idx=True) :
        if do_sort_token and do_sort_idx :
            sorted_vocab = container_util.sorted_dict(self._token_to_idx)
        elif do_sort_token :
            sorted_vocab = container_util.sorted_dict_key(self._token_to_idx)
        else :
            sorted_vocab = container_util.sorted_dict_value(self._token_to_idx)
        
        file_util.write_dict(sorted_vocab, vocab_file_path, encoding, delim)
    
    def load_vocab(self, vocab_file_path, encoding, delim) :
        self._token_to_idx.clear()
        self._idx_to_token.clear()
        file_util.load_dict(self._token_to_idx, True, vocab_file_path, encoding, delim)
        self._init_idx_to_token()
