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

#Random Mutation Function
def babyS(S):
    alphabet = "abcdefghijklmnopqrstuvwxyz. "

    L = []
    for i in range(len(S)):
        L.append(S[i])
        
    random_position_in_L = random.randint(0, len(L) - 1)
    L[random_position_in_L] = random.choice(alphabet)

    S_dash = ""
    for i in range(len(L)):
        S_dash += L[i]
        
    return S_dash

S = genRandText()
current_score = score(S)
score_list = [current_score]
print("Initial string:  ", S)
n = int(input("Number of iterations you would like to try: "))
total_iterations = 0

#Mutation Loop Function
for i in range(0, n):
    S_dash = babyS(S)
    new_score = score(S_dash)

    if current_score == 62:
            print("Success, you have found it! Using", total_iterations, "iterations.")
            break
    
    elif new_score > current_score:
        S = S_dash
        current_score = new_score
        total_iterations += 1

    else:
        total_iterations += 1

    score_list.append(current_score)

#Output Messages
print("Final score:     ", current_score)
print("Final string:    ", S)

#Output Graphs
plt.plot(score_list)
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Evolution of Score")
plt.show()
