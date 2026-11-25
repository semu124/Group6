import random 
import matplotlib.pyplot as plt
import numpy as np

### Task 1

# Random String Function
def genRandText():
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
    S = ""

    for i in range(62):
        S += random.choice(alphabet)
    
    return S

S = genRandText
T = "he who seeks rest finds boredom. he who seeks work finds rest."
alphabet = "abcdefghijklmnopqrstuvwxyz. "

# String Scoring Function
def score(S):
    assert len(S) == len(T)
    score = 0

    for i in range(len(S)):
        if S[i] == T[i]:
            score += 1

    return score

# Scoring Loop
score_list = []
n = int(input("\033[1mNumber of iterations wanted for Task 1: \033[0m"))

for i in range(0, n):
    S = genRandText()
    score_list.append(score(S))
    
    if score(S) == 62:
        print("Success!")
        break

range_scores = max(score_list) - min(score_list)

# Text Output
print("Best monkey score:   ", max(score_list))
print("Worst monkey score:  ", min(score_list))
print("Mean monkey score:   ", sum(score_list) / len(score_list))

## Graphical Output
# Histogram
plt.hist(score_list, bins = range(range_scores + 1), edgecolor = "black")
plt.title("Distribution of Monkey scores")
plt.xlabel("Monkey scores")
plt.ylabel("Frequency")
plt.show()



### Task 2

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

number_of_runs = int(input("\033[1mNumber of runs wanted for Task 2: \033[0m"))
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
print("Fewest iterations needed was", min(stats_iteration_list))
print("Most iterations needed was", max(stats_iteration_list))
print("Mean number of iterations needed was", mean_iterations)
print("The omitted values were:", omitted_iterations_under_20000)
print("The number of runs over the iteration limit (20,000) was", runs_over_20000)

# Output Graphs
# Adjusted Scatter Graph
plt.scatter(range(1, len(stats_iteration_list) + 1), stats_iteration_list)
plt.axhline(y = stats_mean, color = "black", linestyle = "--", label = f"Mean, {stats_mean:.0f}")
plt.xlabel("Run number")
plt.ylabel("Iterations needed")
plt.title(f"Number of iterations needed for each run ({len(stats_iteration_list)} runs)")
plt.legend()
plt.show()

# Adjusted Histogram
plt.hist(stats_data, bins = 40, density = True, edgecolor = "black", label = "Observed")
plt.axvline(x = stats_mean, color = "black", linestyle = "--", label = f"Mean, {stats_mean:.0f}")
plt.xlabel("Iterations needed")
plt.ylabel("Density")
plt.title(f"Distribution of non-anomolous iterations needed ({len(stats_iteration_list)} runs)")
plt.legend()
plt.show()




### Task 3

#   3a: Changing Mutation Rates

def offspringS(S, x):
    
    assert 1 <= x <= len(S), "Mutation rate cannot be outside [1, 62]"
    
    L = list(S) 
    random_positions_in_L = random.sample(range(len(L)), x)  # Selects x random positions from L without repeatition.
    
    for i in random_positions_in_L:
        L[i] = random.choice(alphabet)

    S_dash = "" 
    for i in range(len(L)):
                           
        S_dash += L[i] 
                        
    return S_dash

print("\033[1mWe will be testing mutation rates: 1, 3, 6, 12, 24\033[0m")
runs = int(input("\033[1mNumber of runs wanted for Task 3a: \033[0m"))
n = int(input("\033[1mMaximum number of iterations allowed for Task 3a: \033[0m"))
mutation_rate = [1, 3, 6, 12, 24]
results = {}
success_counts = {}
successful_iterations = {}

for x in mutation_rate:
    results[x] = []
    success_counts[x] = 0
    successful_iterations[x] = []
    for run in range(runs):
        S = genRandText()
        current_score = score(S)

        score_list = [current_score]
        for i in range(0, n):
    
            S_dash = offspringS(S, x) 
            new_score = score(S_dash)
    
            if new_score > current_score:
                S = S_dash
                current_score = new_score
        
            score_list.append(current_score)

            if current_score == 62:
                success_counts[x] += 1
                successful_iterations[x].append(i + 1)
                break
        while len(score_list) < n + 1:
                score_list.append(current_score)
        results[x].append(score_list)    


for x in mutation_rate:
    run_scores = np.array(results[x])
    avarage_score = np.mean(run_scores, axis=0)
    standard_deviation = np.std(run_scores, axis=0)
    plt.plot(
        range(n + 1),
        avarage_score,
        label=f"mutation rate = {x}"
    )
    success_rate = (success_counts[x] / runs) * 100

    print("\033[1mMutation rate: \033[0m", x)
    print("Success rate:    ", success_rate, "%")
    print("Average score:   ", avarage_score[-1])

    if successful_iterations[x]:
        mean_iterations = np.mean(successful_iterations[x])
        print("Mean iteration needed for success:", mean_iterations)
    else:
        print("There were no successful runs")    

plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Evolution of Score")
plt.legend()
plt.grid()
plt.show()



#   3b: Shorter Target String

def short_genRandText():
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
    A = ""
    
    for i in range(28):
        A += random.choice(alphabet)
    
    return A

A = short_genRandText
B = "methinks it is like a weasel"

def short_score(A):
    T = "methinks it is like a weasel"
    assert len(A) == len(B)
    short_score = 0
    
    for i in range(len(A)):
        if A[i] == B[i]:
            short_score += 1
    
    return short_score

def babyA(A):
    alphabet = "abcdefghijklmnopqrstuvwxyz. "

    C = []
    for i in range(len(A)):
        C.append(A[i])
        
    random_position_in_C = random.randint(0, len(C) - 1)
    C[random_position_in_C] = random.choice(alphabet)

    A_dash = ""
    for i in range(len(C)):
        A_dash += C[i]
        
    return A_dash

def A_loop():
    A = short_genRandText()
    short_current_score = short_score(A)
    short_total_iterations = 0

    while A != B :
        A_dash = babyA(A)
        short_new_score = short_score(A_dash)
        short_total_iterations += 1

        if short_new_score > short_current_score:
            A = A_dash
            short_current_score = short_new_score

    return short_total_iterations

number_of_runs_each = int(input("\033[1mNumber of runs wanted for Task 3b: \033[0m"))
iteration_list = []
short_iteration_list = []

for i in range(number_of_runs_each):
    iteration_list.append(S_loop())

for i in range(number_of_runs_each):
    short_iteration_list.append(A_loop())

short_mean_iterations = sum(short_iteration_list) / len(short_iteration_list)
short_data = np.array(short_iteration_list)
short_std_iterations = short_data.std(ddof = 1)
short_x = np.linspace(data.min() - short_std_iterations, short_data.max() + short_std_iterations, 500)
short_pdf = np.exp(-0.5 * ((x - short_mean_iterations) / short_std_iterations) ** 2) / (short_std_iterations * np.sqrt(2 * np.pi))

stats_iteration_list = []
short_stats_list = []

for i in range(0, number_of_runs_each):
    if iteration_list[i] < mean_iterations - 3 * std_iterations:
        continue
    elif iteration_list[i] > mean_iterations + 3 * std_iterations:
        continue
    else:
        stats_iteration_list.append(iteration_list[i])

for i in range(0, number_of_runs_each):
    if short_iteration_list[i] < short_mean_iterations - 3 * short_std_iterations:
        continue
    elif short_iteration_list[i] > short_mean_iterations + 3 * short_std_iterations:
        continue
    else:
        short_stats_list.append(short_iteration_list[i])

short_stats_mean = sum(short_stats_list) / len(short_stats_list)
short_stats_data = np.array(short_stats_list)
short_stats_std = short_stats_data.std(ddof = 1)

histogram_titles = ["Longer Text", "Shorter Text"]
histogram_data = [stats_mean, short_stats_mean]

print("The following results are presented as longer text, shorter text:")
print("Fewest iterations needed each text was", min(stats_iteration_list), "&", min(short_stats_list))
print("Most iterations needed for the longer text was", max(stats_iteration_list), "&", max(short_stats_list))
print("Mean number of iterations needed for the longer text was", stats_mean, "&", short_stats_mean)

plt.bar(histogram_titles, histogram_data)
plt.title("Mean iterations needed to reach target text")
plt.xlabel("Target Text")
plt.ylabel("Mean Iterations Needed")
plt.show()





runs_p3 = int(input("\033[1mNumber of runs wanted for Task 3c: \033[0m"))
iteration = (int(input("\033[1mMaximum number of iterations allowed for Task 3c: \033[0m")))
iteration_per_run = []
for run in range(runs_p3):
    S = genRandText()
    current_score = score(S)
    iterations_taken = 0
    success = False
    for i in range(iteration):
        incorrect_position =[i for i in range(len(S)) if S[i] != T[i]]
        if not incorrect_position:
          success = True
          break
       
        position = random.choice(incorrect_position)
     
        new_character = random.choice(alphabet)
        S_prime = list(S)
        S_prime[position] = new_character
        S_prime = "".join(S_prime)
        new_score = score(S_prime)

        if new_score > current_score:
            S = S_prime
            current_score = new_score
        iterations_taken = i + 1 
        if current_score == len(S):
            success = True
            break 
    if success:
        iteration_per_run.append(iterations_taken)
    else:
        iteration_per_run.append(None)        

# graphs, to show the progress across iteration
mutated_mean = sum(iteration_per_run) / len(iteration_per_run)
mutated_data = np.array(iteration_per_run)
mutated_std = mutated_data.std(ddof = 1)

print("Fewest iterations needed was", min(iteration_per_run))
print("Most iterations needed was", max(iteration_per_run))
print("Mean number of iterations needed was", mutated_mean)

plt.scatter(range(1, len(iteration_per_run) + 1), iteration_per_run)
plt.axhline(y = mutated_mean, color = "black", linestyle = "--", label = f"Mean, {mutated_mean:.0f}")
plt.xlabel("Run number")
plt.ylabel("Iterations needed")
plt.title(f"Number of iterations needed for each run ({len(iteration_per_run)} runs)")
plt.legend()
plt.show()

plt.hist(mutated_data, bins = 40, density = True, edgecolor = "black", label = "Observed")
plt.axvline(x = mutated_mean, color = "black", linestyle = "--", label = f"Mean, {mutated_mean:.0f}")
plt.xlabel("Iterations needed")
plt.ylabel("Density")
plt.title(f"Distribution of iterations needed ({len(iteration_per_run)} runs)")
plt.legend()
plt.show()
