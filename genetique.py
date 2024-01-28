import random

#algorithme to look for solution of an equation called probleme


def probleme(x,y,z):
    return 6*x**3+9*y**2+20*z #lets search using the geetic algorithme for a solution to the current equation equal 0
def fitness(x,y,z) :
    ans =probleme(x,y,z)
    return 1-abs(ans)
#generate some solutions 

solutions_array=[]

for s in range(1000) :
    solutions_array.append((random.uniform(0,10000)
                            ,random.uniform(0,10000)
                            ,random.uniform(0,10000)))
    
#lunching the genetique algorithme
for i in range(10000):
    solution_based_1=[]
    for s in solutions_array :
        solution_based_1.append((fitness(s[0],s[1],s[2]),s))
    solution_based_1.sort(reverse=True)

    if solution_based_1[0][0]>0.9999 and fitness(*s) <=1  :
        print(f"generation {i} has the best solution set to : \n {solution_based_1[0]}") 
        break
        
    genetique_filtring=solution_based_1[:100]
    solution_optimal=[]
    for s in genetique_filtring :
        solution_optimal.append(s[1][0])
        solution_optimal.append(s[1][1])
        solution_optimal.append(s[1][2])
    newGen=[]
    for _ in range(1000):
        e1 = random.choice(solution_optimal) *random.uniform(0.99,1.01)
        e2 = random.choice(solution_optimal) *random.uniform(0.99,1.01)
        e3 = random.choice(solution_optimal) *random.uniform(0.99,1.01)
        newGen.append((e1,e2,e3))
    solutions_array=newGen
        
    

