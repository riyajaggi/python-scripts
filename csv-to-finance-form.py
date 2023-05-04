import requests
import pandas as pd
import time

path = "insert/path/to/csv"
print(path)
print
csv = pd.read_csv(path)

url = "inserturlforform"

# For form ids check the entry id using inspect element or use a prefilled form link
form_ids = {
    "category": "entry.123456789",
    "description": "entry.123456789",
    "cost": "entry.123456789",
    "date": "entry.123456789",
    "method": "entry.123456789"
}


def submit(url, submission):
    response = requests.post(url, submission)
    response_code = response.status_code
    response_message = response.reason
    time.sleep(2)
    print(response_code)
    print(response_message)


for index, row in csv.iterrows():
    # print(row)
    category = row['Category']
    description = row['Description']
    cost = row['Amount']
    date = row['Date'].split("T")[0]
    method = "Debit"

    submission = {form_ids["category"]: category,
                  form_ids["description"]: description,
                  form_ids["cost"]: cost,
                  form_ids["date"]: date,
                  form_ids["method"]: method}
    print(submission)

    try:
        submit(url, submission)
    except Exception as e:
        print("ERROR: " + e)

    print(index+1, 'request sent')
    print()

print("\nEND")
