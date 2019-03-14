
68.18# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: YOUR NAME HERE

## Additional instructions

Document here additional command-line instructions or other details you
want us to know about running your code.

## Reporting for Part 4

### Examples to Run code:
python gendata.py -S 1000 -E 1500 -T 300 -N 2 -P brown-rga.txt output

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

## Reporting for Part Bonus 

### Examples to Run code:
python gendata.py -S 1000 -E 1200 -T 120 brown-rga.txt output -N 5

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
