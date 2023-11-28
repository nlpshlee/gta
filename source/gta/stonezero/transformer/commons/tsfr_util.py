from _init import *

from gta.modules import common_util, file_util

from gta.stonezero.transformer.commons import tsfr_const

###########################################################################################

LOG_FILE_PATH = None
ENCODING = None

def set_log_file_path(log_file_path: str, encoding: str) :
    global LOG_FILE_PATH
    global ENCODING

    LOG_FILE_PATH = log_file_path
    ENCODING = encoding

###########################################################################################

def logging(msg: str, log_option=tsfr_const.LOG_OPTION) :
    common_util.logging(msg, log_option)

    if LOG_FILE_PATH != None :
        file = file_util.open_file(LOG_FILE_PATH, ENCODING, 'a')
        file.write(f"{msg}\n")
        file.close()

def logging_error(msg: str) :
    logging(f"### (ERROR) {msg}", tsfr_const.LOG_OPTION_ERROR)

def print_torch(call_path: str) :
    logging(f"\n{call_path} --> tsfr_util.print_torch() torch version : {torch.__version__}")

    if torch.cuda.is_available() :
        logging(f"{call_path} --> tsfr_util.print_torch() available torch.cuda.device count : {torch.cuda.device_count()}")
        logging(f"{call_path} --> tsfr_util.print_torch() current torch.cuda.device : {torch.cuda.current_device()}")
        logging(f"{call_path} --> tsfr_util.print_torch() device name : {torch.cuda.get_device_name(tsfr_const.TORCH.DEVICE)}")
    else :
        logging(f"{call_path} --> tsfr_util.print_torch() gpuNum : {tsfr_const.TORCH.GPU_NUM} is not avaliable, set torch.device : cpu")
