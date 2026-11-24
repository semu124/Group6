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

            if current_score == 62:
                success_counts += 1
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

## part 3, randomly selecting incorrect positions only 
runs_p3 = int(input("Number of runs for part 3: "))
iteration = (int(input("Number of iteration for part 3: ")))
for run in range(runs_p3):
    S = genRandText()
    current_score = score(S)
    task3_score = []
    
    
    for i in range(iteration):
        incorrect_position =[i for i in range(len(S)) if S[i] != T[i]]
        if not incorrect_position:
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
        task3_score.append(current_score)    
        if current_score == len(S):
            break  

# graphs, to show the progress across iteration
plt.scatter(range(1, len(task3_score) + 1), task3_score, label='task 3', alpha=0.7)
plt.title("Monkey scores against Iteration")
plt.xlabel("Iteration")
plt.ylabel("Monkey scores")
plt.legend()
plt.show()  
