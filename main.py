import os
from dotenv import load_dotenv
from helper.note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from helper.pdf import pdf_engine_generator
from helper.csv import csv_engine_generator
from helper.prompts import context

load_dotenv()

# Add more engines here
jeff_resume_engine = pdf_engine_generator("jefferson.pdf", "jefferson")
data_scientist_population_engine = csv_engine_generator("data_scientist_population.csv", "data_scientist_population")


tools = [
    note_engine,
    # And add in the toolkit here
    QueryEngineTool(
        query_engine=data_scientist_population_engine,
        metadata=ToolMetadata(
            name="ds_salary_data",
            description="this gives information at the salary for Data Scientists",
        ),
    ),
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
