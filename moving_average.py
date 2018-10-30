#Function to get the prior sentiment score of the context word from the sentiment lexicon-SentiWordNet
def prior_score(context_word):
	lexicon=load_lexicon()
	for i in range(0,X.shape[0]):
		if X[i][0]==context_word:
			return X[i][1]