import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from helper.prompts import new_prompt, instruction_str

def csv_engine_generator(csv_file_name, index_name):
    csv_path = os.path.join("data", csv_file_name)
    csv_df = pd.read_csv(csv_path)

    csv_query_engine = PandasQueryEngine(
        df=csv_df, verbose=True, instruction_str=instruction_str
    )
    csv_query_engine.update_prompts({"pandas_prompt": new_prompt})

    return csv_query_engine
