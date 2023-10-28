## HEICODERS AI300 Capstone Project ##

- root_directory (e.g., sep23-team04)
    - folder_name1
        - subfolder_name1
            - file1
            - file2
        - subfolder_name2
    - folder_name2
        - file3
    - file4



- Team Number & names of team members
```
Team 4
Muhammad Hidayat Bin Abdul Wahid
Hee Poh Shin
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


