import pexpect
import yaml
import pssh
import subprocess
input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))

import subprocess

cmd = 'pssh  -i -H ' + input_dict['vm_details'][1]['user'] + '@' + input_dict['vm_details'][1]['mgmt_ip'] + ' -x \"-oStrictHostKeyChecking=no  -i ' + input_dict['vm_details'][1]['key'] + '\"'  + ' \'ping -c 3 ' + input_dict['vm_details'][0]['mgmt_ip'] + "\'"
cmd1 = 'pssh  -i -H ' + input_dict['vm_details'][2]['user'] + '@' + input_dict['vm_details'][2]['mgmt_ip'] + ' -x \"-oStrictHostKeyChecking=no  -i ' + input_dict['vm_details'][2]['key'] + '\"'  + ' \'ping -c 3 ' + input_dict['vm_details'][1]['mgmt_ip'] + "\'"
cmd2 = 'pssh  -i -H ' + input_dict['vm_details'][3]['user'] + '@' + input_dict['vm_details'][3]['mgmt_ip'] + ' -x \"-oStrictHostKeyChecking=no  -i ' + input_dict['vm_details'][3]['key'] + '\"'  + ' \'ping -c 3 ' + input_dict['vm_details'][2]['mgmt_ip'] + "\'"

if input_dict['tests'][0]['test_type'] == 'tcp':
    print "It is a TCP test"
    a = subprocess.check_output(cmd,shell=True)
    print a

if input_dict['tests'][1]['test_type'] == 'udp':
    print "It is a UDP test"
    a = subprocess.check_output(cmd1,shell=True)
    print a

if input_dict['tests'][2]['test_type'] == 'ping':
    print "It is a PING test"
    a = subprocess.check_output(cmd2,shell=True)
    print a
