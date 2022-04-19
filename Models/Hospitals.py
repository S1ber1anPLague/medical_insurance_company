import pandas as pandas
from Models.Hospital import Hospital
import json
import os, json
from Utilities import Utilities as utils

class Hospitals:

    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,"../","Source/hospitals.json")

    def __init__(self):
        self.__hospitals = list()
    
    def __len__(self):
        return len(self.__hospitals)
    
    def add(self, hospital : Hospital):
        self.__hospitals.append(hospital)
        return hospital.id
    
    def get_by_id(self, id : int):
        for hosp in self.__hospitals:
            if(hosp.id == id):
                return hosp
        return None
    
    def delete(self, id : int):
        hosp = self.get_by_id(id)
        if (hosp):
            self.__hospitals.remove(hosp)
            return True
        else:
            return False
    def edit(self, id : int, hospital : Hospital):
        hosp = self.get_by_id(id)
        if(hosp):
            hosp.address = hospital.adress
            hosp.name = hospital.name
            hosp.phonenumber = hospital.phonenumber
            hosp.email = hospital.email
            return True
        else:
            return False
        
    def save(self):
        utils.save(self.__filename,self.__hospitals)
    
    def read(self):
        self.__hospitals = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            hospital = Hospital(elem['id'], elem['address'], elem['name'], elem['phonenumber'], 
                 elem['email'])
            self.add(hospital)
    def get_new_id(self):
        max = 0
        for hosp in self.__hospitals:
            if(hosp.id > max):
                max = hosp.id
        return max + 1

    def get_hospitals_table(self):
        id_arr = []
        address_arr = []
        name_arr = []
        phonenumber_arr = []
        email_arr = []
        for elem in self.__hospitals:
            id_arr.append(elem.id)
            address_arr.append(elem.address)
            name_arr.append(elem.name)
            phonenumber_arr.append(elem.phonenumber)
            email_arr.append(elem.email)
        return pandas.DataFrame(
            {"ИД": id_arr,
            "Адрес": address_arr,
            "Название": name_arr,
            "Номер телефона": phonenumber_arr,
            "Электронная почта": email_arr,},
            index=None)
class HospitalsIterator:
    def __init__(self, hospitals):
        self.__hospitals = hospitals
        self._index = 0
    def __next__(self):
        try:
            result = self.__hospitals[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration    