import sys,re,operator,string

class InfoAbstaract():
    __metaclass__=OOP

    def info(self):
        return self.__class__.__name__

class DataStore(InfoAbstaract):
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

class StopWordManager(InfoAbstaract):

    def __init__(self):
        with open("../stop_words.txt") as f:
            self._stop_words=f.read().split(',')

            self._stop_words.extend(list(string.ascii_letters))

    def is_stop_word(self,word):
        return word in self._stop_words


    def info(self):
        return super(StopWordManager,self).info()+" my major is a"+self._stop_words.__class__.__name__

class WordFreqManager(InfoAbstaract):

    def __init__(self):
       self._word_freqs={}


    def increment_count(self, word):
        if word in self.__word_freqs:
            self.__word_freqs[word] += 1

        else:
            self.__word_freqs[word] = 1

    def sorted(self):
        return  sorted(self.__word_freqs.iteritems(),key=operator.itemgetter(1),reverse=True)

    
    def info(self):
        return super(WordFreqManager,self).info()+"my magor is "+self.__word_freqs.__class__.__name__


class WordFrequencyController(TFExercise):
    def __init__(self, path_to_file):
        self._storage_manager = DataStore(path_to_file)
        self._stop_word_manager = StopWordManager()
        self._word_freq_manager = WordFreqManager()

    def run(self):
        for w in self._storage_manager.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_manager.increment_count(w)

        word_freqs = self._word_freq_manager.sorted()
        for (w, c) in word_freqs[0:25]:
            print(w, ' - ', c)


#
# The main function
#
WordFrequencyController(sys.argv[1]).run()


     
