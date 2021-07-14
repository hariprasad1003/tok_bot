import random
import json

def get_data(data_file_name):

    data_file = open(data_file_name)

    data = json.load(data_file)

    kural = data["kural"]

    result = kural[random.randint(0,len(kural))]

    # print(result)

    return result

def get_secrets(secrets_file_name):

    secrets_file = open(secrets_file_name)

    secrets_data = json.load(secrets_file)

    secrets = secrets_data["secrets"]

    # print(secrets)

    return secrets