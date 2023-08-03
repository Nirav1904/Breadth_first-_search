print("Name : Nirav Parmar\nEnrolment No : 20C22027")
graph1={
        "A":["B","C","E"],
        "B":["A","D","E"],
        "C":["A","F","G"],
        "D":["B"],
        "E":["A","B","D"],
        "F":["C"],
        "G":[]
        }
graph2 = {
  "A" : ["D","C"],
  "B" : ["B", "E"],
  "C" : ["F"],
  "D" : ["E"],
  "E" : ["F"],
  "F" : []
}
def bfs(graph,initial):
    visited=[]
    queue=[initial]

    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours=graph[node]

        for neightbour in neighbours:
            queue.append(neightbour)
    return visited

print("BFS PATH OF GRAPH 1 IS :",bfs(graph1,"A"))
print("BFS PATH OF GRAPH 2 IS :",bfs(graph2,"A"))