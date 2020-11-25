# Comp 5130: Implementation of Rule-Based Classification Algorithm
## Robby March, Alex Lewin
## Table of Contents

* [**Backround**](#Backround)
  * [**Algorithm Description**](#Alg)
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

#### <a name="Alg"></a>*Algorithm Description**

#### <a name="Intro"></a>**Problem Introduction**
We want to identify communities of highly connected authors and also predict if an author is within one of these communities. Additionally, we want to be able to predict if an author is within a specified highly connected community with 3 or greater neighbors.
#### <a name="Dataset"></a>**Problem Introduction**

![Data Visualization](images/plot.pdf)
Our dataset has 5,242 nodes and 28,980 edges, and this dataset describes a collaboration network. In the dataset, a node/vertex represents an author and an edge represents a coauthorship between two authors. 

## <a name="Experiment"></a>**Experiment**
## <a name="Results"></a>**Results**
| Distance | Micro-F1 (Inside) | Micro-F1 (Outside) | Macro-F1 |
| -------- | ----------------- | ------------------ | -------- |
| 3        | 0.861             | 0.459              | 0.660    |
| 5        | 0.919             | 0.575              | 0.747    |
| 7        | 0.936             | 0.590              | 0.763    |
| 9        | 0.960             | 0.611              | 0.785    |
| 11       | 0.979             | 0.623              | 0.801    |
| 13       | 0.992             | 0.627              | 0.809    |

## <a name="Requirements"></a>**Requirements**

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

## <a name="Run-Project"><a/>Run Project

To run our project code, you can either run an interactive CLI or a set of pre-written tests via doctest.

#### <a name="Run Classifier"></a>Run Classifier

```bash
# Run project.
python src/classifier.py
```

#### <a name="Run-Doctests"></a>Run Doctests


```bash
# Run doctests.
python -m doctest -v src/classifier.py
```