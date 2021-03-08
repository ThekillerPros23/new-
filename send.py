from pysftp import sftp

host     = '40.87.90.40'
username = 'new'
password = ' password'

try:
	ftp =  sftp.Connection(host, username, password)
	print("conexion establecida.......")

except Exception as e:
	print('conexion cerrada',* str(e))