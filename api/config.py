import os

postgresql_config = {
	'host': os.environ.get('POSTGRESQL_HOST', 'localhost'),
	'user': os.environ.get('POSTGRESQL_USER', 'root'),
	'pass': os.environ.get('POSTGRESQL_PASS', ''),
	'db':   os.environ.get('POSTGRESQL_DB', 'my_flask'),
}

def alchemy_uri():
	return f"postgresql://{postgresql_config['user']}:{postgresql_config['pass']}@{postgresql_config['host']}/{postgresql_config['db']}"

test_db = {
'user': 'test',
'password': '1234',
'host': 'localhost',
'port': 3306,
'database': 'test_db'
}

def test_db_uri():
	return "sqlite:///:memory:"