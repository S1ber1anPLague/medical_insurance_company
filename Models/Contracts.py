import json
import os, json
from Models.Contract import Contract
from Utilities import Utilities as utils 
import pandas as pandas

class Contracts:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'Source/contracts.json')
    def __init__(self):
        self.__contracts = list()
    def __len__(self):
        return len(self.__contracts)
    
    def __iter__(self):
        return ContractsIterator(self.__contracts)

    def add(self, contract: Contract):
        self.__contracts.append(contract)
        return contract.id
    
    def delete(self, id: int):
        con = self.get_by_id(id)
        if con:
            self.__contracts.remove(con)
            return True
        return False
    
    def edit(self, id: int, contract: Contract):
        con = self.get_by_id(id)
        if con:
            con.clientId = contract.clientId
            con.employeeId = contract.employeeId
            con.hospitalId = contract.hospitalId
            con.price = contract.price
            con.conclusionDate = contract.conclusionDate
            con.status = contract.status
            con.cost = contract.cost
            return True
        return False

    def get_by_id(self, id: int):
        for con in self.__contracts:
            if con.id == id:
                return con
        return None
    
    def save(self):
        utils.save(self.__filename, self.__contracts)

    def read(self):
        self.__contracts= list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            contract = Contract(elem['id'], elem['clientId'], elem['employeeId'], elem['hospitalId'], 
                elem['price'], elem['conclusionDate'], elem['status'])
            self.add(contract)

    def get_contracts_table(self, hospitals, clients, employees):
        id_arr = []
        client_arr = []
        employee_arr = []
        hospital_arr = []
        price_arr = []
        conclusionDate_arr = []
        status_arr = []
        for elem in self.__contracts:
            id_arr.append(elem.id)
            client_arr.append(elem.get_client_str(clients))
            employee_arr.append(elem.get_employee_str(employees))
            hospital_arr.append(elem.get_hospital_str(hospitals))
            price_arr.append(elem.price)
            conclusionDate_arr.append(elem.conclusionDate)
            status_arr.append(elem.get_status())
        return pandas.DataFrame(
            {"Айди": id_arr,
            "Клиент": client_arr,
            "Сотрудник": employee_arr,
            "Лечебное учреждение": hospital_arr,
            "Цена": price_arr,
            "Дата заключения договора": conclusionDate_arr,
            "Статус": status_arr,},
            index=None)

    def get_done_contracts_table(self, hospitals, clients, employees):
        id_arr = []
        client_arr = []
        employee_arr = []
        hospital_arr = []
        price_arr = []
        conclusionDate_arr = []
        status_arr = []
        for elem in self.__contracts:
            if elem.status:
                id_arr.append(elem.id)
                client_arr.append(elem.get_client_str(clients))
                employee_arr.append(elem.get_employee_str(employees))
                hospital_arr.append(elem.get_hospital_str(hospitals))
                price_arr.append(elem.price)
                conclusionDate_arr.append(elem.conclusionDate)
                status_arr.append(elem.get_status())
        return pandas.DataFrame(
            {"Айди": id_arr,
            "Клиент": client_arr,
            "Сотрудник": employee_arr,
            "Лечебное учреждение": hospital_arr,
            "Цена": price_arr,
            "Дата заключения договора": conclusionDate_arr,
            "Статус": status_arr,},
            index=None)

    def get_new_id(self):
        max = 0
        for el in self.__contracts:
            if el.id > max:
                max = el.id
        return max + 1


class ContractsIterator:
   def __init__(self, contracts):
       self.__contracts = contracts
       self._index = 0
   def __next__(self):
        try:
            result = self.__contracts[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration