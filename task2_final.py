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
    L[random_position_in_L] = random.choice(alphabet)

    S_dash = ""
    for i in range(len(L)):
        S_dash += L[i]
        
    return S_dash

failed_runs = 0

# Loop Function
def S_loop():
    S = genRandText()
    current_score = score(S)
    total_iterations = 0

    while S != T :
        S_dash = babyS(S)
        new_score = score(S_dash)
        total_iterations += 1

        if new_score > current_score:
            S = S_dash
            current_score = new_score

    return total_iterations

number_of_runs = int(input("How many runs:  "))
iteration_list = []

for i in range(number_of_runs):
    iteration_list.append(S_loop())

runs_over_20000 = 0

for i in range(0, number_of_runs):
    if iteration_list[i] < 20000:
        continue
    else:
        runs_over_20000 += 1

mean_iterations = sum(iteration_list) / len(iteration_list)
data = np.array(iteration_list)
std_iterations = data.std(ddof = 1)
x = np.linspace(data.min() - std_iterations, data.max() + std_iterations, 500)
pdf = np.exp(-0.5 * ((x - mean_iterations) / std_iterations) ** 2) / (std_iterations * np.sqrt(2 * np.pi))

stats_iteration_list = []
omitted_iterations = []

for i in range(0, number_of_runs):
    if iteration_list[i] < mean_iterations - 3 * std_iterations:
        omitted_iterations.apped(iteration_list[i])
    elif iteration_list[i] > mean_iterations + 3 * std_iterations:
        omitted_iterations.append(iteration_list[i])
    else:
        stats_iteration_list.append(iteration_list[i])

stats_mean = sum(stats_iteration_list) / len(stats_iteration_list)
stats_data = np.array(stats_iteration_list)
stats_std = stats_data.std(ddof = 1)
iterations_included = len(stats_iteration_list)
omitted_iterations.sort()

omitted_iterations_under_20000 = []

for i in range(0, len(omitted_iterations)):
    if omitted_iterations[i] < 20000:
        omitted_iterations_under_20000.append(omitted_iterations[i])

# Output Messages
print("Fewest iterations needed was", min(stats_iteration_list),)
print("Most iterations needed was", max(stats_iteration_list))
print("Mean number of iterations needed was", mean_iterations)
print("The omitted values were:", omitted_iterations_under_20000)
print("The number of runs over the iteration limit (20,000) was", runs_over_20000)

# Output Graphs
# Adjusted Scatter
plt.scatter(range(1, len(stats_iteration_list) + 1), stats_iteration_list)
plt.axhline(y = stats_mean, color = "black", linestyle = "--", label = f"Mean, {stats_mean:.0f}")
plt.xlabel("Run number")
plt.ylabel("Iterations needed")
plt.title(f"Number of iterations needed for each run ({len(stats_iteration_list)} runs)")
plt.legend()
plt.show()

# Adjujsted Normal
plt.hist(stats_data, bins = 30, density = True, edgecolor = "black", label = "Observed")
plt.axvline(x = stats_mean, color = "black", linestyle = "--", label = f"Mean, {stats_mean:.0f}")
plt.xlabel("Iterations needed")
plt.ylabel("Density")
plt.title(f"Distribution of non-anomolous iterations needed ({len(stats_iteration_list)} runs)")
plt.legend()
plt.show()
