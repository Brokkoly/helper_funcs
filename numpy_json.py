import numpy as np
import json,codecs


def ndarray_to_json_file(input_array,file_path):
    b = input_array.tolist()
    json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
    ###code taken from http://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable, credit to user travelingbones

def json_file_to_ndarray(file_path):

    json_text = codecs.open(file_path, 'r',encoding='utf-8').read()
    a = json.loads(json_text)
    return np.array(a)



###code taken from http://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable, credit to user travelingbone
