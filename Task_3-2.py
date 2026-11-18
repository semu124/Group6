import random   
import matplotlib.pyplot as plt

def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz "  # Removed full stop from alphabet as new T does not include any 
    S = ""
    
    for i in range(28):                       # Reduced length of S to 28 as new T is only 28 characters long
        S += random.choice(alphabet)
    
    return S


def score(S):
    
    T = "methinks it is like a weasel"        # Changed T to Dawkins' original target string
    assert len(S) == len(T)

    score = 0
    
    for i in range(len(S)):
        
        if S[i] == T[i]:
            score += 1
    
    return score


def babyS(S):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz "  # As above
    L = list(S) 
    random_position_in_L = random.randint(0, len(L) - 1) 
    L[random_position_in_L] = random.choice(alphabet)
  
    S_dash = "" 
    for i in range(len(L)):
                           
        S_dash += L[i] 
                        
    return S_dash


S = genRandText()
current_score = score(S)
score_list = [current_score]
n = int(input("Number of iterations for Target attempt: "))


for i in range(0, n):
    
    S_dash = babyS(S) 
    new_score = score(S_dash)
    
    if new_score > current_score:
        S = S_dash
        current_score = new_score
        
    score_list.append(current_score)

    if current_score == 28:

        print("Success, the target string has been found!")
   
        break

print("Initial string: ", genRandText())
print("Initial string score: ", score(genRandText()))
print("Final string: ", S) 
print("Final string score: ", current_score) 
print("Number of attempts: ", len(score_list))

plt.plot(score_list)
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Evolution of Score")
plt.show()



# As expected, after numerous trials, the number of iterations to achieve the target string is significantly lower.
# This is because the target string is shorter, and the number of unique characters is lower.
# Therefore the probability of randomly generating a matching character is higher, and the number of iterations required to achieve the target string is lower.
