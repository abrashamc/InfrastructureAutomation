import threading


def create_threads(ip_list, function):
    """
    Create threads
    :param ip_list: Ip address of device
    :param function: target function to execute
    :return:
    """
    threads = []

    for ip in ip_list:
        new_thread = threading.Thread(target=function, args=(ip,))
        new_thread.start()
        threads.append(new_thread)

    for current_thread in threads:
        current_thread.join()