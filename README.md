# Vaccine sentiment in England
This repository contains code &amp; data for the paper "Keep calm and carry on vaccinating: Is ‘anti-vaccination’ sentiment contributing to declining vaccine coverage in England ?"

## Install
```
conda env create -f environment.yml
```

Followed by 

```
conda activate vaccine-sentiment-england
```

## Download raw tweets from Tweet IDs
Generate a set of Twitter API keys and download the tweets using the following command:
```
python download_tweets.py -i ./data/raw_data.csv -o ./data/tweets.jsonl --consumerkey XXX --consumersecret XXX --accesstoken XXX  --accesssecret XXX
```
This will download all vaccine related tweets which have been determined to be from England (using the [geocode-local](https://github.com/mar-muel/local-geocode) repository) between July 2017 and October 2019 (n=187183).

## Generate figure
The figure can be generated using the command
```
python generate_figure.py
```
The data will be read from a binary file (pickle file) which contains the preprocessed sentiment trend and activity data.

## Vaccine sentiment model
The model which was used to predict the sentiment can be found [here](https://crowdbreaks-public.s3.eu-central-1.amazonaws.com/models/fasttext_v1.ftz).
For more information about how this model was generated (including the used training data), please refer to the paper

```
Müller, Martin M., and Marcel Salathé. 
Crowdbreaks: Tracking Health Trends Using Public Social Media Data and Crowdsourcing.
Frontiers in public health 7 (2019).
```
The corresponding data/code can be found [here](https://github.com/salathegroup/crowdbreaks-paper).


## Questions
If you have further questions, please write to martin.muller@epfl.ch (or info@crowdbreaks.org)
