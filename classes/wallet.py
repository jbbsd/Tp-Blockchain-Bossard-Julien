import uuid
import hashlib
import json

class Wallet(object):
    def __init__(self):
        self.unique_id = uuid.uuid4()





def generate_unique_id():
    
    unique_id = uuid.uuid4()
    wallet_id = json.dumps(unique_id.int)
    with open('wallets','w') as f:
        json.dump(wallet_id,f,indent=4, ensure_ascii=False, sort_keys=False)


        
generate_unique_id()

