import os

DB_DETAILS = {
    'dev':{
       'SOURCE_DB':{
        'DB_TYPE': 'mysql',
        'DB_HOST': '127.0.0.1',
        'DB_NAME': os.environ.get('SOURCE_DB_NAME'),
        'DB_USER': 'root',
        'DB_PASS': 'password12345'
       },
        'TARGET_DB':
        {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'PostgreSQL 15',
            'DB_USER': 'postgres',
            'DB_PASS': 'Johncena1234$',
        },
    },
}