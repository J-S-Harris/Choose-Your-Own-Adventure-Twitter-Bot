# BUGS SO FAR INCLUDE:
    # if a player has made multiple tweets between checks, it can cause DB inaccuracies
    # tweets sometimes fail due to being identical to previous tweets

import configfile
import storytext
import tweepy
import time
import sqlite3
mainDB=sqlite3.connect('game_database.db')
cursor=mainDB.cursor()

my_bearer_token = configfile.my_bearer_token
consumer_key=configfile.API_key
consumer_secret=configfile.API_secret_key
access_token=configfile.accesstoken
access_token_secret=configfile.accesstokensecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

name = ''
body = ''
timestamp = ''
location = ''
new_location = ''
new_user_found = 0

#app-specific variables:
possible_actions = ['new-game','go-left','go-right','forwards','backwards','investigate']
contextual_actions = []
victory_tweet = 'placeholder victory text'


def new_game(user): # starts new game for new user, or resets current progress for current user.
    print('new game')
    # set location and progress variables to 0?
    # Respond with standard opening tweet
    # set 'forwards' to be only contextual action


def prev_in():
    global location
    if location == 1:
        cursor.execute("update users set \"previously-in-1\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 2:
        cursor.execute("update users set \"previously-in-2\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 3:
        cursor.execute("update users set \"previously-in-3\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 4:
        cursor.execute("update users set \"previously-in-4\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 5:
        cursor.execute("update users set \"previously-in-5\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 6:
        cursor.execute("update users set \"previously-in-6\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 7:
        cursor.execute("update users set \"previously-in-7\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 8:
        cursor.execute("update users set \"previously-in-8\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 9:
        cursor.execute("update users set \"previously-in-9\"='1' where name=?;", (name,))
        mainDB.commit()
    elif location == 10:
        cursor.execute("update users set \"previously-in-10\"='1' where name=?;", (name,))
        mainDB.commit()

def add_user(name): # if a new user is found, add them to the database with 0 progress
        cursor.execute("""
            select name from users where name=? limit 1
            """, (name,))
        mainDB.commit()
        x = cursor.fetchall()
        if len(x) > 0:
            pass
        else: # This is run if user is a new user:

            # Send welcome tweet:
            global tweet_id
            welcome_tweet = '@'+name,'placeholder welcome tweet'+timestamp
            api.update_status(status=welcome_tweet, in_reply_to_status_id=tweet_id)
            global new_user_found
            new_user_found = 1

            # Wait briefly then send tweet setting the scene:
            time.sleep(5)
            # send tweet: they are entering location 1 for 1st time
            # are database changes needed?
            
            # put name in db:
            cursor.execute("""
                insert into users (name) values (?);
                """, (name,))
            mainDB.commit()

            # set progress and location variables to 0:
            cursor.execute("update users set location='1' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-1'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-2'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-3'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-4'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-5'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-6'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-7'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-8'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-9'='0' where name=?;", (name,))
            mainDB.commit()
            cursor.execute("update users set 'previously-in-10'='0' where name=?;", (name,))
            mainDB.commit()
            print('New player found + committed?')





def take_action(action):
    global name
    global location
    global new_location
    global timestamp
    global tweet_id
    cursor.execute("select location from users where name=?", (name,))
    mainDB.commit()
    location = cursor.fetchall()[0][0]
    
    if action.lower() == 'go-left': # Condense this easily into one function that just checks what the instruction is

        cursor.execute("select \"left-destination\" from locations where id=?", (location,))
        mainDB.commit()
        new_location = cursor.fetchall()[0][0]
        if int(new_location) >0:
            print('old/new locations:',location,new_location)
            cursor.execute("update users set location=? where name=?;", (new_location, name))
            mainDB.commit()
            message = 'test @'+name+' [first text?] [main text] [options] ('+timestamp+')'
            if 'CYO' not in name:
                api.update_status(status = message, in_reply_to_status_id=tweet_id)
            prev_in() # sets current location's 'previously-in' var to 1
        else:
            print('invalid action for current location given')
            #tweet player to suggest they try a diff instruction

    elif action.lower() == 'go-right':

        cursor.execute("select \"right-destination\" from locations where id=?", (location,))
        mainDB.commit()
        new_location = cursor.fetchall()[0][0]
        if int(new_location)>0:
            print('old/new locations:',location,new_location)
            cursor.execute("update users set location=? where name=?;", (new_location, name))
            mainDB.commit()
            message = 'test @'+name+' [first text?] [main text] [options] ('+timestamp+')'
            if 'CYO' not in name:
                api.update_status(status = message, in_reply_to_status_id=tweet_id)
            prev_in() # sets current location's 'previously-in' var to 1
        else:
            print('invalid action for current location given')
            #tweet player to suggest they try a diff instruction
        
    elif action.lower() == 'forwards':

        cursor.execute("select \"forward-destination\" from locations where id=?", (location,))
        mainDB.commit()
        new_location = cursor.fetchall()[0][0]
        if int(new_location) >0:
            print('old/new locations:',location,new_location)
            cursor.execute("update users set location=? where name=?;", (new_location, name))
            mainDB.commit()
            message = 'test @'+name+' [first text?] [main text] [options] ('+timestamp+')'
            if 'CYO' not in name:
                api.update_status(status = message, in_reply_to_status_id=tweet_id)
            prev_in() # sets current location's 'previously-in' var to 1
        else:
            print('invalid action for current location given')
            #tweet player to suggest they try a diff instruction
            

        # put info re: tweet responded to into database
        # b) compose a tweet using new_location's text from DB:
            # if first time there, add 'first time' from text text for that room [from storytext.py]
            # either way, add 'room description' text to tweet [from storytext.py]
            # add sentence outlining options 
        # reply to tweet with composed response
        
        
    elif action.lower() == 'backwards':
        
        cursor.execute("select \"backwards-destination\" from locations where id=?", (location,))
        mainDB.commit()
        new_location = cursor.fetchall()[0][0]
        if int(new_location) >0:
            print('old/new locations:',location,new_location)
            cursor.execute("update users set location=? where name=?;", (new_location, name))
            mainDB.commit()
            message = 'test @'+name+' [first text?] [main text] [options] ('+timestamp+')'
            if 'CYO' not in name:
                api.update_status(status = message, in_reply_to_status_id=tweet_id)
            prev_in() # sets current location's 'previously-in' var to 1
        else:
            print('invalid action for current location given')
            #tweet player to suggest they try a diff instruction
        
    elif action.lower() == 'investigate':
        pass

        # Requires a modified version of other destination script (i.e above ^)
        # must:
            # a) set invest. var to 1
            # b) if location == 7: keyfoundvar = 1
            # c) must fire off a tweet saying what was found.
                # AND ALSO for room 7 if keyfound var is 0: include what was found.
                # AND ALSO for room 10, if keyfound var == 1, 'win' tweet must be sent out.
                    # [Move player to room 11, so cannot go elsewhere without starting new game?]
            # no location change needed
        
            

def main():
    global name
    global body
    global timestamp
    global tweet_id
    global new_user_found
    
    new_user_found = 0
    all_ats = api.mentions_timeline()
    for i in all_ats: # Looking at all received tweets, check: ....
        
        # ...if tweet NOT IN tweets
        
        name = [i][0]['user']['screen_name']
        body = [i][0]['text']
        timestamp = [i][0]['created_at']
        tweet_id = [i][0]['id_str']
        
        
        cursor.execute("select id from 'Previous_tweets' where user=? and body=? and time=? limit 1", (name,body,timestamp)) # reduced to 1 line; broken now?
        mainDB.commit()
        name_presence = cursor.fetchall()
        

        # A) Are they already playing the game?
        add_user(name) # Run this whether new or not; existing users are ignored

        # B) ...put the new tweet into the DB:
        if len(name_presence) == 0: # New tweet found! So....
            cursor.execute("insert into 'Previous_tweets' (user,body,time) values (?,?,?)", (name,body,timestamp)) # ... put into DB
            mainDB.commit()
            print('added tweet?\n')
            # send tweet introducing scenario
    
            # C) Check tweet for keywords; take first one and action it
            
            for ii in body.split():
                global possible_actions
                if ii.lower() in possible_actions:
                    print('permissible action found!')
                    take_action(ii) # is this running multiple times per tweet?




if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)

    
