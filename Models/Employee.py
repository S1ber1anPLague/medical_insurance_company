class Employee:
    def __init__(self, fio, id, passport, phonenumber, email, login, password):
        self.fio=fio
        self.id=id
        self.passport=passport
        self.phonenumber=phonenumber
        self.email=email
        self.login=login
        self.password=password
    def get_string(self):
        return f'''
        ИД: {self.id} 
        ФИО: {self.fio}
        Телефон: {self.phonenumber}
        Email: {self.email}
        Паспорт: {self.passport}
        Логин: {self.login}
        Пароль: {self.password}
        '''
    def set_password(self, password):
        newPassword = input("Укажите новый пароль")
        self.password = newPassword


