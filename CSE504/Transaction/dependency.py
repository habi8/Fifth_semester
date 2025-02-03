transactions=[]

with open('transaction.txt') as f:
    transactions = [line.rstrip() for line in f]

#print(transactions)
num=int(transactions[0])
#print(num)
transactions.pop(0)
separated_transactions = [item.split(",") for item in transactions]
print(separated_transactions)
rows, cols = (num, num)
# arr = [[0]*cols]*rows
arr= [[0]*cols for _ in range(rows)]

print(arr[0][1])
print(arr)
# for row in separated_transactions:
#     for i in range(len(row)):
#         if row[i][0]=='C':
#             row[i]=None

max_len = max(len(t) for t in separated_transactions)
# Column-wise traversal
for i in range(1,max_len):
    for j in range(len(separated_transactions)):
        if separated_transactions[j][i][0] == 'R' or separated_transactions[j][i][0] == 'W':
            for it in range(i+1,max_len): 
                for k in range(len(separated_transactions)):
                    if j != k :
                        if separated_transactions[k][it][0] == 'W' and separated_transactions[k][it][2] == separated_transactions[j][i][2]:
                            arr[j][k] = 1
                        elif separated_transactions[k][it][0] == 'R' and  separated_transactions[j][i][0] != 'R' and separated_transactions[k][it][2] == separated_transactions[j][i][2]:
                            arr[j][k] = 1
print(arr)

def has_cycle(graph):
    def dfs(node, visiting, visited):
        if visiting[node]:
            return True
        if visited[node]:
            return False

        visiting[node] = True
        for neighbor, has_edge in enumerate(graph[node]):
            if has_edge and dfs(neighbor, visiting, visited):
                return True

        visiting[node] = False
        visited[node] = True
        return False

    num_nodes = len(graph)
    visiting = [False] * num_nodes
    visited = [False] * num_nodes

    for node in range(num_nodes):
        if not visited[node] and dfs(node, visiting, visited):
            return True

    return

print(has_cycle(arr))

# for row in separated_transactions:
#     for i in range(len(row)):
#         if row[i][0]=='R':
#             for otherrows in separated_transactions:
#                 for i+1 in otherrows:
#                     if otherrows[i+1][0]=='W':
#                         if otherrows[i+1][2]==row[i][2]:
#                             arr[i][i+1]=1

