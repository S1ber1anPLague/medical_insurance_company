import pandas as pandas
from Models.Employee import Employee
import json
import os, json
from Utilities import Utilities as utils

class Employees():
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,"../","Source/employees.json")

    def __init__(self):
        self.__employees = list()
    def __len__(self):
        return len(self.__employees)
    def __iter__(self):
        return EmployeesIterator(self.__clients)


    def add(self, employee : Employee):
        self.__employees.append(employee)
        return employee.id

    def get_by_id(self, id : int):
        for employee in self.__employees:
            if(employee.id == id):
                return employee
        return None
    def delete(self, id : int):
        employee = self.get_by_id(id)
        if(employee):
            self.__employees.remove(employee)
            return True
        else:
            return False
    def edit(self, id : int, employee : Employee):
        emp = self.get_by_id(id)
        if(emp):
            emp.fio = employee.fio
            emp.phonenumber = employee.phonenumber
            emp.login= employee.login
            emp.email = employee.email
            emp.password = employee.passport
            emp.passport = employee.passport
            return True
        else:
            return False

    def save(self):
        utils.save(self.__filename, self.__employees)
        
    def read(self):
        self.__employees = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            employee = Employee(elem['fio'], elem['id'], elem['passport'], elem['phonenumber'], elem['email'],
                elem['login'], elem['password'])
            self.add(employee)
    
    def get_new_id(self):
        max = 0
        for el in self.__employees:
            if (el.id > max):
                max = el.id 
        return max + 1
    
    def get_employess_table(self):
        id_arr = []
        fio_arr = []
        phone_arr = []
        email_arr = []
        password_arr = []
        login_arr = []
        passport_arr = []
        for elem in self.__employees:
            id_arr.append(elem.id)
            fio_arr.append(elem.fio)
            phone_arr.append(elem.phonenumber)
            email_arr.append(elem.email)
            password_arr.append(elem.password)
            login_arr.append(elem.login)
            passport_arr.append(elem.passport)
        return pandas.DataFrame(
            {"ИД": id_arr,
            "ФИО": fio_arr,
            "Номер телефона": phone_arr,
            "Email": email_arr,
            "Пароль": password_arr,
            "Логин": login_arr,
            "Паспортные данные": passport_arr},
            index=None)
    
class EmployeesIterator:
    def __init__(self, employees):
        self.__employees = employees
        self._index = 0
    def __len__(self):
        return self.__employees
    def __next__(self):
        try:
            result = self.__employees[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration 

