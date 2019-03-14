import os, sys
import glob
import argparse
import numpy as np
import pandas as pd
import nltk,random

def parse_input_data(filename):
    '''

    :param filename:
            Require filename or path as input
    :return:
           Return list of sentences
    '''
    all_lines=[]
    all_POS=[]
    with open(filename, 'r') as f:
        for line in f:
            WP = [(x[0],x[1]) for x in [w.split('/') for w in line.split()]]
            sep_tup = list(zip(*WP))
            all_lines.append(' '.join(word for word in sep_tup[0]))
            all_POS.append(' '.join(pos for pos in sep_tup[1]))
    return all_lines, all_POS
def create_one_hot_vectors(los):
    '''

    :param los:
             List of sentences
    :return:
            dict of word with its one hot vector
    '''
    vocabulary = set()
    vector_dict = {}
    for sen in los:
        vocabulary = vocabulary.union(set(sen.split()))
    list_of_vocabulary = list(vocabulary)
    list_of_vocabulary += ['<start>']
    for count,i in enumerate(list_of_vocabulary):
        zero_array = np.zeros((len(list_of_vocabulary),), dtype=float)
        zero_array[count] = 1.0
        vector_dict.update({ i : zero_array})
    return vector_dict

def create_n_grams(los, n=3, start = None,end = None):
    '''

    :param los:
           list of sentences
    :param start:
           start line number
    :param end:
           end line number
    :return:
        Return n-grams

    '''
    Ngram_list = []
    for sen in los:
        Ngram_list.append(list(nltk.ngrams(sen.split(), n, pad_left=True, pad_right=False,
                                           left_pad_symbol='<start>', right_pad_symbol='<end>')))
    return Ngram_list

def convert_n_grams(n_grams, dict_of_vectors):
    '''

    :param n_grams:
            n-grams
    :param dict_of_vectors:
            dict of vocabulary vectors
    :return:
           return np array
    '''
    n_gram_one_hot = []
    for count, sent in enumerate(n_grams):

        for ng in sent:
            temp_vec = []
            for w in ng[:-1]:
                value = dict_of_vectors[w]
                temp_vec.extend(value)
            temp_vec.append(ng[-1])
            n_gram_one_hot.append(temp_vec)
    final_one_hot_array = np.array(n_gram_one_hot)
    return final_one_hot_array


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Convert text to features")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3,
                        help="The length of ngram to be considered (default 3).")
    parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                        default=0,
                        help="What line of the input data file to start from. Default is 0, the first line.")
    parser.add_argument("-E", "--end", metavar="E", dest="endline",
                        type=int, default=None,
                        help="What line of the input data file to end on. Default is None, whatever the last line is.")
    parser.add_argument("inputfile", type=str,
                        help="The file name containing the text data.")
    parser.add_argument("outputfile", type=str,
                        help="The name of the output file for the feature table.")
    parser.add_argument("-T", "--test-lines", dest="testlines",
                        type=int, default=10,
                        help="Number of lines should be used for testing.")
    parser.add_argument("-P" "--usepostags", action="store_true", default=False, dest='pos',
                        help="use pos tags instead of words")

    args = parser.parse_args()

    print("Loading data from file {}.".format(args.inputfile))
    all_sentences, all_POS_tags = parse_input_data(args.inputfile)


    if args.startline:
        print("Starting from line {}.".format(args.startline))
        if args.endline:
            print("Ending at line {}.".format(args.endline))
            if args.pos:
                actual_data = all_POS_tags[args.startline:args.endline]
                one_hot_dict = create_one_hot_vectors(actual_data)
            else:
                actual_data = all_sentences[args.startline:args.endline]
                one_hot_dict = create_one_hot_vectors(actual_data)
        else:
            print("Ending at last line of file.")
            if args.pos:
                actual_data = all_POS_tags[args.startline:]
                one_hot_dict = create_one_hot_vectors(actual_data)
            else:
                actual_data = all_sentences[args.startline:]
                one_hot_dict = create_one_hot_vectors(actual_data)
    else:
        if args.endline:
            print("Ending at line {}.".format(args.endline))
            if args.pos:
                actual_data = all_POS_tags[:args.endline]
                one_hot_dict = create_one_hot_vectors(actual_data)
            else:
                actual_data = all_sentences[:args.endline]
                one_hot_dict = create_one_hot_vectors(actual_data)

        else:
            print("Ending at last line of file.")
            if args.pos:
                actual_data = all_POS_tags
                one_hot_dict = create_one_hot_vectors(actual_data)
            else:
                actual_data = all_sentences
                print(len(actual_data))
                one_hot_dict = create_one_hot_vectors(actual_data)


    if args.testlines < len(actual_data) and args.ngram >= 2:
        random.shuffle(actual_data)
        test_data = actual_data[:args.testlines]
        train_data = actual_data[args.testlines:]

        print("Constructing {}-gram model.".format(args.ngram))
        train_n_grams = create_n_grams(train_data, args.ngram)
        test_n_grams = create_n_grams(test_data, args.ngram)
        one_hot_final_train_vec = convert_n_grams(train_n_grams, one_hot_dict)
        one_hot_final_test_vec = convert_n_grams(test_n_grams, one_hot_dict)
        print("Writing table to {}.".format(args.outputfile))
        df_train = pd.DataFrame(one_hot_final_train_vec)
        df_train.to_csv('train_'+args.outputfile+'.csv')
        df_test = pd.DataFrame(one_hot_final_test_vec)
        df_test.to_csv('test_'+args.outputfile+'.csv')
    elif not args.testlines and args.ngram >= 2:
        random.shuffle(actual_data)
        test_data = actual_data[:len(actual_data)/2]
        train_data = actual_data[len(actual_data)/2:]

        print("Constructing {}-gram model.".format(args.ngram))
        train_n_grams = create_n_grams(train_data, args.ngram)
        test_n_grams = create_n_grams(test_data, args.ngram)
        one_hot_final_train_vec = convert_n_grams(train_n_grams, one_hot_dict)
        one_hot_final_test_vec = convert_n_grams(test_n_grams, one_hot_dict)
        print("Writing table to {}.".format(args.outputfile))
        df_train = pd.DataFrame(one_hot_final_train_vec)
        df_train.to_csv('train_'+args.outputfile+'.csv')
        df_test = pd.DataFrame(one_hot_final_test_vec)
        df_test.to_csv('test_'+args.outputfile+'.csv')
    else:
        print('The Train data line should be less than the number of lines selected'
              ' and n-gram value should be greater than 2')

