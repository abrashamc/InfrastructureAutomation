import paramiko
import os.path
import sys
from time import sleep
import re

user_file = "resources/credentials.txt"

if os.path.isfile(user_file):
    print("Credential file is valid")
else:
    print(f'File {user_file} does not exist. Please check and try again')
    sys.exit()

cmd_file = "resources/cmd.txt"

if os.path.isfile(cmd_file):
    print("Cmd file is valid")
else:
    print(f'File {cmd_file} does not exist. Please check and try again')
    sys.exit()


def ssh_connection(ip):
    """
    Open SSHv2 connection to the device
    :param ip: Ip address of device
    """
    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys
        # Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()

        # Setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        sleep(1)

        # Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        sleep(1)

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            print(f'Executing command: {each_line}')
            connection.send(each_line + '\n')
            sleep(2)

        selected_user_file.close()
        selected_cmd_file.close()

        # Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% invalid input", router_output):
            print(f'There was at least one IOS syntax error on device {ip}')
        else:
            print(f'DONE for device {ip}')

        # Test for reading command output
        print(str(router_output) + "\n")

        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password. Please check username/password and try again.")
        print("Closing program...")
