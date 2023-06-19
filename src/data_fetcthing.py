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

