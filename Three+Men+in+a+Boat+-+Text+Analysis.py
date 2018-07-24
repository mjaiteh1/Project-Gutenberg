
# coding: utf-8

# In[103]:

from collections import defaultdict
from heapq import heappop, heappush
from nltk.corpus import stopwords
import re, string


def format_word(s):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude)

def remove_number(str):
    if re.sub(r'\d+', '', str) == str:
        return True
    return False

def get20MostFrequentWords(dic):
    heap = []
    mostFrequent = []
    for key, value in dic.items():
        heappush(heap,(-value,key))
    for i in range(20):
        mostFrequent.append([heappop(heap)[1],-heappop(heap)[0]])
    return mostFrequent
    
def get20LeastFrequentWords(dic):
    heap = []
    leastFrequent = []
    for key, value in dic.items():
        heappush(heap,(value,key))
    for i in range(20):
        leastFrequent.append([heappop(heap)[1],heappop(heap)[0]])
    return leastFrequent 

      
def getTotalUniqueWords(dic):
    return "There are "+ str(len(dic)) + " unique words in this book."


def get20MostInterestingFrequentWords(dic):
    heap = []
    mostFrequent = []
    stop_words = set(stopwords.words("english"))
    for key, value in dic.items():
        if key not in stop_words:
            heappush(heap,(-value,key))
    for i in range(20):
        mostFrequent.append([heappop(heap)[1],-heappop(heap)[0]])
    return mostFrequent



# In[121]:

#Analyze the progression of the words used on a chapter-by-chapter basis

'''
    Figure out how to break down a book by chapter.     
    
'''

book = open("308-0.txt","r")
dic = {}
chapter = 0
for line in book:
    if "CHAPTER" in line:
        chapter += 1
        dic[chapter] = line
    else:
        dic[chapter] += line

print("There are {} chapters in the Three Men in a Boat.".format(chapter))


# In[122]:

def getFrequencyOfWord(word,dic):
    #Word Dog 
    arr = []
    for key, value in dic.items():
        count = 0
        for line in value.split():
            if line.lower() == word:
                count += 1
        arr.append(count)
    return(arr)

getFrequencyOfWord("river",dic)


# In[124]:

def getChapterQuoteAppears(quote,dic):
    chapter = 0
    for key,value in dic.items():
        if quote in value:
            chapter = key
    if chapter == 0:
        return -1
    return chapter
#getChapterQuoteAppears('Oh, how delightful',dic)
getChapterQuoteAppears('I do not blame the dog',dic)


# In[117]:

def main():
    
    #Reading in text file 
    file = open("308.txt","r")
    
    '''
        Functions to implement 
        
        1. getTotalNumberOfWords()
        2. getTotalUniqueWords()
        3. get20MostFrequentWords()
        4. get20MostInterestingFrequentWords()
        5. get20LeastFrequentWords()
        6. getFrequencyOfWord()
        7. getChapterQuoteAppears()
        8. generateSentence()
    '''
    #Dictionary =
    characters = {"a","b","c","d","e","f","g",
                  "h","i","j","k","l","m","n",
                  "o","p","q","r","s","t",
                  "u","v","w","x","y","z"}
    wordCount = 0   
    dic = defaultdict(int)
    for line in file:
        #Use Regular expressions to just get the words
        for word in line.split():
            word = format_word(word)
            if remove_number(word):
                dic[word.lower()] += 1
                wordCount += 1
    print("Total Number of words:",wordCount)    
    #Using Heaps - For top 20, least frequent 
    print(get20MostFrequentWords(dic))
    print("---------------------")
    print(get20LeastFrequentWords(dic))
    print("---------------------")
    print(getTotalUniqueWords(dic))
    print("---------------------")
    print(get20MostInterestingFrequentWords(dic))

      
main()


