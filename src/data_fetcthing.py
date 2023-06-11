from flipside import Flipside
# from sequels import pools
import pandas as pd

pools = """
SELECT * FROM ethereum.uniswapv3.ez_pools 
LIMIT 100
"""

def execute_query(sql):
  flipside = Flipside("aacbd3da-5f83-4039-a08f-92ccd15fa9f1", "https://api-v2.flipsidecrypto.xyz")
  query_result_set = flipside.query(sql)
  return query_result_set

# """pip install flipside-sdk"""
# from flipside import Flipside

# """Initialize Flipside with your API Key / API Url"""
# flipside = Flipside("e3147454-8107-4d64-b673-b93b9c8e55fc", "https://api-v2.flipsidecrypto.xyz")
# sql = """SELECT * FROM ethereum.uniswapv3.ez_swaps LIMIT 100"""
# """Run the query against Flipside's query engine and await the results"""
# query_result_set = flipside.query(sql)
# print(query_result_set)

def clean_data(data):
  result = {}
  
  for column in data.columns:
    result[column] = []
  
  for record in data.records:
    for column in data.columns:
      result[column].append(record[column])
  
  return pd.DataFrame(result)

if __name__ == "__main__":
  
  sql = execute_query(pools)
  
  df = clean_data(data=sql)
