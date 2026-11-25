import random 
import matplotlib.pyplot as plt
import numpy as np

T = "he who seeks rest finds boredom. he who seeks work finds rest."
alphabet = "abcdefghijklmnopqrstuvwxyz. "
# Random String Function
def genRandText():
    S = ""
    for i in range(len(T)):
        S += random.choice(alphabet)
    
    return S

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
n = int(input("Number of iterations for task 1: "))

for i in range(0, n):
    S = genRandText()
    score_list.append(score(S))
    
    if score(S) == len(T):
        print("Success!")
        break

range_scores = max(score_list) - min(score_list)

#stat for task 1
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

 
## task 2

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

number_of_runs = int(input("How many runs for task 2:  "))
iteration_list = []

for i in range(number_of_runs):
    iteration_list.append(S_loop())

runs_over_20000 = 0

for i in range(0, number_of_runs):
    if iteration_list[i] < 20000:
        continue
    else:
        runs_over_20000 += 1


# stat for task 2
mean_iterations = sum(iteration_list) / len(iteration_list)
data = np.array(iteration_list)
std_iterations = data.std(ddof = 1)
x = np.linspace(data.min() - std_iterations, data.max() + std_iterations, 500)
pdf = np.exp(-0.5 * ((x - mean_iterations) / std_iterations) ** 2) / (std_iterations * np.sqrt(2 * np.pi))

stats_iteration_list = []
omitted_iterations = []

for i in range(0, number_of_runs):
    if iteration_list[i] < mean_iterations - 3 * std_iterations:
        omitted_iterations.append(iteration_list[i])
    elif iteration_list[i] > mean_iterations + 3 * std_iterations:
        omitted_iterations.append(iteration_list[i])
    else:
        stats_iteration_list.append(iteration_list[i])

stats_mean = sum(stats_iteration_list) / len(stats_iteration_list)
stats_data = np.array(stats_iteration_list)
stats_std = stats_data.std(ddof = 1)
stats_x = np.linspace(stats_data.min() - stats_std, stats_data.max() + stats_std, 500)
stats_pdf = np.exp(-0.5 * ((stats_x - stats_mean) / stats_std) ** 2) / (stats_std * np.sqrt(2 * np.pi))
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
plt.plot(stats_x, stats_pdf, linewidth=2, label=f"Normal, (μ={stats_mean:.0f}, σ={stats_std:.0f})")
plt.axvline(x = stats_mean, color = "black", linestyle = "--", label = f"Mean, {stats_mean:.0f}")
plt.xlabel("Iterations needed")
plt.ylabel("Density")
plt.title(f"Distribution of non-anomolous iterations needed ({len(stats_iteration_list)} runs)")
plt.legend()
plt.show()

## task 3
## part 1, having differnt mutation rate
def babyS(S, x):
    
    assert 1 <= x <= len(S), "Mutation rate cannot be outside [1, 62]"
    
    L = list(S) 
    random_positions_in_L = random.sample(range(len(L)), x)  # Selects x random positions from L without repeatition.
    
    for i in random_positions_in_L:
        L[i] = random.choice(alphabet)

    S_dash = "" 
    for i in range(len(L)):
                           
        S_dash += L[i] 
                        
    return S_dash


runs = int(input("Number of runs for task 3, part 1: "))
n = int(input("Maximum number of iterations for for task 3, part 1: "))
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
    
            S_dash = babyS(S, x) 
            new_score = score(S_dash)
    
            if new_score > current_score:
                S = S_dash
                current_score = new_score
        
            score_list.append(current_score)

            if current_score == len(T):
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

    print("mutation rate:", x)
    print("success rate:", success_rate, "%")
    print("Average score:", avarage_score[-1])
    print("standard deviation:", standard_deviation[-1])

    if successful_iterations[x]:
        mean_iterations = np.mean(successful_iterations[x])
        print("Mean iteration to success:", mean_iterations)
    else:
        print("no successful runs")    

plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Evolution of Score")
plt.legend()
plt.grid()
plt.show()

## part 2, lower number of characters

T = "methinks it is like a weasel"

def babyS(S):
    
    L = list(S) 
    random_position_in_L = random.randint(0, len(L) - 1) 
    L[random_position_in_L] = random.choice(alphabet)
  
    S_dash = "" 
    for i in range(len(L)):
                           
        S_dash += L[i] 
                        
    return S_dash

initial_S = S

score_list = [current_score]
runs = int(input("Number of runs for part 2: "))
n = int(input("Number of iterations for part 2: "))
iteration_list = []
failed_runs = 0
for run in range(runs):
    S = genRandText()
    current_score = score(S)
    iterations_taken = 0
    success = False
    for i in range(0, n):
        if current_score == len(T):
            break

        S_dash = babyS(S) 
        new_score = score(S_dash)
        iterations_taken += 1

        if new_score > current_score:
            S = S_dash
            current_score = new_score 

        if current_score == len(T):
            print("success!")
            success = True
            iteration_list.append(i + 1)
            break
    if not success:
        failed_runs += 1

print("successful runs for part 2: ", len(iteration_list))
print("Failed runs: ", failed_runs)
print("Initial string: ", initial_S)
print("Final string: ", S) 
print("Final string score: ", current_score) 
print("Number of attempts: ", len(score_list) - 1)
print("Mean iterations: ", np.mean(iteration_list))

plt.scatter(range(1, len(iteration_list) + 1), iteration_list)
plt.axhline(y=np.mean(iteration_list), color="black", linestyle="--", label="mean")
plt.xlabel("runs")
plt.ylabel("iteration needed")
plt.title("Iteration needed fpr a shorter target")
plt.legend()
plt.show()
# histogram
plt.hist(iteration_list, bins=20, edgecolor="black")
plt.xlabel("iteration needed")
plt.ylabel("frequency")
plt.title("Distribution of iterations")
plt.show()

## part 3, randomly selecting incorrect positions only 
T = "he who seeks rest finds boredom. he who seeks work finds rest."
runs_p3 = int(input("Number of runs for part 3: "))
iteration = (int(input("Number of iteration for part 3: ")))
iteration_per_run = []
failed_runs = 0
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
        iterations_taken += 1
        if current_score == len(T):
            success = True
            break 

    if success:
        iteration_per_run.append(iterations_taken)
    else:
        failed_runs += 1

print("successful runs: ", len(iteration_per_run))
print("Failed runs: ", failed_runs)
# graphs, to show the progress across iteration
plt.scatter(range(1, len(iteration_per_run) + 1), iteration_per_run)
plt.axhline(y=np.mean(iteration_per_run), color="black", linestyle="--", label="Mean")
plt.title("iteration neded for part 3")
plt.xlabel("successful runs")
plt.ylabel("number of iteration")
plt.legend()
plt.show()    

# hisrogram
plt.hist(iteration_per_run, bins=20, edgecolor="black")
plt.xlabel("iterations")
plt.ylabel("Frequency")
plt.title("Distribution of iteration")
plt.show()
