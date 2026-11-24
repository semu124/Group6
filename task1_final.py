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

range_scores = max(score_list) - min(score_list)

# Text Output
print("Monkey scores: ", score_list)
print("BEST monkey score: ", max(score_list))
print("WORST monkey score: ", min(score_list))
print("Mean monkey score: ", sum(score_list) / len(score_list))

# Graphical Output
# scatter
plt.scatter(range(1, len(score_list) + 1), score_list)
plt.xlabel("Iteration")
plt.ylabel("Monkey Score")
plt.title("Distribution of Monkey Scores")
plt.show()

# Histogram
plt.hist(score_list, bins = range(range_scores + 1), edgecolor = "black")
plt.title("Distribution of Monkey scores")
plt.xlabel("Monkey scores")
plt.ylabel("Frequency")
plt.show()
