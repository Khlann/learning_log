List = [[1,2],[2,4],[1,3]]

List.sort(key=lambda x: x[1])

removed, prev_end = 0, List[0][1]

for i in range(1, len(List)):
    if prev_end > List[i][0]: 
        removed += 1 
    else: 
        prev_end = List[i][1]

print(removed)