import random

library = ["exit","apple","pen","need","cover","book","down","up","no","inverse","intro","avatar",
          "banana","baby","balloon","ball","blank","lemon","chose","choir","clothes","chain","diamond", "die", "druid", "drive", "disk","dance", "dive","end","event","elephant","entropy","energy","fake","food","fine","find","finland","game","gain",
           "good","great","home","house","hole","in","image","illustration",
          "inverse","jealous","ending","envelope","entertainment","joy","japan","jamaica","koala","kite","kayak",
           "kenya","kind","lime","live","lame","louisiana","mont","mint","mine","mind",
          "never","new","null","nice","chain","change","omega","opened","oven","oil","over","owner","park",
           "plane","period","pencil","pie","pest","queue","quinoa",
          "query","quest","rest","range","room","rain","ruins","repeat","run","ran","ruanda","rapid",
           "sight","seat","sit","sign","signify","same","sun","sunlight","similar","school","speed","split",
           "team","toon","tomb",
          "town","toilet","table","time","twin","trust","tropical","union","unity","utopia","university",
           "unbelievable","untrusted","unchanged","vein","vague","viper","vomit","wagon","wallet","wine",
          "win","winner","wall","xylophone","xenophobia","yogurt","yummy","yes","you","young","zoom","zambia",
           "zone","xerox","xi","zillion","zapping","zenith","zero","yourself","year",]
random_starting = ["lava","non","button","close","die","try","expel"]
word_holder = random.choice(random_starting)
print(word_holder)
used_words = []

while True:
    
    #take the user's input, return the iuser input and last letter, and print the user input only
    def getUserInput(user_input= input("Enter Your Word: ").lower()):
        user_input = user_input.strip()
        #user_ending = user_input[-1]
        user_begin = user_input[0]
        return(user_input, user_begin)#, user_ending)
    user_play = getUserInput()
    print(user_play[0])
    
    #check the user's input. (1)check if the word was already used. If yes, break. (2) check if the user input
    #starts with the last letter of the pc input. If no, break. If yes, move to the following function.
    
    def checkInput(holding_word, proposed_word, first_letter):
        for word in used_words:
            if word == proposed_word:
                #proposed_word = "YOU LOSE, word already used!"
                print("Word already used!")
                holding_word = proposed_word
                last_letter = holding_word[-1]
            else:
                continue
        if first_letter != holding_word[-1]:
            proposed_word = "x"
            #print(proposed_word)
            holding_word = proposed_word
            last_letter = holding_word[-1]
        elif first_letter == holding_word[-1]:
            holding_word = proposed_word
            last_letter = holding_word[-1]
        return (holding_word, last_letter)
    given_word = checkInput(word_holder, user_play[0], user_play[1])
     #if the for loop above or if cindition above are fulfilled, break
    if given_word[0] in used_words or given_word[0] == "x":
        print("You lose!")
        break
        
    # if the user's input happened to be in the pc library, remove it.  
    for words in library:
        if words == given_word[0]:
            library.remove(words)
        else:
            continue
    #print(given_word)
    # the pc will at least the user last letter in search for words beginning with that letter in its 
    #dictionary. Once the pc finds them, it adds them to list and randomly select one of them as its play
    # if the pc doesn't find any more words, pc output = "i" and it breaks, player wins
    def getPcInput(lib,last_letter):
        found_words = []
        for word in lib:
            if word.startswith(last_letter):
                found_words.append(word)
                
        if not found_words:
            pc_word = "i"
        elif found_words:
            pc_word = random.choice(found_words)
        pc_ending = pc_word[-1]
        return (pc_word, pc_ending)
    
    pc_input = getPcInput(library, given_word[1])
    if pc_input[0] == "i":
        print("I can't find any word. You win!")
        break
    print(pc_input[0])
    
    # add player & pc words tpo used words. renew the word_holder to the latest output. remove pc word from library
    used_words.append(pc_input[0])
    used_words.append(user_play[0])
    word_holder = pc_input[0]
    library.remove(pc_input[0])