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


    def words(self):
        return self._data.split()

    
    def info(self):
        return super(DataStorage,self).info()+":my major data is a"+self._data.__class__.__name__