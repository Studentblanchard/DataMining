Sentiment Miner
======

## Description

A python project that classifies text and parts of speech.

## Setup

This program requires the NLTK package to be installed. Follow the instructions for your machine from the following [link](http://www.nltk.org/install.html).

NLTK is distributed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0)

Python 2.7.10 was used for development. To check your python version run the following.

```
$ python --version
```
You will also need the following NLTK models.
 * averaged_perceptron_tagger
 * punkt
 * tagsets

To install these packages start up your python interpreter and run

```python
>>> import nltk
>>> nltk.download()
```
This will open the downloader utility which you can then use to install the listed models.

## Usage

#### tag.py
This is used to generate the trained data. In particular it will generate `pos_pos.txt` and `neg_pos.txt`. This data is later used by the miner to find our interesting patterns.

To run the tagger...
```
$ python tag.py
```

#### mine.py
This is used to generate the trained data. In particular it will generate `positive_POS_dict.json` and `negative_POS_dict_pos.json`. This data is later used by the classifier to classify test data.

To run the miner...
```
$ python mine.py
```

#### classify.py
This is used to test the training data. In particular it will run the classifier on `Test/positivetestdata/` and `Test/negativetestdata/`. The results are published in `testResults.txt`.

To run the classifier...
```
$ python classify.py
```

#### interactive.py
An interactive classifier. It will publish the results to `testResults.txt`.

To run the interactive classifier...
```
$ python interactive.py
Enter a file name or a directory > Test/negativetestdata/
...
```

## Datasource

All of the testing and training data used was from the [Stanford link](http://ai.stanford.edu/~amaas/data/sentiment/
).

It has been extracted and placed in accessible locations for our program.



## Contact
* Authors: Trevor Blanchard, Brett Small, Samuel Peers, Stefan Harris
* e-mail: umblanc3@myumanitoba.ca, umsmallb@myumanitoba.ca, peerss@myumanitoba.ca, stefanjharris@gmail.com
