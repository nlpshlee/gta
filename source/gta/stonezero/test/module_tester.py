from _init import *

from gta.modules import common_const, common_util, string_util


# logging test
msg = "this is log message"
common_util.logging(msg, common_const.LOG_OPTION.STDOUT)
common_util.logging(msg, common_const.LOG_OPTION.STDERR)


# error logging test
input_list = ["a", 1]
try :
    ''.join(input_list)
except Exception as e :
    call_path = 'module_tester.py'
    common_util.logging_error(call_path, e)


# string default refine test
text = 'Natural Language Processing'

txt_option = common_const.TXT_OPTION.LOWER
print(f'text : {text}, refine : {string_util.refine_txt(text, txt_option)}')

txt_option |= common_const.TXT_OPTION.RM_SPACE
print(f'text : {text}, refine : {string_util.refine_txt(text, txt_option)}')