import random   


def genRandText():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz, "
    S = ""
    
    for i in range(62):
        S += random.choice(alphabet)
    
    return S


def score(S):
    
    T = "he who seeks rest finds boredom. he who seeks work finds rest."
    assert len(string) == len(T)

    score = 0
    
    for i in range(len(S)):
        
        if S[i] == T[i]:
            score += 1
    
    return score


S = genRandText()

print("Monkey type:")
print(S)
print("Monkey score:", score(S))
