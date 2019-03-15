

2
68.18# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Hemanth Kumar Battula

## Additional instructions

Document here additional command-line instructions or other details you
want us to know about running your code.

## Reporting for Part 4

### Examples to Run code:
python gendata.py -S 1000 -E 1200 -T 120 brown-rga.txt output -N 2

python train.py -N 2 train_output.csv picklefile

python test.py -N 2 test_output.csv picklefile


| Arguments                        | Accuracy              | Perplexity              |
|----------------------------------|-----------------------|-------------------------|
| -S 500 -E 1000 -T 200  -N 2      | 0.11596385542168675   | 64.44424759874161       |
| -S 500 -E 1000 -T 200  -N 3      | 0.1311178247734139    | 62.50996446954039       |
| -S 500 -E 1000 -T 200  -N 4      | 0.12851800826608936   | 61.084440697869546      |
| -S 500 -E 1000 -T 200  -N 5      | 0.12584132163981235   | 62.06472556249275       |
| -S 1000 -E 1200 -T 120 -N 2      | 0.10036231884057971   | 48.89071413734563       |
| -S 1000 -E 1200 -T 120 -N 3      | 0.10323741007194244   | 47.503188532155484      |
| -S 1000 -E 1200 -T 120 -N 4      | 0.11168070303917979   | 51.32840216732968       |
| -S 1000 -E 1200 -T 120 -N 5      | 0.11681109185441942   | 48.22276131048413       |


Preplexity is the measure of how well an n-gram predict the next type in the given test set based on the training model.
A good language model is something which predicts correctly. It usually gives high probability values and low preplexity scores.
When the experiment is carried on the given data with 500 lines, the preplexity decreased as the n-grams increased until 4-gram model. For a 5-gram model it increased again. Froom the experiment carried, the 4-gram model predicts better than any othet n-gram model for the give data. Also when the size of data is reduced the preplexity is very less compared when using more data. This is not true in reality. A good language model should predict unseen data as well and smoothing techniques are used in such cases.

## Reporting for Part Bonus 

### Examples to Run code:
python gendata.py -S 1000 -E 1500 -T 300 -N 5 -P brown-rga.txt output

python train.py -N 5 train_output.csv picklefile

python test.py -N 5 test_output.csv picklefile


| Arguments                        | Accuracy              | Perplexity              |
|----------------------------------|-----------------------|-------------------------|
| -S 1000 -E 1500 -T 300 -N 2 -P   | 0.3010226127034423    | 7.873685001999292       |
| -S 1000 -E 1500 -T 300 -N 3 -P   | 0.2921489332031795    | 7.254899061234176       |
| -S 1000 -E 1500 -T 300 -N 4 -P   | 0.2865604287124524    | 7.000037347462059       |
| -S 1000 -E 1500 -T 300 -N 5 -P   | 0.2965174129353234    | 6.787188260310515       |
| -E 2000 -T 300 -N 2 -P           | 0.28608657883306793   | 6.975442317541038       |
| -E 2000 -T 300 -N 3 -P           | 0.3093707965924376    | 6.518799070883535       |
| -E 2000 -T 300 -N 4 -P           | 0.3136860264519839    | 6.190062985593935       |
| -E 2000 -T 300 -N 5 -P           | 0.31011826544021026   | 6.100597163573069       |


When POS tags are used instead of the words, the preplexity is very less due to the very fact that there are very less number of POS tags and the trainging performed of the data is enough for guessing the next POS tag in a given sentence. But in case of using words, as labels its very difficult as it involves a lot of tarining on large amount of data. Also the accuracy here is more compared when using words.
