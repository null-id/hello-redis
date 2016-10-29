#!/usr/bin/env python
# coding=utf-8

import requests

def count_text_len(url):
    return len(requests.get(url).text.split())


