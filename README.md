## A CLM Strategy for MX
**by Shithi Maitra, Jr. Data Scientist**

### Objectives of the Study
- Designing an optimal journey of a customer from one defined service another desired service
- Retaining a customer to the platform and promote X-selling
- Gaining more control over a customer's life-cycle of taking services 
- Gaining confidence that a data-backed, statistical, algorithmic approach is being followed

*<strong>Note:</strong> Some data are hidden as per privacy policy. Links inactive outside organization.*

### Proposed Methodology

<img width="460" alt="ee4" src="https://github.com/shithi30/BFS-GraphTheory_for_CLM-Cross.Up-Sales/assets/43873081/a64d435b-4db3-4698-b339-9eb21bd6e6b1">
<br><strong>Fig:</strong> Proposed process shown in flowchart<br><br>

- Preprocessing the users' data to view customers' cross-selling tendencies from one ServCat to top-03 (or top-05) ServCats: http://mb.sheba.xyz/question/16912
- Construct a bidirectional network graph as portraying the ServCats as nodes and the flexibility to move between ServCats as edges
- Define the source ServCat (A) and a destination ServCat (B) 
- Run a BFS(Breadth First Search) to find the optimal number of steps and path

<br><img width="300" alt="ee4" src="https://github.com/shithi30/BFS-GraphTheory_for_CLM-Cross.Up-Sales/assets/43873081/5ffe8b5a-9588-427a-bda8-eccd39df5b7e">
<br><strong>Fig:</strong> Preprocessing the data for the construction of a network graph<br>

<br><img width="460" alt="ee4" src="https://github.com/shithi30/BFS-GraphTheory_for_CLM-Cross.Up-Sales/assets/43873081/3c23a9c9-9a72-4ea4-8ce2-d7a40c4c3e40">
<br><strong>Fig:</strong> Preprocessing for inputting into BFS<br><br>

<img width="750" alt="ee4" src="https://github.com/shithi30/BFS-GraphTheory_for_CLM-Cross.Up-Sales/assets/43873081/4a6b21b4-7a6b-41a2-8c34-81ea75dcd563">
<br><strong>Fig:</strong> Snippet of the BFS code and generation of output<br>

### Action Points/Future Work 
- Predicting with ML which customers are likely to return: http://mb.sheba.xyz/question/16969
- Determining the service they last took and defining a high-bucket service we want to take them to 
- Making attempts of pitching them gradually along the optimized path





