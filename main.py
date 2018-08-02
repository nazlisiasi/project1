import pexpect
import yaml


input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))

#print input_dict, len(input_dict['vm_details'])
prompt = '\$'
i = 0
while i < len(input_dict['vm_details']):
   print "login ids", input_dict['vm_details'][i]['mgmt_ip']
#       print "PROMPT IS", prompt
   print "SSH TO ", input_dict['vm_details'][i]['mgmt_ip']
   child = pexpect.spawn('ssh -i vpc-f61a4291:.pem ' + input_dict['vm_details'][i]['mgmt_ip'])
   child.expect (prompt)
   child.logfile = open("/home/ec2-user/results.txt", "w")
   print child.before

   j = 0
   while  j < len(input_dict['vm_details'][i]['ping_ips']):
      print "ping to ", input_dict['vm_details'][i]['ping_ips'][j]
      child.sendline ('ping -c 3 ' + input_dict['vm_details'][i]['ping_ips'][j])
      child.expect (prompt)
      print child.before, child.after
      print "req is done"

      j += 1
   child.close()
   i += 1

print "ALL REQUESTS ARE DONE!"
print "PINGING ALL INTSNACES IS DONE"
'''
prompt = '\$'
print "PROMPT IS", prompt
child = pexpect.spawn('ssh -i vpc-f61a4291:.pem ' + 'ec2-user@109.0.4.176')
child.expect (prompt)
child.sendline ('ping -c 3 ' + '109.0.4.70')
child.expect (prompt)
print child.before, child.after
child.close()
'''
'''
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
            prompt = '\$'
        elif line == 'ec2-user@54.183.39.174':
            prompt = '\$'
        elif line == 'ec2-user@54.241.55.122':
            prompt = '\$'
        elif line == 'ec2-user@54.183.115.182':
            prompt = '\$'

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
'''
