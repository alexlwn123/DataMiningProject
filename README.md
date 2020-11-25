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

#### <a name="Intro"></a>**Problem Introduction**
#### <a name="Dataset"></a>**Dataset**

<img src="plot.png" width=200>


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

## <a name="Run-Project">Run Project<a/>

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