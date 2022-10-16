ML-Lab-1
==============================

Предсказание болезней людей с помощью CatBoost и LGBM.


<hr>
CatBoost:
<ul>
    <li>micro</li>
    <li>precision  0.6530612244897959</li>
    <li>recall  0.4129032258064516</li>
    <li>f1  0.5059288537549407</li>
    <li>ROCAUC 0.8269506999391358</li>
</ul>

<ul>
    <li>samples</li>
    <li>precision  0.3368421052631579</li>
    <li>recall  0.2399122807017544</li>
    <li>f1  0.2668421052631579</li>
    <li>ROCAUC [0.7364082  0.59409341 0.78365009 0.79901508 0.54233254]</li>
</ul>

<hr>
LGBM
<ul>
    <li>micro</li>
    <li>precision  0.5</li>
    <li>recall  0.2064516129032258</li>
    <li>f1  0.2922374429223744</li>
    <li>ROCAUC 0.7444268614323393</li>
</ul>
        
<ul>
    <li>samples</li>
    <li>precision  0.16842105263157894</li>
    <li>recall  0.11798245614035087</li>
    <li>f1  0.1319298245614035</li>
    <li>ROCAUC [0.56534091 0.48317308 0.47487633 0.53062481 0.56817409]</li>
</ul>
<hr>
<br>

## DVC
<pre>
       +-----------------+          
       | data_processing |          
       +-----------------+          
                 *                  
                 *                  
                 *                  
      +--------------------+        
      | feature_generation |        
      +--------------------+        
                 *                  
                 *                  
                 *                  
            +-------+               
            | train |               
            +-------+*              
           **         **            
         **             **          
        *                 *         
+----------+         +-----------+  
| evaluate |         | inference |  
+----------+         +-----------+  
</pre>
<hr>
<br>
Work with experements: experemets_result.txt<br>
Work with metrics: metrics_diff_result.txt<br>
Plots: /dvc_plots/*<br>
DVC data storage: https://drive.google.com/drive/folders/1VH7MS7sFDgY69r4AADqP2EyZL2hPIR-P<br>
<br>
<hr>

# Обоснования выбора метрик

<br>

Метрики – <b> Precision, Recall, F1, ROCAUC </b>

Описание метрик:
<ul>
<li> <b>Precision</b> можно интерпретировать как долю объектов, названных классификатором положительными и при этом действительно являющимися положительными.</li>
<li> <b>Recall</b> показывает, какую долю объектов положительного класса из всех объектов положительного класса нашел алгоритм. </li>

Так как нам важно уменьшить ошибку <i>False Negative</i>r,  то есть в поставленной задаче ошибка не распознания положительного класса высока, так как мы определяем болен ли человек болезнью или нет, больше все же ориентируемся на <b>Recall</b>.

Для полной оценки модели так же используем метрики:

<b>F1</b> — среднее гармоническое <b>Precision</b> и <b>Recall</b>.
    
<b>ROCAUC</b> - оценка модели в целом, не привязываясь к конкретному порогу.
    
</ul>

Целевая метрика: <b>Recall</b>


<hr>
Project Organization <br>
Была добавлена папка src/inferenct - для запуска модели на обычных данных. <br>
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py
    │   │
    │   └── inference  <- Scripts to work with generated models
    │       └── inference.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
