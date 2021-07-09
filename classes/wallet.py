import uuid
import hashlib
import json

class Wallet(object):
    def __init__(self):
        self.balance = 0
        self.history = []
        self.generate_unique_id()



def generate_unique_id():
    unique_id = str(uuid.uuid4())
    balance = 0
    with open('content\wallets\''+unique_id+'.json','w') as f:
        json.dump(unique_id,f,ensure_ascii=False, sort_keys=False,indent=4)
    print(unique_id)
    add_balance(unique_id,balance)



    
    
def add_balance(unique_id,balance):
        balance = int(input("Solde?"))
        with open('content\wallets\''+unique_id+'.json','a') as f:
            json.dump(balance,f, ensure_ascii=False, sort_keys=False,indent=6)
        sub_balance(unique_id,balance)


def sub_balance(unique_id,balance):
    question = input("Soustraire du solde? y/N")
    if question == "y":
        sub = int(input("Somme a soustraire?"))
        balance = balance - sub 
        print("Nouveau solde",balance)
        with open('content\wallets\''+unique_id+'.json','a') as f:
            json.dump(balance,f, ensure_ascii=False, sort_keys=False,indent=8)
    elif question == "N":
        print("Solde actuelle",balance)
    else:
        print("Veuillez rentrer une réponse correcte")
        sub_balance(unique_id,balance)


            



generate_unique_id()







