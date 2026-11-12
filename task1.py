import random 
import matplotlib.pyplot as plt


# Random String Function
def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz, "
    S = ""
    
    for i in range(62):
        S += random.choice(alphabet)
    
    return S


# String Scoring Function
def score(S):
    
    T = "he who seeks rest finds boredom. he who seeks work finds rest."
    assert len(S) == len(T)

    score = 0
    
    for i in range(len(S)):
        
        if S[i] == T[i]:
            score += 1
    
    return score

S = genRandText()

# Scoring Loop
score_list = []
n = int(input("Number of iterations: "))

for i in range(0, n):

    S = genRandText()
    
    if score(S) == 62:
        
        print("Success!")
        
        break
    
    score_list.append(score(S))


# Text Output
print("Monkey scores: ", score_list)
print("BEST monkey score: ", max(score_list))
print("WORST monkey score: ", min(score_list))
print("Mean monkey score: ", sum(score_list) / len(score_list))

# Graphical Output
plt.scatter(range(1, n+1), score_list)
plt.xlabel("Iteration")
plt.ylabel("Monkey Score")
plt.title("Distribution of Monkey Scores")
plt.show()

