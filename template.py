import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNN_Classifier'

list_of_files = [
    '.github/workflows/.gitkeep', 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # seperates into directories and file
    filedir, filename = os.path.split(filepath)

    #checking if directory path is exits, if exist we create a directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory, {filedir} for the file: {filename}")
    # if not file exists (or) if file exists and if it consists of no info inside the file
    # then I will create the file 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # writing that file (no content, just creating that file)
        with open(filepath, "w") as f:
            pass 
        # logging 
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists..!") 


