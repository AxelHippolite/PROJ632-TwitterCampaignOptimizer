import tweepy
import pandas as pd
import numpy as np
import time
import os

def getFollowers(client, account_username, account_id):
    """
    input: API Objects, str
    output: list
    returns all the followers of a twitter account and save them into an excel file
    """
    total_follower, followers_list = [], []
    for page in tweepy.Paginator(client.get_users_followers, account_id, max_results=1000):
        followers_list.extend(page)
    for i in range(len(followers_list)):
        if len(followers_list[i]) > 3:
            for j in range(len(followers_list[i])):
                user_id, user_username = followers_list[i][j].id, followers_list[i][j].username
                total_follower.append([user_id, "@"+user_username])
    df = pd.DataFrame(np.asarray(total_follower))
    os.mkdir('assets/'+ account_username)
    df.to_excel('assets/'+ account_username +'/followers.xlsx')
    return total_follower
        
def getAccountID(api):
    """
    input: API Object
    output: str
    returns the account username et the account id
    """
    account_username = input("Account @ : ")
    account_id = api.get_user(screen_name=account_username)
    return account_username, account_id.id_str

def initialize():
    """
    input: None
    output: API Objects
    connects to the Twitter api and allows its use
    """
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHXbYwEAAAAA4QPzse4AZT2JgBeJhHFX6FZ1Hq4%3Dt8cD1K7iM8gwL2hORXMM7dIU58jPJgPmGHK9gZOqghr4tyPbWL" #"AAAAAAAAAAAAAAAAAAAAADxtYwEAAAAARJhAUfR%2FMUiFlDGJbtgr3gzfWic%3DxlzKtK2Nud9kxWGd6XWh2xd4PCc18YnPGCIrFaQnaZebA58xSN"
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
    account_username, account_id = getAccountID(api)
    print("Account : @" + account_username + " ID : " + account_id)
    followers = getFollowers(client, account_username, account_id)
    print("Total Followers :", len(followers))
