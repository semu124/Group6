import random 
import matplotlib.pyplot as plt
import numpy as np

# Random String Function
def genRandText():
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
    S = ""
    
    for i in range(62):
        S += random.choice(alphabet)
    
    return S

S = genRandText
T = "he who seeks rest finds boredom. he who seeks work finds rest."

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
    L[random_position_in_L] = random.choice([c for c in alphabet if c != L[random_position_in_L]])  ### coursework said to 'another character' so i thought i do this.

    S_dash = ""
    for i in range(len(L)):
        S_dash += L[i]
        
    return S_dash

# Loop Function
def S_loop():
    S = genRandText()
    current_score = score(S)
    total_iterations = 0

    while S != T and total_iterations < n:  ### for iteration
        S_dash = babyS(S)
        new_score = score(S_dash)
        total_iterations += 1

        if new_score > current_score:
            S = S_dash
            current_score = new_score

    return total_iterations, S == T

number_of_runs = int(input("How many runs:  "))
n = int(input("How many iterations per one run: "))  ### so we can choose the number of iteration ourselves
iteration_list = []
for i in range(number_of_runs):
    iteration_list.append(S_loop())
    
successful_runs = 0  ### to see how many of them reached the target
iteration_list = []
for i in range(number_of_runs):
    iterations, success = S_loop()
    if success:
        successful_runs += 1
        iteration_list.append(iterations)
    

mean_iterations = sum(iteration_list) / len(iteration_list)
data = np.array(iteration_list)
std_iterations = data.std(ddof=1)
x = np.linspace(data.min() - std_iterations, data.max() + std_iterations, 500)
pdf = np.exp(-0.5 * ((x - mean_iterations) / std_iterations) ** 2) / (std_iterations * np.sqrt(2 * np.pi))

# Output Messages
print("Fewest iterations needed was", min(iteration_list))
print("Most iterations needed was", max(iteration_list))
print("Mean number of iterations needed was", mean_iterations)
print("Succeful runs:", successful_runs) ###
# Output Graphs
plt.scatter(range(1, len(iteration_list) + 1), iteration_list)
plt.axhline(y = mean_iterations, color = "black", linestyle = "--", label = f"Mean, {mean_iterations:.0f}")
plt.xlabel("Run number")
plt.ylabel("Iterations needed")
plt.title("Number of iterations needed for each run")
plt.legend()
plt.show()

plt.hist(data, bins = 20, density = True, edgecolor = "black", label = "Observed")
plt.plot(x, pdf, linewidth=2, label=f"Normal, (μ={mean_iterations:.0f}, σ={std_iterations:.0f})")
plt.axvline(x = mean_iterations, color = "black", linestyle = "--", label = f"Mean, {mean_iterations:.0f}")
plt.xlabel("Iterations needed")
plt.ylabel("Density")
plt.title(f"Distribution of iterations needed ({number_of_runs} runs)")
plt.legend()
plt.show()