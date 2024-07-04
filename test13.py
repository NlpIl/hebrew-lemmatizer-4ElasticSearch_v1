import math
import subprocess
from elasticsearch import Elasticsearch,helpers
import time
import requests
import json

Tstdict={}

def json_load(path, mode='r'):
    with open(path, mode) as reader:

        contents = json.load(reader)        
    return contents
    
def run_test():
    try:
        print("You Started Test 13 succesfully")
        data =  { "status":"Running", "progress":0 ,"result":0}
            
                    
        mappings_vectors = json_load('/home/azureuser/datadrive/hebrew_project/tests/mappings_vectors_he.json')
        settings = json_load('/home/azureuser/datadrive/hebrew_project/tests/settings_he.json')

        es = Elasticsearch("http://localhost:9200",request_timeout=1000)

        # Create an index
        if(not es.indices.exists(index="test13_index")):
            response = es.indices.create(index="test13_index", settings = settings,mappings=mappings_vectors)

        # get the txt for the test
        documents=[]
        for i in range(2,52):
            with open(f'/home/azureuser/datadrive/hebrew_project/documents/hebrew_paragraphs_1000_{i}.txt', 'r') as file:
                documents.append({"text":file.read()})

        start_time = time.time()
        total_success = 0

        for i in range(0,50,4):
            actions = []
            for j in range(1,5):
                if i+j > 50:
                    continue
                op_data = {
                    "_op_type": 'index',
                    "_index": "test13_index",
                    "_id": i+j,
                    "_source": documents[i+j-1]
                }
                actions.append(op_data)
            success, failed = helpers.bulk(es, actions)
            total_success += success
            data =  { "status":"Running", "progress": min(total_success*2 ,99) ,"result":0}
            print(total_success , "\n")
            print(time.time() - start_time , "\n")

        
        end_time = time.time()
        # Calculate duration
        duration = end_time - start_time

        # result_json = {
        #         "data": {
        #             "input": self.Testinput,
        #             "output": str(duration/60) + " Mintues"
        #         }
        #     }

        print(f"{duration}")

    
        return duration
    except  Exception as e :
        return "ERR : "+str(e)


run_test()