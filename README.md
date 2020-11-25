# DataMiningProject
Comp 5130 Rule-Based Classifications

## Table of Contents

* [**Requirements**](#Requirements)
* [**Install**](#Install)
* [**Run Project**](#Run-Project)
  * [**Run Classifier**](#Run-Classifier)
  * [**Run Doctests**](#Run-Doctests)

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