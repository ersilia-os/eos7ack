# imports
import os
import csv
import joblib
import sys
import requests
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read smiles list
smiles_list = []
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
    	smiles_list += [r[0]]
            
smiles=smiles_list[0]
for s in smiles_list[1:]:
    smiles=smiles+"\r\n"+s

root_url = "http://www.swissadme.ch/"
url = "http://www.swissadme.ch/index.php"
data = {"smiles": smiles }
sess = requests.Session()
r1 = sess.post(url, data = data)
soup = BeautifulSoup(r1.text, features = 'html.parser')

for a in soup.select('a[href^="results"]'):
    file_url = a['href']
    
file = urljoin(root_url, file_url)
file_data = requests.get(file).content
df = pd.read_csv(io.StringIO(file_data.decode('utf-8')))
df.drop(['Molecule'], axis=1,inplace=True)
df.to_csv(output_file,index=False)

