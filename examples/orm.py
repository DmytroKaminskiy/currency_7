import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


con = sqlite3.connect('chinook.db')
con.row_factory = dict_factory

cur = con.cursor()

sql = '''
SELECT FirstName, LastName FROM customers;
'''
cur.execute(sql)

customers_list = cur.fetchall()

con.close()
##########################

class Customer:
    def __init__(self, db_object):
        self.first_name = db_object.get('FirstName')
        self.last_name = db_object.get('LastName')

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self):
        pass

customer_objects = [
    Customer(customer)
    for customer in customers_list
]

for customer in customer_objects:
    print(customer.get_full_name())
    # print(customer['FirstName'], customer['LastName'])
    # print(customer[1], customer[2])

'''
ORM
O - object
R - relation
M - mapping

Django ORM
SQLAlchemy
'''
