from _init import *

from gta.falcon.transformer.commons import tsfr_const


class TSFRProperties :
    def __init__(self, default_flag=False) :
        self.res_dir = ""
        self.encoding = tsfr_const.ENCODING
        
        self.model_dir = "models"
    
    def set(self, res_dir: str, encoding: str, logging_flag: bool) :
        self.res_dir = res_dir
        self.encoding = encoding
        
        self.model_dir = os.path.join(self.res_dir, self.model_dir)
    
    def _print(self) :
        print(f'\nres_dir : {self.res_dir}')
        print(f'model_dir : {self.model_dir}\n')


''' if __name__ == "__main__" :
    res_dir = "C:/nlpshlee/dev_env/git/repos/gta/resources/falcon/transformer/"
    encoding = "utf8"

    tsfr_properties = TSFRProperties()
    tsfr_properties.set(res_dir, encoding, True)
    
    tsfr_properties._print() '''