from datetime import datetime
from numpy import fabs
from Models.Client import Client
from Models.Clients import Clients
from Models.Employee import Employee
from Models.Employees import Employees
from Models.Hospitals import Hospitals
from Models.Hospital import Hospital
from Models.Contract import Contract
from Models.Contracts import Contracts

main_commands = {
    "q": -1,
    "help": 0,
    "clients" : 1,
    "employees" : 2,
    "hospitals" : 3,
    "contracts" : 4
}

clients = Clients()
employees = Employees()
hospitals = Hospitals()
contracts = Contracts()

def help():
    print(
"""
- Чтобы перейти в управление клиентами введите "clients"
- Чтобы перейти в управление сотрудниками введите "employees"
- Чтобы перейти в управление лечебными учреждениями введите "hospitals"
- Чтобы перейти в управление договрами введите "contracts"
- Чтобы посмотреть инструкцию, введите "help"
- Чтобы выйти, введите "q"
""")
    

def main_menu():
    command = input("Введите команду: ")
    if command in main_commands:
        i = main_commands[command]
        if i == -1:
            exit()
        elif i == 0:
            help()
            main_menu()
        elif i == 1:
            clients_menu()
        elif i == 2:
            employees_menu()
        elif i == 3:
            hospital_menu()
        elif i == 4:
            contract_menu()
    else:
        print('''\nНекорректный ввод... 
        Прочитайте инструкцию по использованию данной программы:''')
        help()
        main_menu()

def clients_menu():
    try:
        global clients
        answer = int(input("Для того чтобы просмотреть список всех клиентов, введите 1. Чтобы добавить клиента, введите 2. Чтобы удалить клиента, введите 3. (Чтобы вернуться назад нажмите 0)\n"))
        if answer == 0:
            main_menu()
        if answer == 1:
            get_clients()
        if answer == 2:
            add_client()
        if answer == 3:
            del_client()
    except:
        print('Что-то пошло не так!')

def get_clients():
    global clients
    print(clients.get_clients_table())
    clients_menu()

def add_client():
    fio = input('Введите ФИО: ')
    passport = input('Введите паспорт: ')
    phonenumber = input('Введите номер телефона: ')
    email = input('Введите email: ')
    occupation = input('Введите ваш вид деятельности: ')
    dateofbirth = input('Введите дату рождения (через точку - пример: 01.01.2000): ')
    try:
        datetime.strptime(dateofbirth, "%d.%m.%Y")
    except:
        print('Неправильный формат введенных данных!')
        clients_menu()

    global clients
    client = Client(fio, clients.get_new_id(), passport, phonenumber, email, dateofbirth, occupation)
    clients.add(client)
    clients.save()
    print('Клиент успешно создан.') 
    clients_menu()
        
def del_client():
    try:
        id = int(input('Введите ID клиента: '))
        ans = input(f'Вы точно хотите удалить клиента №{id}? (y/n)\n')
        if ans == 'y':
            global clients
            ok = clients.delete(id)
            if ok:
                clients.save()
                print('Клиент успешно удален.')
                clients_menu()
            else:
                print('Произошла ошибка при удалении клиента!')
                clients_menu()
        else:
            clients_menu()
    except:
        print('Что-то пошло не так!')
        clients_menu()

def employees_menu():
    global employees
    try:
        answer = int(input("Для того чтобы просмотреть список всех сотрудников, введите 1. Чтобы добавить сотрудника, введите 2. Чтобы удалить сотрудника, введите 3\n"))
        if answer == 0:
            main_menu()
        if answer == 1:
            get_employees()
        if answer == 2:
            add_employee()
        if answer == 3:
            del_employee()
    except:
        print('Что-то пошло не так!')
        employees_menu()

def get_employees():
    global employees
    print(employees.get_employess_table())
    employees_menu()

def add_employee():
    fio = input('Введите ФИО: ')
    passport = input('Введите паспорт: ')
    phonenumber = input('Введите номер телефона: ')
    email = input('Введите email: ')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    global employees
    employee = Employee(fio, employees.get_new_id(), passport, phonenumber, email, login, password)
    employees.add(employee)
    employees.save()
    print('Сотрудник успешно создан.') 
    employees_menu()
        
def del_employee():
    try:
        id = int(input('Введите ID сотрудника: '))
        ans = input(f'Вы точно хотите удалить сотрудника №{id}? (y/n)\n')
        if ans == 'y':
            global employees
            ok = employees.delete(id)
            if ok:
                employees.save()
                print('Сотрудник успешно удален.')
                employees_menu()
            else:
                print('Произошла ошибка при удалении сотрудника!')
                employees_menu()
        else:
            employees_menu()
    except:
        print('Что-то пошло не так!')
        employees_menu()


def hospital_menu():
    try:
        answer = int(input("Для того чтобы просмотреть список всех лечебных учреждений, введите 1. Чтобы добавить учреждение, введите 2. Чтобы удалить учреждение, введите 3\n"))
        if answer == 0:
            main_menu()
        if answer == 1:
            get_hospitals()
        if answer == 2:
            add_hospital()
        if answer == 3: 
            del_hospital()
    except:
        print('Что-то пошло не так!')
        hospital_menu()

def get_hospitals():
    global hospitals
    print(hospitals.get_hospitals_table())
    hospital_menu()

def add_hospital():
    name = input('Введите название: ')
    address = input('Введите адрес: ')
    phonenumber = input('Введите номер телефона: ')
    email = input('Введите email: ')
    global hospitals
    hospital = Hospital(hospitals.get_new_id(), address, name, phonenumber, email)
    hospitals.add(hospital)
    hospitals.save()
    print('Лечебное учреждение успешно создано.') 
    hospital_menu()
        
def del_hospital():
    try:
        id = int(input('Введите ID лечебного учреждения: '))
        ans = input(f'Вы точно хотите удалить лечебное учреждение №{id}? (y/n)\n')
        if ans == 'y':
            global hospitals
            ok = hospitals.delete(id)
            if ok:
                hospitals.save()
                print('Лечебное учреждение успешно удалено.')
                hospital_menu()
            else:
                print('Произошла ошибка при удалении лечебного учреждения!')
                hospital_menu()
        else:
            hospital_menu()
    except:
        print('Что-то пошло не так!')
        hospital_menu()


def contract_menu():
    try:
        answer = int(input(
"""
- Для того чтобы просмотреть список всех договоров, введите 1. 
- Чтобы просмотреть список договоров, приведенных в исполнение введите 2. 
- Чтобы просмотреть определенный договор, введите 3. 
- Чтобы добавить новый договор, введите 4.
- Чтобы удалить договор, введите 5.
- Чтобы привести договор в исполнение, введите 6.\n
"""))
        if answer == 0:
            main_menu()
        if answer == 1:
            get_contracts()
        if answer == 2:
            get_done_contracts()
        if answer == 3:
            get_contract()
        if answer == 4:
            add_contract()
        if answer == 5: 
            del_contract()
        if answer == 6:
            set_done()
    except:
        print('Что-то пошло не так!')
        contract_menu()

def get_contracts():
    global contracts, clients, employees
    print(contracts.get_contracts_table(hospitals, clients, employees))
    contract_menu()

def get_done_contracts():
    global contracts, clients, employees
    print(contracts.get_done_contracts_table(hospitals, clients, employees))
    contract_menu()

def get_contract():
    global contracts
    try:
        id = int(input('Введите ID договора: '))
        contract = contracts.get_by_id(id)
        if contract:
            print(contract.get_string())
            contract_menu()
        else:
            print('Нет такого договора!')
            contract_menu()
    except:
        print('Что-то пошло не так!')
        contract_menu()


def add_contract():
    global clients, employees, hospitals
    print(clients.get_clients_table())
    client = int(input('Введите ID клиента: '))
    print(employees.get_employess_table())
    employee = int(input('Введите ID сотрудника: '))
    print(hospitals.get_hospitals_table())
    hospital = int(input('Введите ID лечебного учреждения: '))
    price = float(input('Введите цену: '))
    date = input('Введите дату заключения договора: ')
    try:
        datetime.strptime(date, "%d.%m.%Y")
    except:
        print('Неправильный формат введенных данных!')
        contract_menu()
    global contracts
    contract = Contract(contracts.get_new_id(), client, employee, hospital, price, date, False)
    contracts.add(contract)
    contracts.save()
    print('Договор успешно создан.') 
    contract_menu()
        
def del_contract():
    try:
        id = int(input('Введите ID договора: '))
        ans = input(f'Вы точно хотите удалить договор №{id}? (y/n)\n')
        if ans == 'y':
            global contracts
            ok = contracts.delete(id)
            if ok:
                contracts.save()
                print('Договор успешно удален.')
                contract_menu()
            else:
                print('Произошла ошибка при удалении договора!')
                contract_menu()
        else:
            contract_menu()
    except:
        print('Что-то пошло не так!')
        contract_menu()

def set_done():
    try:
        id = int(input('Введите ID договора: '))
        global contracts
        contract = contracts.get_by_id(id)
        contract.set_done()
        contracts.save()
        print('Договор успешно приведен в исполнение.')
        contract_menu()
    except:
        print('Что-то пошло не так!')
        set_done()

print("Добро пожаловать")
clients.read()
employees.read()
contracts.read()
hospitals.read()
help()
main_menu()