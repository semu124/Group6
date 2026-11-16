import random 
import matplotlib.pyplot as plt


# Random String Function
def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
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
    
    score_list.append(score(S))
    
    if score(S) == 62:
        
        print("Success!")
        
        break
    


# Text Output
print("Monkey scores: ", score_list) # Possibly avoid this as it is too much on massive numbers like n = 1000000
print("BEST monkey score: ", max(score_list))
print("WORST monkey score: ", min(score_list))
print("Mean monkey score: ", sum(score_list) / len(score_list))

# Graphical Output
# scatter
plt.scatter(range(1, len(score_list) + 1), score_list,  edgecolour ="black", alpha=0.6)
plt.xlabel("Iteration")
plt.ylabel("Monkey Score")
plt.title("Distribution of Monkey Scores")
plt.show()
# Histogram
plt.hist(score_list, bins=range(63), edgecolor="black", alpha=0.6)
plt.title("Distribution of Monkey scores")
plt.xlabel("Monkey scores")
plt.ylabel("Frequency")
plt.show()

