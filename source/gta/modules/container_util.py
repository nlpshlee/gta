from _init import *

from gta.modules.common_const import *
from gta.modules import string_util

###########################################################################################

def add_str_list_int(in_dict: dict, key_list: list, value: int, txt_option: int) :
    if in_dict != None :
        for i in range(len(key_list)) :
            key = str(key_list[i])
            add_str_int(in_dict, key, value, txt_option)

def add_str_int(in_dict: dict, key: str, value: int, txt_option: int) :
    if in_dict != None :
        if txt_option != TXT_OPTION.OFF :
            key = string_util.refine_txt(key, txt_option)

        if key in in_dict :
            value_prev = int(in_dict[key])
            in_dict[key] = value_prev + value
        else :
            in_dict[key] = value

###########################################################################################

'''
    key를 기준으로 정렬
        - is_reverse = False : 오름 차순
        - is_reverse = True : 내림 차순
'''
def sorted_dict_key(in_dict: dict, is_reverse: bool) :
    return dict(sorted(in_dict.items(), key=lambda item:item[0], reverse=is_reverse))

'''
    value를 기준으로 정렬
        - is_reverse = False : 오름 차순
        - is_reverse = True : 내림 차순
'''
def sorted_dict_value(in_dict: dict, is_reverse: bool) :
    return dict(sorted(in_dict.items(), key=lambda item:item[1], reverse=is_reverse))

'''
    key를 기준으로 오름 차순 정렬, value를 기준으로 내림 차순 정렬
'''
def sorted_dict(in_dict: dict) :
    return sorted_dict_value(sorted_dict_key(in_dict, False), True)
