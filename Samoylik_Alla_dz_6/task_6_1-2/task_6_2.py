with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    addr_list = [line.split()[0] for line in f]
    remote_addr_count = zip((addr_list.count(i) for i in addr_list), addr_list)
    spammer = max(remote_addr_count)
    print(list(spammer))
