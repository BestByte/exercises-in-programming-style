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


class StopWordManager():

    def __init__(self):
        with open('../stop_words.txt') as f:
            self._stop_words=f.read().split(',')

        self._stop_words.extend(list(string.ascii_lowercase))

    def is_stop_word(self,word):
        return  word in self._stop_words

    def info(self):
        return super(StopWordManager,self).info()+":My major data is a"+self._stop_words.__class__.__name__



