import os,sys,os.path,threading,codecs
if not os.path.exists('Results'):
    os.makedirs('Results')
def save_domain(name,data_save):
    with open(f'Results\\{name}.txt','a',encoding='utf-8') as save:
        save.write(data_save+'\n')
# check domain die
def check_domain_die_cmd(data_domain):
    global checked,die,live,retry
    if '@' in data_domain.strip():
        DomainFirst = data_domain.split('@')[1]
        if ':' in DomainFirst:
            domainName = DomainFirst.split(':')[0]
        elif '|' in DomainFirst:
            domainName = DomainFirst.split('|')[0]
        else:
            domainName = DomainFirst
    else:
        domainName = data_domain
        cmd_sys = f'ping {domainName}'
        print(cmd_sys)
    try:
        check_domain_die = os.system(cmd_sys)
        if check_domain_die == 1:
            save_domain('Die',data_domain)
            print(f'Domain Die: {data_domain}')
        else:
            print(f'Domain Live: {data_domain}')
            save_domain('Live',data_domain)
    except:
        pass
        # threading.Thread(target=check_domain_die_cmd,args=(data_domain)).start()
    if checked == len(data_check):
        input('Check Done ! - hungsaki2003@gmail.com')
        sys.exit()
    os.system('title Check Domain Die No Proxy - {}/{} - Die: {} - Live: {} - Retry: {} - hungsaki2003@gmail.com'.format(checked,len(data_check),die,live,retry))

with codecs.open('data.txt','r',encoding='unicode_escape') as read_file_data:
    data_check = read_file_data.readlines()

# def runTools(thread_step):
#     for i in range(thread_step,len(data_check),2):
#         data_domain = data_check[i].strip()
#         check_domain_die_cmd(data_domain)
checked = die = live = retry = 0
os.system('title Check Domain Die No Proxy - {}/{} - Die: {} - Live: {} - Retry: {} - hungsaki2003@gmail.com'.format(checked,len(data_check),die,live,retry))
input('Enter to run - hungsaki2003@gmail.com')
# for x in range(2):
#     threading.Thread(target=runTools,args=(x,)).start()
for x in data_check:
    data_domain = x.strip()
    check_domain_die_cmd(data_domain)
