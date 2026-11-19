# 
import random
import matplotlib.pyplot as plt
import numpy as np
T = "he who seeks rest finds boredom. he who seeks work finds rest."
characters = "abcdefghijklmnopqrstuvwxyz ."
## task 1
def genRandText():
    s = ""   # empty string to store characters
    for i in range(62):
       s += random.choice(characters) 
    return s

# for string scoring
def score(s):
    assert len(s) == len(T)

    score = 0

    for i in range(len(s)):
        if s[i] == T[i]:
            score += 1
    return score

task1_score = []
n = int(input("Number of iterations: "))

for i in range(n):
    s = genRandText()

    task1_score.append(score(s))
    if score(s) == 62:
        print("correct!")
        break

## Task 2. choose one incorrect position and change the letter
S = genRandText()
current_score = score(S)
task2_score = []
for i in range(n):
    
    S_list = list(S)
    position = random.randrange(len(S))
    new_character = random.choice(characters)

    S_list[position] = new_character
    S_prime = "".join(S_list)
    offspring_score = score(S_prime)

    if offspring_score > current_score:
        S = S_prime 
        current_score = offspring_score
    task2_score.append(current_score)
    if current_score == 62:
        print("correct!")
    else:
        print("Iteration limit reached")        
print(S) # see the 62 characters at the end of iteration.

# Task 3: memory based mutation
# this allows for a random letter in an incorrect postion to be stored and not be targeted on the next trials
S = genRandText()
current_score = score(s)
task3_score = []
tried_characters = [[] for i in range(len(S))]
for i in range(n):
     incorrect_position =[i for i in range(len(S)) if S[i] != T[i]]
     if not incorrect_position:
          break
     position = random.choice(incorrect_position)
     non_tried_character = [ 
          c for c in characters if c!= S[position] and c not in tried_characters[position]
     ]
     new_character = random.choice(non_tried_character)
     tried_characters[position].append(new_character)

     S_prime = list(S)
     S_prime[position] = new_character
     S_prime = "".join(S_prime)
     new_score = score(S_prime)

     if new_score > current_score:
          S = S_prime
          current_score = new_score
     task3_score.append(current_score)    
     if current_score == len(s):
          break     
     

# results for task 1
print("Monkey scores:", task1_score)
print("Best monkey score:", max(task1_score))
print("Worrst monkey score:", min(task1_score))
print("Mean monkey score:", sum(task1_score) / len(task1_score))
print("standard deviation:", np.std(task1_score))

# graphs, to show the progress across iteration
plt.scatter(range(1, len(task1_score) + 1), task1_score, label='task 1', alpha=0.7)
plt.scatter(range(1, len(task2_score) + 1), task2_score, label='task 2', alpha=0.7)
plt.scatter(range(1, len(task3_score) + 1), task3_score, label='task 3', alpha=0.7)
plt.title("Monkey scores against Iteration")
plt.xlabel("Iteration")
plt.ylabel("Monkey scores")
plt.legend()
plt.show()

# task 3 should have the best outcome because it chooses from less options as incorrect character is stored and ignored for the next try.
# for a smaller iteration the outcome becomes more random. 