from _init import *

from gta.modules import common_const

ENCODING = "utf8"
DELIM_KEY = "\t"

TXT_OPTION_CASE = common_const.TXT_OPTION.UPPER

LOG_OPTION = common_const.LOG_OPTION.STDOUT
LOG_OPTION_ERROR = common_const.LOG_OPTION.STDERR

NULL_STR = "#NULL#"
NULL_INT = -99999

ANNOTATION_MARK = '#'

class TORCH :
    SEED = 777
    GPU_NUM = 0

    DEVICE = torch.device(f"cuda:{GPU_NUM}" if torch.cuda.is_available() else "cpu")
    if torch.cuda.is_available() :
        torch.cuda.set_device(DEVICE)

    MODEL_NAME = "model.state"
    OPTIM_NAME = "optimizer.state"

def set_params(conf_dict: dict) :
    if "params" in conf_dict :
        params_dict = conf_dict["params"]

        if "torch" in params_dict :
            _set_params_torch(params_dict["torch"])

def _set_params_torch(params_dict: dict) :
    if "gpuNum" in params_dict :
        TORCH.GPU_NUM = int(params_dict["gpuNum"])

        TORCH.DEVICE = torch.device(f"cuda:{TORCH.GPU_NUM}" if torch.cuda.is_available() else "cpu")
        if torch.cuda.is_available() :
            torch.cuda.set_device(TORCH.DEVICE)
