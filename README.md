# nltk-corpora-addition
Addition of ~5,000 TV and Movie Scripts to the NLTK Corpora.

# Inspiration
If you look at the [nltk corpora](https://www.nltk.org/_modules/nltk/corpus.html), you can see it has thousands of books and dictionaries but not much in terms of contemporary work. This program scrapes ~5,000 shows TV scripts so that they can be put in the nltk corpora. 

# Dependencies 
Run in command line
1. `pip install beautifulsoup4`
2. `pip install os`
3. `pip install requests`
4. `pip install urllib3`

# How to run the program 
1. clone the repository 
2. create a corpora library in the folder of the scraper 
3. run `python3 main.py` in the command line 
** Note that given the thousands of web requests that this scraper takes approximately 40 hours to scrape all of this information. Consequently, if you are cut for time I would recommend running this on multiple VM's as a batch job rather than your local. 
