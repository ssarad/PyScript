# importing the module 
# -*- coding: utf-8 -*-
import tweepy 

# personal details 


consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

def tweet(status):
	if len(status) > 280:
		print("Count limit exceeded! Try again")
	else:
		api.update_status(status) 
		print("Success! Your tweet %s was sent!") % (status)

def reply_tweet():
	tweetid = int(input("Enter tweet id: "))
	print(' ')
	status = raw_input("Enter tweet less than 280 char: ")
	print(' ')
	if len(status) > 280:
    		exit()
	elif len(status) < 280:
		try:
	    		api.update_status(status, in_reply_to_status_id = tweetid ,auto_populate_reply_metadata=True)
	    		twp = api.get_status(tweetid,tweet_mode = 'extended')
	    		name = twp.user.screen_name
	    		tweet = twp.full_text
	    		print('\nSuccess! Your reply was sent to %s , this was the tweet:\n\n %s') %(name,tweet)
		except:
	    		print('Failed!')
def reply_with_media():
	tweetid = int(input("Enter tweet id: "))
	print(" ")
	try:	
		link_to_file = raw_input("\nEnter location of file with filename: ")
		caption = raw_input("\nEnter caption: ")
		api.update_with_media(link_to_file,caption,in_reply_to_status_id = tweetid,auto_populate_reply_metadata=True)
		twp = api.get_status(tweetid,tweet_mode = 'extended')
	    	#name = twp.user.screen_name
	    	#tweet = twp.full_text
		print('\nSuccess! Your reply was sent to %s , this was the tweet:\n\n %s') %(twp.user.screen_name,twp.full_text)
	except:
		print('Failed!')

def tweet_with_media():
	link_to_file = raw_input("\nEnter location of file with filename: ")
	caption = raw_input("\nEnter caption: ")
	try:
		api.update_with_media(link_to_file,caption)
	except:
		print("Broken! Code 0x7512AE")

def quote_retweet():
	link = raw_input("\nEnter link of the status to quote-retweet: ")
	comment = raw_input("\nEnter your comment: ")
	tweet(comment+" "+link,api)	

def printMenu():
	print("\n\n")
	print("---------------------------------------------------------")
	print("|    	~~~~~Tweet from your terminal~~~~~   		|")
	print("|							|")
	print("|	1) Tweet a status.				|")
	print("|	2) Reply to a status.				|")
	print("|	3) Tweet with an image.				|")
	print("|	4) Reply to a tweet with media.			|")
	print("|	5) Quote retweet.				|")
	print("|	6) Quit.					|")
	print("---------------------------------------------------------")
	print("\n\n")

def start():
	while(True):
		try:
			choice = int(input("Enter the number corresponding to the menu: "))
			while(choice < 1 or choice > 6):
				print("\nInvalid input. Try again!\n")
				printMenu()
				choice = int(input("Enter the number corresponding to the menu: "))
			break;
		except:
			print("Only numbers! Try again.")
	return choice;

def main():
	while(True):
		printMenu()
		choice = start()
		if(choice == 1):
			status = raw_input("Enter your status: ")
			tweet(status)
		elif(choice == 2):
			reply_tweet()
		elif(choice == 3):
			tweet_with_media()
		elif(choice == 4):
			reply_with_media()
		elif(choice ==5):
			quote_retweet()
		elif(choice == 6):
			print("Goodbye!")
			exit()
		anotherC = raw_input("\nWould you like to do another task? Enter Y for yes, N for No.")[0]
		while(not(anotherC == 'Y' or anotherC == 'y' or anotherC == 'N' or anotherC == 'n')):
			print("\nInvalid input! Try again\n")
			anotherC = raw_input("Would you like to do another task? Enter Y for yes, N for No.")
		if(anotherC == 'n' or anotherC == 'N'):
				exit()


main()

		


