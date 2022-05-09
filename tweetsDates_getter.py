import tweepy
import pandas as pd
import numpy as np
import time

def getDates(api, client, users, path):
    """
    input: API Objects, str
    output: list
    returns all the creation dates of all tweets of a list of users and save them into an excel file
    """
    all_tweets = []
    count = 0
    for ids in users:
        tweets = []
        print('- User No.', count)
        try:
            tweets = [[tweet.id, str(api.get_status(tweet.id).created_at)] for tweet in tweepy.Paginator(client.get_users_tweets, str(ids), max_results=100).flatten()]
        except tweepy.errors.TooManyRequests as e:
            time.sleep(60)
        for tweet in tweets:
            all_tweets.append(tweet)
        count += 1
    df = pd.DataFrame(np.asarray(all_tweets))
    df.to_excel(path[0]+'/'+path[1]+'/all_tweets.xlsx')
    return all_tweets

def getFollowersCSV(path):
    """
    input: str
    output: list
    returns the ids of all the followers of the file passed in argument
    """
    df = pd.read_excel(path)
    data = pd.DataFrame(df, columns=[0]).values.tolist()
    return [ids[0] for ids in data]

def initialize():
    """
    input: None
    output: API Objects
    connects to the Twitter api and allows its use
    """
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHXbYwEAAAAA4QPzse4AZT2JgBeJhHFX6FZ1Hq4%3Dt8cD1K7iM8gwL2hORXMM7dIU58jPJgPmGHK9gZOqghr4tyPbWL"
    auth = auth = tweepy.OAuth2BearerHandler(bearer_token)
    api = tweepy.API(auth) #v1
    client = tweepy.Client(bearer_token) #v2
    return api, client

def main():
    """
    input: None
    output: None
    main function allowing to save all followers of a twitter account in an excel file
    """
    api, client = initialize()
    path = input("Enter the Path to your Followers List : ")
    followers = getFollowersCSV(path)
    print("Total Followers :", len(followers))
    all_tweetID = getDates(api, client, followers, path.split('/'))
    print("Collected Tweets :", len(all_tweetID))