import pexpect
import yaml
import addr







#input_file = 'vm_info.yaml'
#input_dict = yaml.load(open(input_file))
#print 'ssh -i vpc-3905545e\:.pem ec2-user@' + input_dict['vm_details'][0]['mgmt_ip']
#ip_list = []


csv_file = "/home/ec2-user/file.txt"
req_num = 0
with open(csv_file, 'r') as f:
#    next(f)
    content = f.read()
ip_list = content.splitlines()
print "IPLIST", ip_list
for line in ip_list:
    if line != '':


        print "LINE IS", line
        req_num += 1
        if line == 'ec2-user@52.52.24.93':
          # prompt = '\[ec2\-user\@ip\-108\-0\-4\-184 \~\]\$'
            prompt = '\$'
        elif line == 'ec2-user@54.183.39.174':
          # prompt = '\[ec2\-user\@ip\-108\-0\-4\-58 \~\]\$'
            prompt = '\$'
        elif line == 'ec2-user@54.241.55.122':
          # prompt = '\[ec2\-user\@ip\-108\-0\-4\-202 \~\]\$'
            prompt = '\$'
        elif line == 'ec2-user@54.183.115.182':
          # prompt = '\[ec2\-user\@ip\-108\-0\-4\-29 \~\]\$'
            prompt = '\$'
        print "PROMPT IS", prompt
        child = pexpect.spawn('ssh -i vpc-3905545e\:.pem ' + line)
        child.expect (prompt)
        print child.before
        child.sendline ('ping -c 3 ' + addr.ips[0] + '>> pingresults.txt')
        child.expect (prompt)
        print child.before
        child.sendline ('ping -c 3 ' + addr.ips[1] + '>> pingresults.txt')
        child.expect (prompt)
        print child.before
        child.sendline('ping -c 3 ' + addr.ips[2] + '>> pingresults.txt')
        child.expect (prompt)
        print child.before
        child.sendline('ping -c 3 ' + addr.ips[3] + '>> pingresults.txt')
        child.expect (prompt)
        print child.before, child.after
        child.close()
        print "req", req_num, "is done"
print "ALL REQUESTS ARE DONE!"
print "PINGING ALL INTSNACES IS DONE"
