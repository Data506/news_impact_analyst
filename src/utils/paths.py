import os
import sys

# Detect root folder (named "stock_system") regardless of cwd or file
def find_project_root(project_name: str = "news_impact_analyst") -> str:
    current_dir = os.path.abspath(__file__)
    while True:
        current_dir = os.path.dirname(current_dir)
        if os.path.basename(current_dir) == project_name:
            return current_dir
        if current_dir == "/" or current_dir.endswith(":\\"):
            raise RuntimeError(f"Project root '{project_name}' not found.")

PROJECT_ROOT = find_project_root()

# Append to sys.path only if not already there
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Data directories
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, "external")

# Notebooks
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "notebooks")

# Source code
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
FEATURES_DIR = os.path.join(SRC_DIR, "features")
MODELS_DIR = os.path.join(SRC_DIR, "models")
EVALUATION_DIR = os.path.join(SRC_DIR, "evaluation")
UTILS_DIR = os.path.join(SRC_DIR, "utils")

# Reports and tracking
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
MLRUNS_DIR = os.path.join(PROJECT_ROOT, "mlruns")

# Airflow and API
DAGS_DIR = os.path.join(PROJECT_ROOT, "dags")
API_DIR = os.path.join(PROJECT_ROOT, "api")

# Output
MODELS_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "models")
