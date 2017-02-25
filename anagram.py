# https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/
def anagram_detector(input):
    compared_words = input.split(" ? ")
    scrambled_words = []
    for s in compared_words:
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace("'", "")
        s = "".join(sorted(s))
        scrambled_words.append(s)
    
    if scrambled_words[0] == scrambled_words[1]:
        print(compared_words[0] + " is an anagram of " + compared_words[1])
    else:
        print(compared_words[0] + " is NOT an anagram of " + compared_words[1])
        
anagram_detector("Clint Eastwood ? Old West Action")
anagram_detector("wisdom ? mid sow")
anagram_detector("Seth Rogan ? Gathers No")
anagram_detector("Reddit ? Eat Dirt")
anagram_detector("Schoolmaster ? The classroom")
anagram_detector("Astronomers ? Moon starer")
anagram_detector("Vacation Times ? I'm Not as Active")
anagram_detector("Dormitory ? Dirty Rooms")