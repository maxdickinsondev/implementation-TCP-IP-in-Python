from sys import argv
from serverUtils import HandleConnection

try:
	porta = int (argv[1])
	diretorio = argv[2]
except:
	print('d Parameter(s): <PORT> <FILE-DIR>'.format(argv[0]))
	exit(-1)

if(porta < 0 or porta > 65535):
	print('d Porta inválida')
	exit(-1)

clients = []

connection = HandleConnection(porta, diretorio, clients)
print('d Starting HandleConnection...')
print('d Use Ctrl+C to stop server.')
connection.start()