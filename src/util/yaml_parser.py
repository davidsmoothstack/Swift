from dataclasses import dataclass
import json
from logging import Logger
from collections import namedtuple
from tempfile import NamedTemporaryFile
import yaml


@dataclass(frozen=True)
class YamlObject:
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def read_yaml(file_path) -> YamlObject:
    with open(file_path, "r") as stream:
        try:
            loaded_yaml = yaml.safe_load(stream)
            yaml_obj = json.loads(json.dumps(loaded_yaml),
                                  object_hook=YamlObject)

            return yaml_obj
        except yaml.YAMLError as exc:
            Logger.exception("")
