'''
Created on Apr 24, 2017

@author: lissnerlistner
'''
import nltk

pos_twits = [('$WATT speculating about $AAPL WWDC in early June: beta of ios 11 will be released - wondering if code snipets will reveal anything', 'positive'),
            ('$AAPL Punditry 101: The Echo is a huge success. The Apple Watch isn’t. This despite the fact that Apple sold more Watches.', 'positive'),
            ('@Isildur1 Wink Wink 😉or should I say Slim. $AAPL, $FB. Thanks for the bearish post 🚀 after ER report', 'positive'),
            ('$AAPL prediction ... open at $144+ tomorrow', 'positive'),
            ('$AAPL John Gruber nails it.', 'positive'),
            ('$AAPL $FB missed slim in both the boards today', 'positive'),
            ('$AAPL $FB momentum confirmed. Decent volume on broad market rise.  See you at 150.', 'positive'),
            ('$AAPL Nice day, looking for more upside tomorrow!', 'positive'),
            ('$AAPL can I see $145 tomorrow pretty please', 'positive')]

neg_twits = [('$AAPL $fb Seems they overly hyped the markets today....$UVXY bounce tomorrow and we sell off tomorrow', 'negative'),
             ('$AAPL $fb Looking for a pullback tomorrow', 'negative')]

twits = []

for (words, sentiment) in pos_twits + neg_twits:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    twits.append((words_filtered, sentiment))

def get_words_in_twits(twits):
    all_words = []
    
    for (words, sentiment) in twits:
        all_words.extend(words)
    
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
        
    return features
'''
def train(labeled_featuresets, estimator=nltk.ELEProbDist):
    label_prodlist = estimator(label_freqdist)
    feature_probdist = {}
    
    return nltk.NaiveBayesClassifier(label_prodlist, feature_probdist)
'''

word_features = get_word_features(get_words_in_twits(twits))
training_set = nltk.classify.apply_features(extract_features, twits)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print(classifier.classify(extract_features('$fb is way better than $appl')))