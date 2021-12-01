# Note (Example is valid for Python v2 and v3)
from __future__ import print_function

import sys

#sys.path.insert(0, 'python{0}/'.format(sys.version_info[0]))

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'Demidov1988@',
    'host': 'localhost',
    'port': '3304',
    'database': 'demidov_db',
    # 'client_flags': [ClientFlag.SSL],
    # 'ssl_ca': '/opt/mysql/ssl/ca.pem',
    # 'ssl_cert': '/opt/mysql/ssl/client-cert.pem',
    # 'ssl_key': '/opt/mysql/ssl/client-key.pem',
}



try:
    with mysql.connector.connect(**config) as connection:
      with connection.cursor() as cursor:        
        insert_query = """
        INSERT INTO person (name, age)
        VALUES ( %s, %s )
        """
        records = []
        with open('names.txt', 'r', encoding='utf-8') as f: 
          data = f.read().split('\n')
          count = 0
          for d in data:
            d_clean = d.strip().replace("'", '')
            if d_clean != '':
              records.append(tuple(d.rsplit(' ', maxsplit=1)))
            # count += 1
            # if count == 20:
            #   break
            

        # cursor.execute("SELECT * FROM person")
        # result = cursor.fetchall()
        cursor.executemany(insert_query, records)
        # print(type(result))
        # for t in result:
        #   print(t)
        connection.commit()

        # insert_reviewers_query = """
        #       INSERT INTO reviewers
        #       (first_name, last_name)
        #       VALUES ( %s, %s )
        #       """
        # reviewers_records = [
        #     ("Chaitanya", "Baweja"),
        #     ("Mary", "Cooper"),
        #     ("John", "Wayne"),
        #     ("Thomas", "Stoneman"),
        #     ("Penny", "Hofstadter"),
        #     ("Mitchell", "Marsh"),
        #     ("Wyatt", "Skaggs"),
        #     ("Andre", "Veiga"),
        #     ("Sheldon", "Cooper"),
        #     ("Kimbra", "Masters"),
        #     ("Kat", "Dennings"),
        #     ("Bruce", "Wayne"),
        #     ("Domingo", "Cortes"),
        #     ("Rajesh", "Koothrappali"),
        #     ("Ben", "Glocker"),
        #     ("Mahinder", "Dhoni"),
        #     ("Akbar", "Khan"),
        #     ("Howard", "Wolowitz"),
        #     ("Pinkie", "Petit"),
        #     ("Gurkaran", "Singh"),
        #     ("Amy", "Farah Fowler"),
        #     ("Marlon", "Crafford"),
        #     ]
        # cursor.executemany(insert_reviewers_query, reviewers_records)

    connection.commit()







except mysql.connector.Error as e:
    print(e)