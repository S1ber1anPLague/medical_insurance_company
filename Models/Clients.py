import json
from Models.Client import Client
import pandas as pandas
import os, json
from Utilities import Utilities as utils

class Clients:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'Source/clients.json')

    def __init__(self):
        self.__clients = list()

    def __len__(self):
        return len(self.__clients)

    def __iter__(self):
        return ClientsIterator(self.__clients)


    def add(self, client : Client):
        self.__clients.append(client)
        return client.id

    def get_by_id(self, id : int):
        for client in self.__clients:
            if client.id == id:
                return client
        return None

    def delete(self, id : int):
        client = self.get_by_id(id)
        if (client):
            self.__clients.remove(client)
            return True
        else:
            return False
    def edit(self, id : int, client : Client):
        cl = self.get_by_id(id)
        if(cl):
            cl.fio = client.fio
            cl.phonenumber = client.phonenumber
            cl.occupation = client.occupation
            cl.dateofbirth = client.dateofbirth
            cl.email = client.email
            cl.passport = client.passport
            return True
        else:
            return False

    def save(self):
        utils.save(self.__filename, self.__clients)
        
    def read(self):
        self.__clients = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            client = Client(elem['fio'], elem['id'],  elem['passport'], elem['phonenumber'], 
                elem['email'], elem['dateofbirth'], elem['occupation'])
            self.add(client)
    
    def get_new_id(self):
        max = 0
        for el in self.__clients:
            if el.id > max:
                max = el.id 
        return max + 1
    
    def get_clients_table(self):
        id_arr = []
        fio_arr = []
        phone_arr = []
        email_arr = []
        passport_arr = []
        date_of_birth_arr = []
        occupation_arr = []
        for elem in self.__clients:
            id_arr.append(elem.id)
            fio_arr.append(elem.fio)
            phone_arr.append(elem.phonenumber)
            email_arr.append(elem.email)
            passport_arr.append(elem.passport)
            date_of_birth_arr.append(elem.dateofbirth)
            occupation_arr.append(elem.occupation)
        return pandas.DataFrame(
            {"ИД": id_arr,
            "ФИО": fio_arr,
            "Номер телефона": phone_arr,
            "Email": email_arr,
            "Паспорт": passport_arr,
            "Дата рождения": date_of_birth_arr,
            "Род деятельности": occupation_arr},
            index=None)
    
class ClientsIterator:
    def __init__(self, clients):
        self.__clients = clients
        self._index = 0
    def __next__(self):
        try:
            result = self.__clients[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration    
    
        
    
    

