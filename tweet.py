"""Assignment 1.
   Pragith Chenthuran
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '

def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).
    
    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False
    """
    
    return len(text) >= 1 and len(text) <= MAX_TWEET_LENGTH
    
def compare_tweet_lengths(tweet_1: str, tweet_2: str) -> int:
    """Return 1 if the tweet_1 is longer than tweet_2, -1 if
    the tweet_2 is longer than tweet_1, or 0 if the tweet_1
    and tweet_2 have the same length.

    Pre-Conditions:
    -tweet_1 and tweet_2 are valid tweets
    
    >>> compare_tweet_lengths('Hello Twitter!', 'Hi Twitter!')
    1
    >>> compare_tweet_lengths('Hello Twitter!', 'Hi, Hello and Welcome to Twitter!')
    -1
    >>> compare_tweet_lengths('Welcome Friends', 'Welcome Friends')
    0
    """
    num_return = 0
    if len(tweet_1) > len(tweet_2):
        num_return = 1
    elif len(tweet_1) < len(tweet_2):
        num_return = -1
    elif len(tweet_1) == len(tweet_2):
        num_return = 0

    return num_return

def add_hashtag(tweet: str, tweet_word: str) -> str:
    """Returns the potential-tweet which is the tweet
    with a SPACE, HASHTAGE_SYMBOL and tweet_word appeded
    to it, if the potential-tweet is a valid tweet, else
    returns tweet if potential-tweet is not valid.

    Pre-Condition:
    - tweet and tweet_word are valid
    
    >>> add_hashtag('I like','cscA08')
    'I like #cscA08'
    >> add_hashtag('01'*25,'binary')
    '01010101010101010101010101010101010101010101010101'
    """
    
    p_tweet = tweet + SPACE + HASHTAG_SYMBOL + tweet_word
    if is_valid_tweet(p_tweet) is True:
        return p_tweet
    else:
        return tweet
    
    
def helper_hash_mention(tweet: str, tweet_word: str, type_symbol: str) -> bool:
    """Return True if the full tweet_word is in tweet followed by the stated
    type_symbol, either HASHTAG_SYMBOL or MENTION_SYMBOL. Used as a helper
    function for both contains_hashtag() and is_mentioned().

    Pre-Conditions:
    - tweet and tweet_word are valid
    - type_symbol is either HASTAG_SYMBOL or MENTION_SYMBOL
       
    >>> helper_hash_mention('I love the iPhone @apple', 'apple', MENTION_SYMBOL)
    True
    >>> helper_hash_mention ('The Raptors WON! ', 'Raptors', HASHTAG_SYMBOL)
    False
    """
    
    clean_tweet = clean(tweet) + SPACE
    tweet_word = (SPACE + type_symbol + tweet_word +SPACE)
    if type_symbol == HASHTAG_SYMBOL and tweet_word in clean_tweet:
        return True
    elif type_symbol == MENTION_SYMBOL and tweet_word in clean_tweet:
        return True
    else:
        return False

def contains_hashtag(tweet: str, tweet_word: str) -> bool:
    """Return True if and only if the tweet contains a 
    hashtag made up of the hash symbol and the tweet_word.

    Pre-Conditions:
    - tweet and tweet_word are valid
    
    >>> contains_hashtag('I like #cscA08','cscA08')
    True
    >>> contains_hastag('I like #mata31','mata')
    False
    """
    
    return helper_hash_mention(tweet, tweet_word, HASHTAG_SYMBOL)

def is_mentioned(tweet: str, tweet_word: str) -> bool:
    """Return True if and only if the tweet contains a 
    hashtag made up of the hash symbol and the tweet_word.

    Pre-Conditions:
    - tweet and tweet_word are valid
    
    >>> is_mentioned('The winners are the @raptors','raptors')
    True
    >>> is_mentioned('The winners are the #raptors','raptors')
    False
    
    """
    
    return helper_hash_mention(tweet, tweet_word, MENTION_SYMBOL)

def add_mention_exclusive(tweet: str, word: str) -> str:
    """Returns the tweet with a mention of the word by appending a space
    mention symbol, and the word to the end of the tweet if the tweet
    does not already contain the mention.

    Pre-Condition:
    - tweet and tweet_word are valid
    
    >>> add_mention_exclusive ('I love the new iPhone', 'apple')
    'I love the new iPhone'
    >>> add_mention_exclusive ('The best raptors year', 'raptors')
    'The best raptors year @raptors'  
    """

    cl_tweet = SPACE + clean(tweet)
    cl_word = SPACE + word
    n_word = MENTION_SYMBOL + word
    n_tweet = tweet + SPACE + n_word
    if cl_word in cl_tweet and is_valid_tweet(n_tweet) and n_word not in tweet:
        return n_tweet
    else:
        return tweet

def num_tweets_required(tweet: str) -> int:
    """Returns the number of tweets required to post the requested tweet
    if the character count excedes the MAX_TWEET_LENGTH.

    >>> num_tweets_required('The @raptors won the finals!')
    1
    >>> num_tweets_required('11'*30)
    2
    """
    
    tweets_req = math.ceil((len(tweet))/MAX_TWEET_LENGTH)
    return tweets_req


def get_nth_tweet(tweet: str, n: int) -> str:
    """Returns the nth valid tweet-sequence in the sequence if all of
    the tweets in the sequence tweet would be of length MAX_TWEET_LENGTH.

    Pre-Conditions:
    -Valid nth tweet exists in message
    -n is greater than 0

    >>> get_nth_tweet('ab'*26, 2)
    'ab'
    >>> get_nth_tweet('2345'*26, 3)
    '2345'
    """
    
    tweet_length = len(tweet)
    seq_length = (n-1)*MAX_TWEET_LENGTH
    full_length = seq_length + MAX_TWEET_LENGTH
    if full_length < tweet_length:
        return tweet[seq_length:full_length]
    else:
        return tweet[seq_length:tweet_length]

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
