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

n = int(input("Number of iterations for Target attempt "))

for i in range(0, n):
    S_dash = babyS(S)
    
    new_score = score(S_dash)
    if new_score > current_score:
        S = S_dash
        current_score = new_score
        
    score_list.append(current_score)

    if current_score == 62:
        print("Success, you have found !")
        break

print("Final string: ", S)
