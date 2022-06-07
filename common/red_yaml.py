import yaml
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

data_file_path = os.path.join(BASE_PATH,"data","casedata.yml")


def red_yaml(data_location):
    data = yaml.safe_load(open(data_file_path,encoding="utf8"))[data_location]
    return data