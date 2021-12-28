import subprocess
import sys
from sys import platform
import os.path


def ip_file_valid() -> [int]:
    """
    Checking IP address file and content validity
    :return: array of IP values in int
    """
    ip_file = "resources/ip.txt"

    if os.path.isfile(ip_file):
        print("IP file is valid")
    else:
        print(f"File {ip_file} does not exist!")
        sys.exit()

    selected_ip_file = open(ip_file, 'r')

    selected_ip_file.seek(0)

    ip_list = selected_ip_file.readlines()

    selected_ip_file.close()

    return ip_list


def ip_address_valid(ip_list):
    """
    Check octets

    :param ip_list: list of ip addresses
    """
    for ip in ip_list:
        ip = ip.rstrip("n")
        octet_list = ip.split('.')

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (
                int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (
                0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print(f'There was an invalid IP address in the file: {ip}')
            sys.exit()


def ip_reach(ip_list):
    """
    Check IP reachability
    :param ip_list: list of ip addresses
    """
    for ip in ip_list:
        ip = ip.rstrip("\n")

        if platform == "linux" or platform == "darwin":
            ping_response = subprocess.call(f'ping {ip} -c 2',
                                            stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL,
                                            shell=True)
        elif platform == "win32":
            ping_response = subprocess.call(f'ping {ip} -n 2', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            raise Exception("Unsupported OS!")

        if ping_response == 0:
            print(f'{ip} is reachable')
            continue
        else:
            print(f'{ip} not reachable. Check connectivity and try again.')
            sys.exit()
