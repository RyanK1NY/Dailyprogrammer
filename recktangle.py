# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
def recktangle(word, width, height):
    word_length = len(word)
    
    rectangle = [[" "] * word_length for i in range(word_length)]
    
    for i in range(word_length):
        rectangle[0][i] = word[i] #top
        rectangle[i][0] = word[i] #left
        rectangle[word_length - 1][i] = word[(word_length - 1) - i] #bottom
        rectangle[i][word_length - 1] = word[(word_length - 1) - i] #right
        
    print("\n".join([" ".join(line) for line in rectangle]))
    
recktangle("rekt", 1 , 2)
