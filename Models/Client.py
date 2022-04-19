class Client:
    def __init__(self, fio, id, passport, phonenumber, email, dateofbirth, occupation):
        self.fio = fio
        self.passport = passport
        self.phonenumber = phonenumber
        self.email = email
        self.id = id
        self.dateofbirth = dateofbirth
        self.occupation = occupation
    def get_string(self):
        return f'''
        ИД: {self.id} 
        ФИО: {self.fio}
        Телефон: {self.phonenumber}
        Email: {self.email}
        Паспорт: {self.passport}
        Дата рождения: {self.dateofbirth}
        Род деятельности: {self.occupation}
        '''
        
