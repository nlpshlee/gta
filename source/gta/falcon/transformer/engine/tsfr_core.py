from _init import *

from gta.falcon.transformer.commons import tsfr_const, tsfr_util
from gta.falcon.transformer.commons.tsfr_properties import TSFRProperties


class TSFRCore :
    def __init__(self, res_dir: str, encoding: str, training_flag: bool) :
        self.res_dir = res_dir
        self.encoding = encoding
        
        self.init(training_flag)
    
    def init(self, training_flag: bool) :
        # 사전, 모델, 로그 파일 등의 경로 설정
        self.set_properties(training_flag)
        
        tsfr_util.print_torch('TSFRCore.init()')
        self.tsfr_properties._print()
    
    def set_properties(self, logging_flag: bool) :
        self.tsfr_properties = TSFRProperties()
        self.tsfr_properties.set(self.res_dir, self.encoding, logging_flag)
    
    def set_params(self, conf_dict: dict, training_flag: bool) :
        if conf_dict is not None :
            tsfr_const.set_params(conf_dict)
            self.init(training_flag)


''' if __name__ == "__main__" :
    res_dir = 'C:/nlpshlee/dev_env/git/repos/gta/resources/falcon/transformer/'
    encoding = "utf8"
    training_flag = True

    tsfr_core = TSFRCore(res_dir, encoding, training_flag) '''