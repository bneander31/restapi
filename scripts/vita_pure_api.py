import json
import requests  # http requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():  # --> Lists all this out
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("There is an error!")
    data = r.json()
    # print(type(json.dumps(data)))
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:  # --> User Interaction
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print(dir(r2))
            print(r2.json())
    return data


def create_update():
    new_data = {
        'user': 1,
        'content': 'Some More Cool Content'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def do_obj_update():
    new_data = {
        'content': 'New obj data'
    }
    r = requests.put(BASE_URL + ENDPOINT + "1/", data=new_data)
    # new_data = {
    #     'id': 1,
    #     'content': 'Some More Cool Content'
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def do_obj_delete():
    new_data = {
        'content': 'New obj data'
    }
    r = requests.delete(BASE_URL + ENDPOINT + "1/")
    # new_data = {
    #     'id': 1,
    #     'content': 'Some More Cool Content'
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


print(do_obj_update())

# print(get_list())
# get_list()
# print(create_update())
