# SwissADME, evaluation of evaluate pharmacokinetics, drug-likeness and medicinal chemistry friendliness of small molecules
## Model identifiers
- Slug: swiss-adme
- Ersilia ID: eos7ack
- Tags: ADMET

# Model description
Fast yet robust predictive models for physicochemical properties, pharmacokinetics, drug-likeness and medicinal chemistry friendliness.
- Input: SMILES
- Output: Physicochemical property, ADME (Probabilities, scores and real numbers)
- Model type: Classification, Regression
- Training set: 10000 Molecules
- Mode of training: Online

# Source code
Source Publication: https://www.nature.com/articles/srep42717
- Code: The model uses the web application available at http://www.swissadme.ch/index.php
- Checkpoints: N/A

# License
State the licences used which are GPL v3 license used by Ersilia and the license used by the source code, if any exists. Use [this guide]() on how to license new models to be incorporated into Ersilia's model hub 

# History 
- We have developed a python script that accesses the web server available at http://www.swissadme.ch/index.php to run the predictions.
- `requests` and `beautifulSoup` libraries are used to post the input to the server and fetch the results.
- Model was incorporated into Ersilia on 10/11/2022


# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
