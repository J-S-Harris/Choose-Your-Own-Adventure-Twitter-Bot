import configfile
import storytext
import tweepy
import time
import sqlite3
mainDB=sqlite3.connect('game_database.db')
cursor=mainDB.cursor() # mainDB is 'connect' in RPG text engine

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


#app-specific variables:
possible_actions = ['new-game','go-left','go-right','forwards','backwards','investigate']


def new_game(user): # starts new game for new user, or resets current progress for current user.
    print('new game')
    # set location and progress variables to 0

def add_user(name): # if a new user is found, add them to the database with 0 progress
        cursor.execute("""
            select name from users where name=? limit 1
            """, (name,))
        mainDB.commit()
        x = cursor.fetchall()
        if len(x) > 0:
            print(x[0][0])
        else: # This is run if user is a new user:
            
            # put name in db:
            cursor.execute("""
                insert into users (name) values (?);
                """, (name,))
            mainDB.commit()

            # set progress and location variables to 0:
            cursor.execute("""
                update users set location='0' where name=?;
                """, (name,))
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
    pass #remove this
    if action.lower() == 'go-left':
        pass
        # current_location = [DB: location var]
        # new_location = [DB: location var's go-left var]
        # compose a tweet:
            # if first time there, add 'first time' from text text for that room [from storytext.py]
            # either way, add 'room description' text to tweet [from storytext.py]
            # add sentence outlining options 
        # reply to tweet with composed response
        # modify DB accordingly: update location, set previous visit var to 1, 
        
    elif action.lower() == 'go-right':
        pass
        # see go-left
    elif action.lower() == 'forwards':
        pass
        # see go-left
    elif action.lower() == 'backwards':
        pass
        # see go-left
    elif action.lower() == 'investigate':
        pass
        # see go-left



            

def main():
    global name
    global body
    global timestamp
    all_ats = api.mentions_timeline()
    for i in all_ats: # Looking at all received tweets, check: ....

        # ...if tweet NOT IN tweets
        print('nbt', name, body, timestamp)
        name = [i][0]['user']['screen_name']
        body = [i][0]['text']
        timestamp = [i][0]['created_at']
        print('\n',name,'\n',body,'\n',timestamp)
        cursor.execute("""
        select id from 'Previous_tweets' where user=? and body=? and time=? limit 1
        """, (name,body,timestamp))
        mainDB.commit()
        name_presence = cursor.fetchall()
        print('name presence:',name_presence, len(name_presence))

        # A) ...put the new tweet into the DB:
        if len(name_presence) == 0: # New tweet found! So....
            cursor.execute("""
            insert into 'Previous_tweets' (user,body,time) values (?,?,?)""", (name,body,timestamp)) # ... put into DB
            mainDB.commit()
            print('added tweet?\n')
        
        # B) Are they already playing the game?
        add_user(name) # Run this whether new or not; existing users are ignored
    
        # C) Check tweet for keywords; take first one and action it
        for ii in body.split():
            global possible_actions
            if ii.lower() in possible_actions:
                take_action(ii)



if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)

    
