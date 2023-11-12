from _init import *

from gta.modules import file_util

class WordTokenizer :
    def __init__(self) :
        pass
    
    def train(self, in_path, encoding) :
        in_file_paths = file_util.get_file_paths(in_path, True)
        for in_file_path in in_file_paths :
            print(in_file_path)


if __name__ == "__main__" :
    res_dir = '../../../../resources'
    in_path = f'{res_dir}/sample/sejong/'
    
    tokenizer = WordTokenizer()
    tokenizer.train(in_path, 'UTF-8')