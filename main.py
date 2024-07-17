from urllib.request import urlopen
import json
import pandas as pd
response = urlopen(
    "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json")
json_data = response.read().decode('utf-8', 'replace')
d = json.loads(json_data)
df = pd.DataFrame(d)
df.to_csv('test.csv')
print(df)
