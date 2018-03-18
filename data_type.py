# -*- coding: utf-8 -*-


class Fund:
    code = ''
    name = ''
    values = {} #key-value

    def __init__(self, code):
        self.code = code
        self.name = ''
        self.values = {}

    def setCode(self, code):
        self.code = code

    def setName(self, name):
        self.name = name

    def addValue(self, date, value):
        self.values[date] = value

    def getValLen(self):
        return len(self.values)