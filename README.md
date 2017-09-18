# Dota scraping project
Proof-of-concept spiders for scraping Dota-related data

## About Dota
Dota is a popular MOBA (Multiplayer Online Battle Arena) video game with the highest prize pool in E-sports (last Valve organized event, the International 7 had a prize pool of over $24M).

## Contents of this project
Currently the project features two simple spiders that showcase scraping identical data from two different sources: dotabuff.com and opendota.com.

## Before running the spiders
Before we can start scraping the data, the user needs to install the necessary packages. This can be done with:
```
pip install -r requirements.txt
```

## Running the spiders
To run a specific spider, the user needs to run:
```
scrapy crawl <SPIDER_NAME>
```
from the command line.
