import json


nemo_train_data = './data_nemo/train.json'
nemo_eval_data = './data_nemo/train.json'


def __process_line(line):
    json_data = json.loads(line)
    return '{}|{}'.format(json_data['audio_filepath'], json_data['text'])


def convert_data(data_path, output_path):
    with open(data_path, 'r') as f:
        data = [__process_line(line) for line in f]

    with open(output_path, 'w') as f:
        f.write('\n'.join(data))


convert_data(nemo_train_data, './train_tacotron2.txt')
convert_data(nemo_eval_data, './dev_tacotron2.txt')
