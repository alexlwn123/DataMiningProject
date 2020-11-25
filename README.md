# Comp 5130: Implementation of Rule-Based Classification Algorithm

## Robby March, Alex Lewin
## Table of Contents

* [**Backround**](#Backround)
  * [**Problem Introduction**](#Intro)
  * [**Dataset**](#Dataset)
* [**Experiment**](#Experiment)
  * [**Results**](#Results)
* [**Requirements**](#Requirements)
* [**Install**](#Install)
* [**Run Project**](#Run-Project)
  * [**Run Classifier**](#Run-Classifier)
  * [**Run Doctests**](#Run-Doctests)

## <a name="Backround"></a>**Backround**

We were tasked to implement a Rule-Based Classifier.

### <a name="Intro"></a>**Problem Introduction**
### <a name="Dataset"></a>**Dataset**


We want to identify communities of highly connected authors and also predict if an author is within one of these communities. 
### <a name="Dataset"></a>**Problem Introduction**


Our dataset has 5,242 nodes and 28,980 edges, and this dataset describes a collaboration network. In the dataset, a node/vertex represents an author and an edge represents a coauthorship between two authors. 


## <a name="Experiment"></a>**Experiment Description**

To predict whether a specific author exists within the inner-circle of authors, we implemented  rule based classifier that predicts membership based on the number of 1st degree neighbors that a node posesses.   

<img src="plot.png" width=200>

To test this, we implemented a union-find algorithm to determine the actual membership of a specific author. 

## <a name="Results"></a>**Results**
### Classification Results
We used F1 scores to determine the optimal bound for the rule.
| Distance | Micro-F1 (Inside) | Micro-F1 (Outside) | Macro-F1  |
| -------- | ----------------- | ------------------ | --------- |
| 3        | 0.861             | 0.459              | 0.660     |
| 5        | 0.919             | 0.575              | 0.747     |
| 7        | 0.936             | 0.590              | 0.763     |
| 9        | 0.960             | 0.611              | 0.785     |
| 11       | 0.979             | 0.623              | 0.801     |
| 13       | 0.992             | 0.627              | **0.809** |
A distance of 13 results in the best Macro-F1 score.

### Efficiency Test

Small Dataset Neighbor Analysis:   
`15 nanosec`

Runtime is incredibly fast for calculating neighbors using a dataset of this size.
## <a name="Requirements"></a>**Requirements**
Below are the requiremnts to run the test locally.

* **Python 3** [Download](https://www.python.org/downloads/)   
* **Git** [Download](https://git-scm.com/downloads)

## <a name="Install"></a>Install

In the terminal, enter the following commands:

```bash
# Clone the project repository.
git clone https://github.com/alexlwn123/DataMiningProject
# Move to the project directory.
cd DataMiningProject
# Activate the Virtual Environment.
./Scripts/activate
# Install requirements
pip install -r requirements.txt 
```
## <a name="Run-Project" ></a>Run Project  

To run our project code, you can either run an interactive CLI or a set of pre-written tests via doctest.

### <a name="Run-Classifier"></a>Run Classifier

```bash
# Run project.
python src/classifier.py
```

### <a name="Run-Doctests"></a>Run Doctests


```bash
# Run doctests.
python -m doctest -v src/classifier.py
```