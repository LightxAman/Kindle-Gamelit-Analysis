# TODO: Implement utils.py

import yaml
import time
import random


def load_config(path="config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def wait(min_s=2, max_s=5):
    time.sleep(random.uniform(min_s, max_s))
