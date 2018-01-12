#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

FILENAME = "pass.dat"

_name = "***"
_pass = "***"

with open(FILENAME, "wb") as file:
    pickle.dump(_name, file)
    pickle.dump(_pass, file)

with open(FILENAME, "rb") as file:
    _name = pickle.load(file)
    _pass = pickle.load(file)
    print("Имя:", _name, "\tПароль:", _pass)
