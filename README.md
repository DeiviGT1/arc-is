# cookiecuter - Data Analysis project 

This is a Cookiecutter template for creating a data analysis project 
## Project Features
- Python 3.8+
- Git integration
- Python preset functions

## Requirements
- git >= 2.x
- Cookiecutter Python package >= 1.4.0: 

You could install cookiecutter depending on how you manage your Python packages (pip or conda), follow the code below:

- pip:  

```
pip install cookiecutter
```

- conda: 

```
conda install -c conda-forge cookiecutter
```

## Directories Distribution
```
├── README.md
├── cookiecutter.json
├── environment.yaml
├── hooks
│   └── pos_gen_project.py
│   └── pre_gen_project.py
└── miami_ds
    ├── LICENCE
    ├── README.md
    ├── data
    │   └── .gitkeep
    ├── notebooks
    │   └── 0.0-miami_ds-introduction.ipynb
    ├── requirements.txt
    └── scripts
        └── .gitkeep
```

## Usage
In the directory that you create for the project, execute in terminal:

```
cookiecutter https://github.com/DeiviGT1/plantilla-ds.git
```