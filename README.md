# Introduction

This project aims to explore the capability of LLM to explore internal information, leveraging llama_index library. This is a substantially more efficient method than fine-tuning or let alone retraining of the LLM model. 

## Example
Input: when jeff go to NTU?
<br>:: Note the bad grammar, to challenge the model

Output: <br>
*Thought: I need to use the jefferson_data tool to find out when Jefferson went to NTU.*<br>
**Action**: jefferson_data<br>
**Action Input**: {'input': 'NTU'}<br>
**Observation**: Nanyang Technological University

*Thought: The observation indicates that NTU refers to Nanyang Technological University, but it doesn't provide the specific information about when Jefferson went to NTU. I need to refine my query to specifically ask for the year Jefferson attended NTU.*<br>
**Action**: jefferson_data<br>
**Action Input**: {'input': 'education'}<br>
**Observation**: Bachelor of Mechanical Engineering with minor in Business Aug 2013 – May 2017 from Nanyang Technological University with CGPA 4.88/5.00 (Top 5% of cohort, 3 x Deans List)

*Thought: I can answer without using any more tools.*<br>
**Answer**: Jefferson attended Nanyang Technological University from August 2013 to May 2017, where he pursued a Bachelor of Mechanical Engineering with a minor in Business.

