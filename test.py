import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3,
                        help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features in the test data.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the saved model file.")
    args = parser.parse_args()
    print("Loading data from file {}.".format(args.datafile))
    df_csv = pd.read_csv(args.datafile, index_col=0)
    # split data frame to dictionary
    df_dict = df_csv.to_dict('split')
    #all row data
    data = df_dict['data']
    #convert data to np array
    data = np.array(data)
    #separate data and feature label
    X, y = data[:, :-1], data[:, -1]
    # array to a float dtype before using it in scikit-learn
    X = X.astype(np.float64)
    print("Loading model from file {}.".format(args.modelfile))
    LRF = pickle.load(open(args.modelfile, 'rb'))
    print("Testing {}-gram model.".format(args.ngram))
    predictions = LRF.predict(X)
    print("Accuracy is ...")
    print(accuracy_score(y, predictions))
    plp = np.array(LRF.predict_log_proba(X))
    pp =  np.array(LRF.predict_proba(X))
    calculated_entropies =[]
    predicted_probabilities = [a*b for logs,probs in zip(list(plp),list(pp)) for a,b in zip(list(-logs),list(probs))]
    all_entropies = np.array_split(predicted_probabilities, len(pp))
    for i in all_entropies:
        calculated_entropies.append(sum(i))
    entropy = sum(calculated_entropies) / len(calculated_entropies)
    print("Perplexity is...")
    perplexity = 2**entropy
    print(perplexity)
