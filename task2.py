
import random   
import matplotlib.pyplot as plt

def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz, "
    S = ""
    
    for i in range(62):
        S += random.choice(alphabet)
    
    return S


def score(S):
    
    T = "he who seeks rest finds boredom. he who seeks work finds rest."
    assert len(S) == len(T)

    score = 0
    
    for i in range(len(S)):
        
        if S[i] == T[i]:
            score += 1
    
    return score


# Now we pick 1 random position out of 62 and change it to another letter in the alphabet. 
# We then score the new string and compare it to the previous score. If the new score is higher, 
# we keep the new string. If not, we revert back to the previous string. We repeat this process for a 
# number of iterations specified by the user.

def babyS(S):
    """
    Creates a clone of S where a randomly selected character position in S is changed to a random character from the alphabet
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz. " # the alphabet to choose from

    # Create a list L from the string S so that we can easily modify a character in S by changing the corresponding element in L
    L = list(S) 
    # this breaks S into a list L
     
    # We now pick a random position in list L and change it to a random letter from alphabet
    random_position_in_L = random.randint(0, len(L) - 1) # picks random position 0 - 62 in L
    L[random_position_in_L] = random.choice(alphabet) # the random position in L is converted to a letter

    # rebuild the new string S_dash from the list L   
    S_dash = "" 
    for i in range(len(L)):# this is a loop that goes through each charachter in list L 
                           # and adds it to the a new string S_dash.
        S_dash += L[i] # this line adds the character at the chosen position in L
                       # to S_dash hence it becomes a copy of S with one letter chaneged
        
    return S_dash


S = genRandText() # this generates a random string S of length 62

current_score = score(S) # this gives a score for this S using the score function

score_list = [current_score] # this creates a list of the scores

n = int(input("Number of iterations for Target attempt ")) # this asks the user to input a their number of iterations


for i in range(0, n): # Now we repeat the above process n times
    
    S_dash = babyS(S) # this calls the babyS function and uses S as its list, this value is then stored as S'
    
    # Calculate score of S_dash, if better than S it replaces S by S_prime
    new_score = score(S_dash) # this scores the S' function so we can compare it to the score of S
    
    if new_score > current_score: # if new_score > current_score we use S' as the new S
        S = S_dash # if true replace S with S_dash
        current_score = new_score # update the current score if true
        
    score_list.append(current_score) # this adds the above score to the list of scores

    if current_score == 62: # this checks if the score has reached the maximun possible value

        print("Success, the target string has been found!")
   
        break # this forces it to break if the score limit is reached


print("Final string: ", S) 
print("Final score: ", current_score) 
print("Number of attempts: ", len(score_list))


plt.plot(score_list)
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Evolution of Score")
plt.show()
