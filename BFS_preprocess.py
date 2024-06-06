# import
import pandas as pd

# edges (consecutive services) for BFS
df = pd.read_csv("BFS_input_data.csv") 
from_scat = list(df["from_scat"])
to_scats = list(df["to_scat"])
tuples = len(from_scat)

# no. of graphs to input (1, in our case)
print("1")
print()

## input: 
# no. of edges in graph
# plus
# no. of service pairs to find the shortest path between

# read the above inputs
print(str(tuples) + " " + str(1)) 
for i in range(0, tuples):
    print(from_scat[i] + " " + to_scats[i]) 

# service-pair (A - B) to mine shortest path (input to BFS)
print("wash_&_iron" + " " + "refrigerator_repair_services")
