import base64
import json                    
from sys import exit
import requests
import socket
# print(socket.gethostbyname(socket.gethostname()))
def verify(img1 , img2):
    api = "http://0.0.0.0:5000/verify"
    # f = open('deepface/api/deepface.postman_collection.json')
    headers = {'Content-type': 'application/json'}
    f = open('data2.json')
    data = json.loads(f.read())
    data2 = json.loads(data)
    # data2["max_threshold_to_verify"] = 0.45
    # data2['enforce_detectio'] = False
    data2['img'] = [{'img1': "", 'img2': ""} for i in range(len(img2))]
    # for i in range(len(img2)):
    #     data2['img'][i] = {}
    # exit(0)
    # data2 = data2['img'].pop()
    with open(img1, "rb") as f:
        im_bytes = f.read()        
    im_b64_1 = base64.b64encode(im_bytes).decode("utf8")
    
    for i in range(len(img2)):
        with open(img2[i], "rb") as f:
            im_bytes = f.read()        
        im_b64_2 = base64.b64encode(im_bytes).decode("utf8")
        data2['img'][i]['img1'] = "data:image/jpeg;base64," + str(im_b64_1)
        data2['img'][i]['img2'] = "data:image/jpeg;base64," + str(im_b64_2)
        
    data2 = json.dumps(data2)
    
    response = requests.post(api, data=data2, headers=headers).text
    response = json.loads(response)
    
    
    return response
    
def detect(img_path):
    api = "http://0.0.0.0:5000/represent"
    # f = open('deepface/api/deepface.postman_collection.json')
    headers = {'Content-type': 'application/json'}
    f = open('data2.json')
    data = json.loads(f.read())
    data2 = json.loads(data)
    # data2["max_threshold_to_verify"] = 0.45
    # data2['enforce_detectio'] = False
    # for i in range(len(img2)):
    #     data2['img'][i] = {}
    # exit(0)
    # data2 = data2['img'].pop()
    if type(img_path) == str:
        with open(img_path, "rb") as f:
            im_bytes = f.read()        
        im_b64_1 = base64.b64encode(im_bytes).decode("utf8")
        # for i in range(len(img2)):
        #     with open(img2[i], "rb") as f:
        #         im_bytes = f.read()        
        #     im_b64_2 = base64.b64encode(im_bytes).decode("utf8")
        data2['img'] = "data:image/jpeg;base64," + str(im_b64_1)
        # data2['img'][i]['img2'] = "data:image/jpeg;base64," + str(im_b64_2)
    elif type(img_path) == list:
        data2['img'] = [{'img1': ""} for i in range(len(img_path))]
        for i, img in enumerate(img_path):
            with open(img, "rb") as f:
                im_bytes = f.read()        
            im_b64_1 = base64.b64encode(im_bytes).decode("utf8")
            # for i in range(len(img2)):
            #     with open(img2[i], "rb") as f:
            #         im_bytes = f.read()        
            #     im_b64_2 = base64.b64encode(im_bytes).decode("utf8")
            data2['img'][i]['img1'] = "data:image/jpeg;base64," + str(im_b64_1)
            
    # print(data2['img'][-1]['img1'])
    data2 = json.dumps(data2)
    response = requests.post(api, data=data2, headers=headers).text
    response = json.loads(response)
    
    
    return response
