import random
from teams import teams

def addEdge(adj , u , v):
    adj[u].append(v)
    adj[v].append(u)
    return adj

def color(graph , v):
    degrees = []
    for i in range(v):
        degrees.append((i , len(graph[i])))

    degrees.sort(key=lambda x : x[1] , reverse=True)    

    result = [-1] * v
    result[0] = 0 # assign v0 color0

    # A temporary array to store the available colors. 
    # False value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [True] * v

    for n in degrees: # color the remaining vertices
        for i in graph[n[0]]: # loop through adjacent nodes of the current vertex
            if result[i] != -1: # if the current vertex has a color
                available[result[i]] = False # make that color unavailable

        # find the first available color
        clr = 0
        while clr < v and (not available[clr]):
            clr += 1

        # assign the first available color to n
        result[n[0]] = clr

        # reset the available array for next iteration
        for i in graph[n[0]]:
            if (result[i] != -1):
                available[result[i]] = True

    groups = {}
    for u in range(32):
        # print("team", teams[u]["name"], " --->  group", result[u])
    
        if result[u] in groups:
            groups[result[u]].append((teams[u]["name"] , teams[u]["pot"]))
        else:
            groups[result[u]] = [(teams[u]["name"] , teams[u]["pot"])]    

        
    return groups

def deg(g , v):
    return len(g[v]) 


random.shuffle(teams)
g = [[] for i in range(32)]
for i in range(32):
    for j in range(i + 1 , 32):
        if teams[i]["pot"] == teams[j]["pot"] or teams[i]["country"] == teams[j]["country"]:
            addEdge(g , i , j)

groups = color(g , 32)

def display(groups):
    print()
    print("-----CHAMPOINS LEAGUE DRAW RESULTS-----")
    print()
    for key in sorted(groups.keys()):
        groups[key].sort(key = lambda x: x[1])
        print("GROUP" , chr(key + 65))
        for t in groups[key]:
            print(t[0] , t[1])

        print("############################")
display(groups)