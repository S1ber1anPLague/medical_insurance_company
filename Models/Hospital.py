class Hospital:
    def __init__(self, id , address, name, phonenumber, email):
        self.id = id
        self.address = address
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
    def get_string(self):
        return f'''
        ИД: {self.id} 
        Адрес: {self.adress}
        Телефон: {self.phonenumber}
        Email: {self.email}
        '''