processes = 3
resources = 4

max_resources = [3,1,1,2]
print(f"\n Available Recources: {max_resources}")
currently_allocated = [[1,2,2,1],[1,0,3,3],[1,2,1,0]]
print(f"\n Current allocation: {currently_allocated}")
max_need = [[3,3,2,2],[1,2,3,4],[1,3,5,0]]
print(f"\n Maximum Resources: {max_need}\n")
need = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(processes):
        for j in range(resources):
            need[i][j] = max_need[i][j] - currently_allocated[i][j]

print(f"\n need: {need}\n")
# Safety Algorithm
print("Safety Algorithm:\n")
count = 0
sequence = []
while count < processes:
    for i in range(processes):
        if i not in sequence:
            if need[i] <= max_resources:
                max_resources = [max_resources[j] + currently_allocated[i][j] for j in range(resources)]
                sequence.append(i)
                count += 1
    if count == 0:
        print("Deadlock detected")
        break
    
if len(sequence) > 0:
    print("The safe sequence is\n", sequence, "\n")

# Request Algorithm
print("Request Algorithm:\n")
allocated = [0,0,0,0]
available = [max_resources[i] - allocated[i] for i in range(resources)]
print(f"total available resources : {available}\n")

running = [True] * processes
count = processes
while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} is executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("the processes are in an unsafe state.")
            break

        print(f"the process is in a safe state.\navailable resources : {available}\n")

