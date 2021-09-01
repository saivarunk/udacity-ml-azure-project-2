import requests
import json

# URL for the web service
scoring_uri = 'http://169c9a03-8da5-4a6a-bb83-9627c173fe5f.eastus2.azurecontainer.io/score'

# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 17,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 971,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": 1,
            "job": 1,
            "loan": 1,
            "marital": "married",
            "month": 5,
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": 0,
            "previous": 1
          },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 471,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": 1,
            "job": 1,
            "loan": 1,
            "marital": "married",
            "month": 5,
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": 0,
            "previous": 1
          },
      ]
    }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, json=data, headers=headers)
print(resp.json())
