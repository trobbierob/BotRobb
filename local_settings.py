'''
Local Settings for a BotRobb account. #fill in the name of the account you're tweeting from here.
'''

from onepiece import *

#configuration
MY_CONSUMER_KEY = consumer_key
MY_CONSUMER_SECRET = consumer_secret
MY_ACCESS_TOKEN_KEY = access_token_key
MY_ACCESS_TOKEN_SECRET = access_token_secret

SOURCE_ACCOUNTS = ["SwiftOnSecurity", "KidFury", "captainsafia", "ashleymanta", "Raquel_Savage"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "BotRobb" #The name of the account you're tweeting to.
