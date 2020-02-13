"""
check the availability of additional cleaners, i.e cantonese_cleaners, mandarin_cleaners
"""
import time
from tqdm import tqdm
import pandas as pd

from opencc import OpenCC
import jyutping
from jyutping import utils

from text.cleaners import cantonese_cleaners


def get_missing_chars(filename):
    df = pd.read_csv(filename, header=0)
    missing_chars = []

    for row in df.itertuples():
        try:
            text = cantonese_cleaners(row.transcript)
            # print('DEBUG transcript {} text {}'.format(row.transcript, text))
        except Exception as err:
            print('ERROR transcript {}'.format(row.transcript))
            for char in row.transcript:
                jyut = jyutping.get(char)[0]
                if jyut is None:
                    missing_chars.append(char)
                    print('ERROR char {}'.format(char))

    missing_chars = list(set(missing_chars))
    if missing_chars:
        with open('missing_char.txt', 'w') as f:
            f.write('\n'.join(missing_chars))
    else:
        print('DEBUG No missing chars found!')


def get_jyutping_of_missing_chars(missing_char_txt, results_txt='./results.txt'):
    cc = OpenCC('hk2s')

    total = 905

    results = []
    with open(missing_char_txt, 'r') as f:
        for char in tqdm(f, total=total):
            char = char.rstrip()
            try:
                jyut = utils.get_jyutping_from_api(char, resource='jyut.net')
                if jyut == '':
                    jyut = utils.get_jyutping_from_api(char, resource='ctext')
                    time.sleep(0.01)
                if jyut:
                    results.append('\t'.join((char, cc.convert(char), jyut)))
                else:
                    print('ERROR char {} is still missing'.format(char))
            except Exception as err:
                print('Error char {} err {}'.format(char, err))

    if results:
        with open(results_txt, 'w') as f:
            f.write('\n'.join(results))
        print('DEBUG {} chars have been added!'.format(len(results)))
