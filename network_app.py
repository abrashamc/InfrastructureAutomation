import sys

from ip_reach import ip_reach, ip_file_valid, ip_address_valid
from ssh_connection import ssh_connection
from multi_thread import create_threads


def run():
    """
    Run main app
    """
    ip_list = ip_file_valid()

    # Verifying validity of each IP address in the list
    try:
        ip_address_valid(ip_list)
    except KeyboardInterrupt:
        print("Program aborted by user. Exiting...")
        sys.exit()

    # Verifying reachability of each IP address in the list
    try:
        ip_reach(ip_list)
    except KeyboardInterrupt:
        print("Program aborted by user. Exiting...")
        sys.exit()

    create_threads(ip_list, ssh_connection)


if __name__ == "__main__":
    run()
