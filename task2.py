# Now we pick 1 random position out of 62 and change it to another letter in the alphabet. 
# We then score the new string and compare it to the previous score. If the new score is higher, 
# we keep the new string. If not, we revert back to the previous string. We repeat this process for a 
# number of iterations specified by the user.

def babyS(S):
    """
    Creates a clone of S with x = 1 at a randomly position in S changed to a random character from the alphabet
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz. " # the alphabet to choose from

    # Create a list L from the string S so that we can easily modify a character in S by changing the corresponding element in L
    L = [] # creat a list L to hold the characters of S
    for i in range(len(S)): # this breaks S into a list L,
        L.append(S[i]) # this adds each letter of S to L
        
    # We now pick a random pisition in list L and change it to a random letter from alphabet
    random_position_in_L = random.randint(0, len(L) - 1) # picks random position 0 - 62 in L
    L[random_position_in_L] = random.choice(alphabet) # the random position in L is converted to a letter

    # rebuild the new string S_dash from the list L   
    S_dash = "" 
    for i in range(len(L)):# this is a loop that goes through each charachter in list L 
                           # and adds it to the a new string S_dash.
        S_dash += L[i] # this line adds the character at the chosen position in L
                       # to S_dash hence it becomes a copy of S with one letter chaneged
        
    return S_dash
