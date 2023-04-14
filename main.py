meme_dict = {
            "CRINGE": "Something very strange or embarrassing",
            "LOL": "A common response to something funny",
            }
            
            

word = input("Type a word you don't understand (use all capital letters!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
