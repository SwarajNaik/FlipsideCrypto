from flipside import Flipside
from sequels import pools


flipside = Flipside("aacbd3da-5f83-4039-a08f-92ccd15fa9f1", "https://api-v2.flipsidecrypto.xyz")


sql = """
SELECT 
  date_trunc('hour', block_timestamp) as hour,
  count(distinct tx_hash) as tx_count
FROM ethereum.core.fact_transactions 
WHERE block_timestamp >= GETDATE() - interval'7 days'
GROUP BY 1
"""


query_result_set = flipside.query(sql)
print(query_result_set)