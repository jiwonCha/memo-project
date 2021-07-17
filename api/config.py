import os

postgresql_config = {
	'host': os.environ.get('POSTGRESQL_HOST', 'localhost'),
	'user': os.environ.get('POSTGRESQL_USER', 'root'),
	'pass': os.environ.get('POSTGRESQL_PASS', ''),
	'db':   os.environ.get('POSTGRESQL_DB', 'my_flask'),
}

def alchemy_uri():
	return f"postgresql://{postgresql_config['user']}:{postgresql_config['pass']}@{postgresql_config['host']}/{postgresql_config['db']}"


def test_db_uri():
	return "sqlite:///:memory:"