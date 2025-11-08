#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os


class DataUtils:
    @staticmethod
    def save_json(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_json(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_cache(path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                cache = json.load(f)
        else:
            cache = {}
        return cache
