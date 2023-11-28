from _init import *

from gta.modules import json_util

from gta.stonezero.transformer.engine.tsfr_core import TSFRCore

class TSFRRunner :
    def __init__(self, conf_path: str, res_dir: str, encoding: str) :
        self.conf_path = conf_path
        self.res_dir = res_dir
        self.encoding = encoding
    
    def init_core(self, training_flag=False) :
        self.tsfr_core = TSFRCore(res_dir, encoding, training_flag)
        
        # 파라미터 변경 (conf 파일이 주어지는 경우)
        conf_dict = json_util.load_file_to_dict(self.conf_path, self.encoding)
        self.tsfr_core.set_params(conf_dict, training_flag)


if __name__ == "__main__" :
    home_dir = 'C:/dev/git/repos/gta'
    conf_path = os.path.join(home_dir, 'conf/stonezero/tsfr_conf.json')
    res_dir = os.path.join(home_dir, 'resources/stonezero/transformer/')
    encoding = "utf8"
    training_flag = True
    
    tsfr_runner = TSFRRunner(conf_path, res_dir, encoding)
    tsfr_runner.init_core(training_flag)
