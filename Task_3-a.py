import random   
import matplotlib.pyplot as plt

def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
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


def babyS(S):
    
    assert 1 <= x <= len(S), "Mutation rate cannot be outside [1, 62]"
    
    alphabet = "abcdefghijklmnopqrstuvwxyz. " 
    L = list(S) 
    random_positions_in_L = random.sample(range(len(L)), x)  # Selects x random positions from L without repeatition.
    
    for i in random_positions_in_L:
        L[i] = random.choice(alphabet)

    S_dash = "" 
    for i in range(len(L)):
                           
        S_dash += L[i] 
                        
    return S_dash


S = genRandText()
current_score = score(S)
score_list = [current_score]
n = int(input("Maximum number of iterations for target attempt: "))
x = int(input("Mutation rate (1-62): "))

for i in range(0, n):
    
    S_dash = babyS(S) 
    new_score = score(S_dash)
    
    if new_score > current_score:
        S = S_dash
        current_score = new_score
        
    score_list.append(current_score)

    if current_score == 62:

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


# After trialling different mutation rates x, we have seen that x = 1 is the most effective.
# Our graphical output shows that higher mutation rates create an increased rate of progress in the earlier iterations.
# However, with these higher rates, the progress plateaus as the score increases.
# This is because a higher mutation rate increases the chance of altering an already correct character.
# Essentially, our function has a limit point where the mutation rate is too high to allow for further progress.
