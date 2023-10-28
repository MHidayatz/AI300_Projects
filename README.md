## HEICODERS AI300 Capstone Project ##

## Team Number & names of team members
```
Team 4
Muhammad Hidayat Bin Abdul Wahid
Hee Poh Shin
```

## Folder Structure

```
├── data
│   └── filename_edited.xlsx
│   └── filename.xlsx
├── model
│   └── best_clf.pkl
├── notebooks
│   └── WorkingNotebook.ipynb
├── src
│   └── static
│      └── style.css
│   └── templates
│      └── index.html
│   └── app.py
│   └── input_processing.py
│   └── model.py
├── Readme.md
├── requirements.txt

```

- Website URL of deployed Flask web application 

## Details on chosen final model and model parameters

```
CatBoostClassifier

{'learning_rate': 0.1,
 'l2_leaf_reg': 0.01,
 'iterations': 400,
 'depth': 9,
 'border_count': 64}


```


## Offline AUC metric of chosen final model

```
 CatBoostClassifier
 AUC: 0.9058097286413764
 Accuracy: 0.8971783835485414

```


## About This Repo

- Package dependencies can be found in `requirements.txt` file.
- Command to start Flask app: `python src/app.py`


