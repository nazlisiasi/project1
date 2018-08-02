import pexpect
import yaml


input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))

print input_dict, len(input_dict['vm_details'])
prompt = '\$'
i = 0
while i < len(input_dict['vm_details']):
   print "login ids", input_dict['vm_details'][i]['mgmt_ip']
   print "PROMPT IS", prompt
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