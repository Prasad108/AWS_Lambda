import os
import requests

# @author Prasad Dukale
# After configuring the env variable script will hit the scheduler API, it should be triggered by aws cloudWatch event


URL = os.environ['URL']
USERNAME = os.environ['API_USERNAME']
PASSWORD = os.environ['PASSWORD']
ENV = os.environ['ENV']
SCHEDULER_NAME = os.environ['SCHEDULER_NAME']


def lambda_handler(event, context):
    response = requests.get(URL, auth=(USERNAME, PASSWORD))
    result = '{"environment" :"' + ENV + '","scheduler": "' + SCHEDULER_NAME + '", "status_code" :"' + str(
        response.status_code) + '"}'
    print(result)
    try:
        output = response.json()
    except ValueError:
        output = response.text
    print(output)
    return output


def main():
    lambda_handler("", "")


if __name__ == '__main__':
    main()
