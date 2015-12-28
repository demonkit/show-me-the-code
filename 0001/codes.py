#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid


NUMBER_OF_CODES = 200


for num in range(NUMBER_OF_CODES):
    print uuid.uuid4().get_hex()
