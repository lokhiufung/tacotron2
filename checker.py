"""
check the availability of additional cleaners, i.e cantonese_cleaners, mandarin_cleaners
"""
import pandas as pd
from text.cleaners import cantonese_cleaners


def get_missing_chars(filename):
    df = pd.read_csv(filename, header=0)
    missing_chars = []

    for row in df.itertuples():
        try:
            text = cantonese_cleaners(row.transcript)
            print('DEBUG text {} jyutping {}'.format(row.transcript, text))
        except Exception as err:
            for char in row.transcript:
                try:
                    jyut = jyutping.get(char)[0]
                except Exception as err:
                    missing_chars.append(char)
                    print('ERROR char {}'.format(char))

    missing_chars = list(set(missing_chars))
    if missing_chars:
        with open('missing_char.txt', 'w') as f:
            f.write('\n'.join(missing_chars))
    else:
        print('DEBUG No missing chars found!')