import followers_getter
import tweetsDates_getter
import activityStats_getter

if __name__ == '__main__':
    var = True
    print('##### Twitter Campaign Optimizer #####')
    while var:
        print("\nWhat do you want to do ?")
        choice = int(input("1 - Get All the Followers of a User.\n2 - Get All the Dates of the Tweets from a List of Followers.\n3 - Have Activity Statistics.\n4 - Quit Program.\nChoice : ")) #menu  creation
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            choice = int(input("1 - Get All the Followers of a User.\n2 - Get All the Dates of the Tweets from a List of Followers.\n3 - Have Activity Statistics.\n4 - Quit Program.\nChoice : "))
        if choice == 1:
            print("\n1 - Get All the Followers of a User.")
            followers_getter.main() #crete excel file with the followers of a Twitter account
            print("The List of Followers is available in \"/assests\".")
        elif choice == 2:
            print("\n2 - Get All the Dates of the Tweets from a List of Followers.")
            tweetsDates_getter.main() # create an excel file with the creation dates of all tweets made by a follower list
            print("The Dates of Collected Twetts is available in \"/assests\".")
        elif choice == 3:
            print("\n3 - Have Activity Statistics.")
            activityStats_getter.main() #display the temporal distribution of the tweets
        else:
            var = False #allows to quit the program