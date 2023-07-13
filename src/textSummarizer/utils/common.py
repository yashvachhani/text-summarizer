import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        reads a yaml file and returns a ConfigBox

        Args:
            path_to_yaml(str): path to the yaml file     

        Raises:
            valueError: if the yaml file is empty
            e: empty file

        Returns:
            ConfigBox: ConfigBox object
    """
    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        creates directories in a list

        Args:
            path_to_directories(list): list of directories to create
            ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to False.

    """
    for directory in path_to_directories:
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"creating directory {directory}")


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """
        get the size of file in KB

        Args:
            path_to_file(Path): path to the file

        Returns:
            str: size of the file in KB
    """
    return str(round(os.path.getsize(path_to_file) / 1024))