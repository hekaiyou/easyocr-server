import sys
import easyocr
from time import time
from json import dump

# https://www.jaided.ai/easyocr/
# https://github.com/JaidedAI/EasyOCR
# python ocr.py examples/chinese.jpg ch_sim,en

img_filename = sys.argv[1]
language = sys.argv[2].split(',')
ocr_results = {
    'language': language,
    'init_take': 0.0,
    'ocr_take': 0.0,
    'summary_result': [],
    'full_result': [],
    'error': ''
}
try:
    init_start = time()
    # 只需要运行一次即可将模型加载到内存中
    reader = easyocr.Reader(
        language,
        gpu=False,
        model_storage_directory='model/.',
        user_network_directory='model/.',
    )
    init_end = time()
    ocr_results['init_take'] = init_end - init_start
    ocr_start = time()
    result = reader.readtext(img_filename)
    for _res in result:
        ocr_results['summary_result'].append(_res[1])
        _res_0_conversion = [[0, 0], [0, 0], [0, 0], [0, 0]]
        for _i in range(len(_res[0])):
            _res_0_conversion[_i] = [int(_res[0][_i][0]), int(_res[0][_i][1])]
        ocr_results['full_result'].append({
            'bounding_box': _res_0_conversion,
            'text_detected': _res[1],
            'confident_level': _res[2],
        })
    ocr_end = time()
    ocr_results['ocr_take'] = ocr_end - ocr_start
except Exception as e:
    ocr_results['error'] = str(e)
with open(f'{img_filename}.json', 'w', encoding='UTF-8') as f:
    dump(ocr_results, f)
