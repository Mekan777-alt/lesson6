request_list = []
remote_dict = {}
spam_addr = ''
spam_req_score = 0


with open('ngnix_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line.split()[0]
        request_type = line.split('"')[1].split()[0]
        requested_resource = line.split('"')[1].split()[1]
        request_list.append((remote_addr, request_type, requested_resource))
        print(request_list[-1])
        remote_dict[remote_addr] = remote_dict.setdefault(remote_addr, 0) + 1
        if remote_dict[remote_addr] > spam_req_score:
            spam_addr = remote_addr
            spam_req_score = remote_dict[remote_addr]

    print(f'С IP {spam_addr} было совершено запросов: {spam_req_score}!')




