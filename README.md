# Multitask Models for Supervised Protests Detection in Texts Replication Archive

Benjamin J. Radford  
Paper available at [arXiv:2005.02954](https://arxiv.org/abs/2005.02954)

<hr>

## Required files

1. Download the file `wiki.en.bin` from [https://www.kaggle.com/azunre/fasttext-wikienbin](https://www.kaggle.com/azunre/fasttext-wikienbin) and place it in the root directory.
2. Populate the directory `task3public9may/` with the following competition files:
    + china_test.data
    + dev.txt
    + task3_test.data
    + train.txt
3. Populate the directory `solutions/` with the following competition files:
    + task1_dev.data
    + task1_dev.solution
    + task1_test.data
    + task1_train.data
    + task1_train.solution
    + task2_dev.data
    + task2_dev.solution
    + task2_test.data
    + task2_train.data
    + task2_train.solution
4. Populate the directory `data/Document/` with the following competition files:
    + dev_filled.json
    + test_china_filled.json
    + test_filled.json
    + train_filled.json
5. Populate the directory `data/Sentence/` with the following competition files:
    + dev_filled.json
    + test_china_filled.json
    + test_filled.json
    + train_filled.json
    
I will provide the necessary data for academic researchers interested in replicating this project on a case-by-case basis. To make a request, please contact me at benjamin.radford (at) uncc.edu.

## Setup

Create a new [Anaconda environment](https://www.anaconda.com/products/individual) by running the following command:

```
conda env create -f environment.yml
```
