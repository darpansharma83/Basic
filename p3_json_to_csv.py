#use python3 and install panadas and sys
import sys 
import pandas as pd

read_json = pd.read_json(sys.argv[1],lines=True)
read_json.to_csv(sys.argv[2])
