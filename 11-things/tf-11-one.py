import sys,re,operator,string

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
        return super(DataStore,self)