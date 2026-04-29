import subprocess
import os

import sys

def run_notebook(notebook_path):
    print(f"Running {notebook_path}...")
    # Find jupyter in the same directory as the python executable
    jupyter_path = os.path.join(os.path.dirname(sys.executable), "jupyter")
    try:
        subprocess.run([
            jupyter_path, "nbconvert", "--to", "notebook", "--execute", 
            "--inplace", "--ExecutePreprocessor.timeout=600", notebook_path
        ], check=True)
        print(f"Successfully finished {notebook_path}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {notebook_path}: {e}")
        exit(1)

def main():
    notebooks = [
        "notebooks/01_extraction.ipynb",
        "notebooks/02_cleaning.ipynb",
        "notebooks/03_eda.ipynb",
        "notebooks/04_statistical_analysis.ipynb",
        "notebooks/05_final_load_prep.ipynb"
    ]
    
    for nb in notebooks:
        if os.path.exists(nb):
            run_notebook(nb)
        else:
            print(f"Warning: {nb} not found.")

if __name__ == "__main__":
    main()
