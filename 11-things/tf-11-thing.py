#!/usr/bin/env python
import sys,re,operator,string

class DataStorage():
    '''

    '''
    def __init__(self,path_to_file:string):
        with open(path_to_file) as f:
            self._data=f.read()

        pattern=re.compile('[\W_]+')

        self._data=pattern.sub("", self._data).lower()