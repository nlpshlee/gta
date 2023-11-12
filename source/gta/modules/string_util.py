from _init import *

from gta.modules.common_const import *
from gta.modules import common_util

import hashlib

###########################################################################################

def is_empty(input: str, trim_flag: bool) :
    if input is None :
        return True
    
    if trim_flag :
        input = input.strip()
    
    if len(input) == 0 :
        return True
    
    return False

###########################################################################################

def trim(input_list: list, rm_empty_flag: bool) :
    if not rm_empty_flag :
        for i in range(len(input_list)) :
            if input_list[i] is None :
                input_list[i] = ""
            else :
                input_list[i] = str(input_list[i]).strip()
    else :
        result = []

        for i in range(len(input_list)) :
            if not is_empty(input_list[i], True) :
                result.append(str(input_list[i]).strip())
        
        return result

###########################################################################################

def refine_txt(input: str, txt_option: int) :
    if common_util.check_option(txt_option, TXT_OPTION.OFF) :
        return input

    if common_util.check_option(txt_option, TXT_OPTION.UPPER) :
        input = input.upper()
    elif common_util.check_option(txt_option, TXT_OPTION.LOWER) :
        input = input.lower()

    if common_util.check_option(txt_option, TXT_OPTION.RM_SPACE) :
        #input = input.replace(" ", "")
        input = ''.join(input.split()) # '\t', '\n' 등도 제거

    return input

def to_hash(input: str, encoding=ENCODING) :
    hash_obj = hashlib.sha1((input.encode(encoding)))
    #hash_obj = hashlib.sha256((input.encode(encoding)))
    
    hex_dig = hash_obj.hexdigest()
    return hex_dig

###########################################################################################
'''
def test_is_empty() :
    print(is_empty(None, True))
    print(is_empty("", True))
    print(is_empty(" \t\n", True))
    print(is_empty("ABC", True))
    print(is_empty(" ABC\t", True))
    print(is_empty("\tABC\n", True))
    print(is_empty(" \t\nABC \t\n", True))
    print()

    print(is_empty(None, False))
    print(is_empty("", False))
    print(is_empty(" \t\n", False))
    print(is_empty("ABC", False))
    print(is_empty(" ABC\t", False))
    print(is_empty("\tABC\n", False))
    print(is_empty(" \t\nABC \t\n", False))

def test_trim() :
    input_list = [None, "   ", " \t\nABC \t\n"]
    trim(input_list, False)

    for i in range(len(input_list)) :
        print(f"[{i}]\t[{input_list[i]}]")
    print()
    
    input_list = [None, " \t", " \tABC"]
    input_list_rm = trim(input_list, True)

    for i in range(len(input_list)) :
        print(f"[{i}]\t[{input_list[i]}]")
    print()

    for i in range(len(input_list_rm)) :
        print(f"[{i}]\t[{input_list_rm[i]}]")

def test_hash() :
    input = ("나는 이성희다."*50)
    print(f"input : {input}, to_hash : {to_hash(input)}")

if __name__ == "__main__" :
    #test_is_empty()
    #test_trim()
    test_hash()
'''