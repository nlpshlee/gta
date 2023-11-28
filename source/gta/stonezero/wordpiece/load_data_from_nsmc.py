from Korpora import Korpora

nsmc = Korpora.load('nsmc', force_download=True)

import os


def write_lines(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(f'{line}\n')
    
write_lines('./content/train.txt', nsmc.train.get_all_texts())
write_lines('./content/test.txt', nsmc.test.get_all_texts())