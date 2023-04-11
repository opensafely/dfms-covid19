import pandas as pd
import numpy as np
import os
import re
import json
from collections import Counter

def match_input_files(file: str) -> bool:
    """Checks if file name has format outputted by cohort extractor"""
    pattern = r"^input_20\d\d-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])\.csv"
    return True if re.match(pattern, file) else False

def get_date_input_file(file: str) -> str:
    """Gets the date in format YYYY-MM-DD from input file name string"""
    # check format
    if not match_input_files(file):
        raise Exception("Not valid input file format")

    else:
        date = result = re.search(r"input_(.*)\.csv", file)
        return date.group(1)

def round_5(x):
    return int(5 * round(float(x)/5))

OUTPUT_DIR = "output"

for file in os.listdir(OUTPUT_DIR):
    if match_input_files(file):
        df = pd.read_csv(os.path.join(OUTPUT_DIR, file))

        date = get_date_input_file(file)
        # e.g date='2020-01-01'

        ind_conditions = [
            (df["alcohol_dependence"] == 1),
            (df["anxiety_disorder"] == 1),
            (df["chronic_pain"] == 1),
            (df["insomnia"] == 1),
            (df["mental_disorder"] == 1),
            (df["muscle_spasm"] == 1),
            (df["neurological_pain"] == 1),
            (df["sciatica"] == 1),
            (df["post_covid"] == 1),
        ]
    
        ind_values = ["alcohol_dependence", "anxiety_disorder", "chronic_pain", "insomnia", "mental_disorder", "muscle_spasm", "neurological_pain", "sciatica", "post_covid"]

        df["indication"] = np.select(ind_conditions, ind_values)

        df.to_csv(os.path.join(OUTPUT_DIR, file))  # this will overwrite