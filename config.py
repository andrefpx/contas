USERNAME='root'
PASSWORD = ''
SERVER= 'localhost'
DB = 'gerenciamento_contas'

SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLACHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='chave_secreta1'