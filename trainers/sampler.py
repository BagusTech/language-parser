import json, requests

#random stocks to load for sampling
stocks = ['CLD','BBGI']#,'AAPL','V','BP','FB','CAT','KHC','JNJ','AZN','TIPT','GOV']
stock_stream = 'https://api.stocktwits.com/api/2/streams/symbol/'

def pull_samples(stocks, use_sentiment = True):    
    samples = []
    for s in stocks:
        res = requests.get(stock_stream + s + '.json')
        messages = json.loads(res.text).get('messages')
        for m in messages:
            samples.append(m)
    
    if use_sentiment == True:
        out = []
        for m in samples:
            if m.get('entities').get('sentiment') != None:
                out.append((m.get('body'), m.get('entities').get('sentiment').\
                        get('basic')))
        return out
    else:
        #TODO: not sure how to auto classify without using sentiment, maybe just print
        pass
        
#pull_samples(stocks)