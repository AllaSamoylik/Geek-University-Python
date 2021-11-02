log_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        log = line.split()
        remote_addr = log[0]
        request_type = log[5].replace('"', '')
        requested_resource = log[6]
        log_result = (remote_addr, request_type, requested_resource)
        log_list.append(log_result)
    print(log_list)
