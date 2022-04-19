from Models.Clients import Clients
from Models.Employees import Employees
from Models.Hospitals import Hospitals
from Models.Client import Client

class Contract:
    def __init__(self, id, clientId, employeeId, hospitalId, price, conclusionDate, status = False):
        self.id = id
        self.clientId = clientId
        self.employeeId = employeeId
        self.hospitalId = hospitalId
        self.price = price
        self.conclusionDate = conclusionDate
        self.status = status

    def get_client(self, clients : Clients):
        return clients.get_by_id(self.clientId)

    def get_employee(self, employees : Employees):
        return employees.get_by_id(self.employeeId)
    
    def set_client(self, clientId):
        self.clientId = clientId

    def set_employee(self,employeeId):
        self.employeeId = employeeId

    def get_client_str(self, clients: Clients):
        try:
            return self.get_client(clients).fio
        except AttributeError:
            return ''

    def get_employee_str(self, employees : Employees):
        try:
            return self.get_employee(employees).fio
        except AttributeError:
            return ''

    def get_hospital(self, hospitals : Hospitals):
        return hospitals.get_by_id(self.hospitalId)

    def set_hospital(self, hospitalId):
        self.hospitalId = hospitalId

    def get_hospital_str(self, hospitals : Hospitals):
        try:
            return self.get_hospital(hospitals).name
        except AttributeError:
            return ''

    def get_status(self):
        if not self.status:
            return "Договор оформлен"
        else:
            return "Договор исполнен"

    def set_done(self):
        self.status = True

    def get_string(self):
        status = self.get_status()
        client = self.get_client_str(self.clientId)
        employee = self.get_employee_str(self.employeeId)
        hospital = self.get_hospital_str(self.hospitalId)
        return f'''
        Айди : {self.id}
        Клиент : {client}
        Сотрудник : {employee}
        Лечебное учреждение : {hospital}
        Цена : {self.price}
        Дата заключения договора : {self.conclusionDate}
        Статус : {status}
        '''
    




