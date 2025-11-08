#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from pathlib import Path


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is the Project Root
DATA_DIR = str(Path(ROOT_DIR) / "Benchmark")  # This is the data of this project
OUTPUT_DIR = str(Path(ROOT_DIR) / "output")  # This is the output of this project


class PathUtil:

    @staticmethod
    def benchmark_data(filename: str, ext: str):
        path = Path(DATA_DIR)
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)


    @staticmethod
    def output_result_data(filename: str, ext: str):
        path = Path(OUTPUT_DIR)
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)
