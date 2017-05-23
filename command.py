import json
import telnetlib

telnet_connection = telnetlib.Telnet('0.0.0.0', 55555)

def send_command(command_string):
    telnet_connection.write(command_string + '\n')    
    returned_data = telnet_connection.read_all()    
    return json.loads(returned_data)    
