processes = 3
resources = 4
max_resources = [int(i) for i in input("maximum resources : ").split()]

print("\n allocated resources for each process:")
currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

print("\n maximum resources for each process:")
max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]
print(max_need)
need = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(processes):
        for j in range(resources):
            need[i][j] = max_need[i][j] - currently_allocated[i][j]

print(f"\n need: {need}\n")
# Safety Algorithm
print("Safety Algorithm\n")
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
print("Request Algorithm\n")
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

