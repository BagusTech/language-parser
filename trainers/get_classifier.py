import sampler

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

class NaiveBayesClassy:
    
    def __init__(self, training_data = None):
        if training_data == None:
            self.training_data = sampler.pull_samples(sampler.stocks)
    
    def get_classifier(self, file = None):
        #make sure to download corpus with "python -m nltk.downloader all" prior to run 
        if file == None:
            classifier = NaiveBayesClassifier(self.training_data) 
            return classifier            
        else:
            #TODO test!
            classifier_f = open(file, "rb")
            classifier = pickle.load(classifier_f)
            classifier_f.close()
            return classifier

    def save_classifier(self, classifier, file):
        #TODO test
        save_classifier = open(file, "wb")
        pickle.dump(classifier, save_classifier)
        save_classifier.close()
        
    def featurize(self, sentence):
        vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in \
                    self.training_data]))
        featurized =  {i:(i in word_tokenize(sentence.lower())) for i in vocabulary}
        return featurized

test = NaiveBayesClassy()
cl = test.get_classifier()
blob = TextBlob('huge losses', classifier=cl)
print(blob.classify())