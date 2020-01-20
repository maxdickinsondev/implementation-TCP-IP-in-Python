from sys import argv
from clientUtils import ConnectionToServer


try:
    server_ip= argv[1]
    port     = int( argv[2] )
    filename = argv[3]
except:
    print('d Parameter(s): <HOSTNAME-OR-IP> <PORT> <FILENAME>'.format( argv[0] ))
    exit(-1)

if(port < 0 or port > 65535):
    print('d Porta inválida')
    exit(-1)

try:
    print('d Starting ConnectionToServer...')
    print('d Use Ctrl+C to stop all process.')
    connection = ConnectionToServer( (server_ip, port), filename )
    connection.connect_to_server()
    connection.send_file()
    connection.close()
except KeyboardInterrupt as ki:
    print('\nd Used Ctrl+C.')
    print('d Stopping all process.')
    connection.close()