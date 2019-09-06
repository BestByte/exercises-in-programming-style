import sys,re,operator,string

class InfoAbstaract():
    __metaclass__=OOP

    def info(self):
        return self.__class__.__name__

class DataStore():
    '''

    '''
    def __init__(self,path_to_file):
        with open(path_to_file) as f:
            self._data=f.read()

        pattern=re.compile('[\W_]+')
        self._data=pattern.sub('',self._data).lower()


    def words(self):
        '''
        '''
        return self._data.split()


    def info(self):
        return super(DataStore,self).info()+"My major data is a "+self._data.__class__.__name__

