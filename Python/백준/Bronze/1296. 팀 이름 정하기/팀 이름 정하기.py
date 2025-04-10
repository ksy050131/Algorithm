def winnerTeam(L, O, V, E):
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

def countName(target, nameY, teamName):
    targetcnt = nameY.count(target) + teamName.count(target)
    return targetcnt

nameY = input()
testcase = int(input())
result = {}

for i in range(testcase):
    teamName = input()
    
    L = countName('L', nameY, teamName)
    O = countName('O', nameY, teamName)
    V = countName('V', nameY, teamName)
    E = countName('E', nameY, teamName)
    
    result[teamName] = winnerTeam(L, O, V, E)
    
result = {k : v for k, v in sorted(result.items())}
# print(result)
maxTeam = max(result, key=result.get)
maxValue = result[maxTeam]
print(f"{maxTeam}")