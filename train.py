import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the file to which you write the trained model.")

    args = parser.parse_args()

    print("Loading data from file {}.".format(args.datafile))
    df_csv = pd.read_csv(args.datafile, index_col=0)
    print("Training {}-gram model.".format(args.ngram))
    df_dict = df_csv.to_dict('split')
    data = df_dict['data']
    data = np.array(data)
    X, y = data[:, :-1], data[:, -1]
    clf = LogisticRegression(solver='lbfgs',max_iter=10000,
                              multi_class='multinomial').fit(X, y)

    print("Writing table to {}.".format(args.modelfile))
    with open(args.modelfile, 'wb') as f:
        model = pickle.dump(clf, f)


