import os
from datetime import datetime

def validate_and_timestamp_output_paths(log_txt: str, error_txt: str, results_json: str) -> (str, str, str):
    for path in [log_txt, error_txt, results_json]:
        dir_name = os.path.dirname(path)
        if dir_name != '' and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if '.' in os.path.split(path)[-1]: # the first letter of the last part of the path must not be a dot '.'
            raise Exception(f'Path {path} contains an extension')

    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    log_txt += f'_{timestamp}.txt'
    error_txt += f'_{timestamp}.txt'
    results_json += f'_{timestamp}.json'
    return log_txt, error_txt, results_json