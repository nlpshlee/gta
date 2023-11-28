from _init import *

from gta.modules import common_util, file_util

from gta.falcon.transformer.commons import tsfr_const, tsfr_util


class TSFRProperties :
    def __init__(self, default_flag=False) :
        self.res_dir = ""
        self.encoding = tsfr_const.ENCODING
        
        self.model_dir = "models"
        self.model_path = tsfr_const.MODEL_VERSION
    
    def set(self, res_dir: str, encoding: str, logging_flag: bool) :
        self.res_dir = res_dir
        self.encoding = encoding
        
        self.model_dir = os.path.join(self.res_dir, self.model_dir)

        self.model_path = os.path.join(self.model_dir, self.model_path)
        file_util.make_parent(os.path.join(self.model_path, "model.tmp"))
        
        self.model_log_path = os.path.join(self.model_path, "training.log")
        if logging_flag :
            tsfr_util.set_log_file_path(self.model_log_path, self.encoding)
    
    def _print(self) :
        tsfr_util.logging(f'\nres_dir : {self.res_dir}')
        tsfr_util.logging(f'model_dir : {self.model_dir}')
        tsfr_util.logging(f'model_path : {self.model_path}\n')


''' if __name__ == "__main__" :
    res_dir = "C:/nlpshlee/dev_env/git/repos/gta/resources/falcon/transformer/"
    encoding = "utf8"

    tsfr_properties = TSFRProperties()
    tsfr_properties.set(res_dir, encoding, True)
    
    tsfr_properties._print() '''