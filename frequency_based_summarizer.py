from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut 
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut 
    self._stopwords = set(list(stopwords.words('english')) + list(punctuation))

  def _compute_frequency(self, sentences):
    freq = defaultdict(int)
    for words in sentences:
      for word in words:
        if word.strip('\t') not in self._stopwords:
          freq[word.strip('\t')] += 1
    freq = self._freq_normalize(freq)     
    return freq     

  def _freq_normalize(self, freq_dict):
    m = float(max(freq_dict.values()))
    for w in freq_dict.keys():
      freq_dict[w] = freq_dict[w] / m
      if freq_dict[w] > self._max_cut or freq_dict[w] <= self._min_cut:
        del freq_dict[w]
    return freq_dict  
  
  def _stemmmerfunc(self, word_sent):
    words_sent = []
    # stemmer = PorterStemmer()
    stemmer = WordNetLemmatizer()
    for words in word_sent:
      for word in words:
        # words_sent.add(stemmer.stem_word(word))
        words_sent.append(stemmer.lemmatize(word))
    return list(words_sent)  


  
  def summarize(self, text, n=None):
    """
      Return a list of n sentences 
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    if not n:
      n = len(sents)/2 + 1
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    word_stemmed = self._stemmmerfunc(word_sent)
    print word_stemmed
    self._freq = self._compute_frequency(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)    
    return [sents[j] for j in sents_idx]


  # def _tfidf(self, )


  def _rank(self, ranking, n):
    """ return the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)

if __name__ == '__main__':
  import requests
  from bs4 import BeautifulSoup
  html = requests.get('http://timesofindia.indiatimes.com/business/\
                    india-business/Delhi-budget-tomorrow-boost-for-education-transport-likely\
                    /articleshow/51569096.cms').content
  soup = BeautifulSoup(html,'html.parser')
  string = ''
  for sents in soup.find_all('p')[0:10]:
    string += sents.text
  # print len(sent_tokenize(string))  
  summarizerr = FrequencySummarizer()
  # print ' '.join(summarizerr.summarize(string))
  summarizerr.summarize(string)

