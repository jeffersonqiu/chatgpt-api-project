from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from helper.prompts import new_prompt, instruction_str, context
from helper.note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from helper.pdf import jeff_resume_engine

load_dotenv()

# population_path = os.path.join("data", "population.csv")
# population_df = pd.read_csv(population_path)

# population_query_engine = PandasQueryEngine(
#     df=population_df, verbose=True, instruction_str=instruction_str
# )
# population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    # QueryEngineTool(
    #     query_engine=population_query_engine,
    #     metadata=ToolMetadata(
    #         name="population_data",
    #         description="this gives information at the world population and demographics",
    #     ),
    # ),
    QueryEngineTool(
        query_engine=jeff_resume_engine,
        metadata=ToolMetadata(
            name="jefferson_data",
            description="this gives detailed information about Jefferson's CV",
        ),
    ),
]

# llm = OpenAI(model="gpt-3.5-turbo-0613")
llm = OpenAI(model="gpt-4-turbo-preview")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
