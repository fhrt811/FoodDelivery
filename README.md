## Create Environment
```
Create a folder in pwd
```
``` 
Create a README.md file
```
```
Creat requirements.txt file
```
```
Add all the required packages in requirements.txt file as well as '-e .' also
```
```
Create a setup.py file and import setup and find_packages from setuptools
and import List from typing
```
```
define a function 'get_requirements' in setup.py file for requirements.txt to run with the help of seltup.py
and give the informan=tion like Name of project, version, author, author email,install_requires, packages
```
```
Create a folder 'notebooks'
in notebooks create a folder 'Data' and in data folder add the csv file for the project, and all the jupyter notebook task like EDA and FE will be performed in this notebooks folder
```
```
Create a .gitignore file in main folder and add environment name in .gitignore file
```
```
Create a folder src
```
```
add a file __init__.py (to act src as a package)
add logger.py, exception.py, utils.py(for creating general functionality)
```
```
Create a components folder in src folder
in components folder add files __init__.py, data_ingeation.py, data_transformation.py, model_trainer.py
```
```
Create a pipeline folder in src folder
in pipeline folder add files __init__.py, prediction_pipeline.py, training_pipeline.py
```
```
Create a repository in github
```
```
add, commit and push all the folders in github
```
```
Do EDA in EDA.ipynb file in notebooks folder, load dataset and perform all the EDA functions to the dataset.
```
```
Perform all the automation in a file named ModelTraining created in notebooks folder.
First import the requirements:
1. Handling missing values (from sklearn.impute import SimpleImputer)
2. Feature scaling (from sklearn.preprocessing import StandardScaler)
3. Performing Ordinal Encoding (from sklearn.preprocessing import OrdinalEncoder)
4. Creating pipeline to perform the above operations in an order (from sklearn.pipeline import Pipeline)
5. grouping these operations (from sklearn.compose import ColumnTransformer)
```
```
For Numerical features:
Create Numerical pipeline and perform the operations needed for numerical features
```
```
For Categorical features:
Create Categorical pipeline and perform the oprations needed for ordinal features
```
```
Now combine the Numerical Pipeline and Categorical piepline using column transformer
```
```

```