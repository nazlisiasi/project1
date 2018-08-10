import pexpect
import yaml
import pssh
import subprocess



input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))

cmd_server = "pssh -H 109.0.4.176 -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -s -p 1114 -D ' "
cmd_client = "pssh -H 109.0.4.198 -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -c 109.0.4.176 -p 1114 -P 2 -t 2 '"

cmd_server2 = "pssh -H 109.0.4.176 -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -s -p 1114 -D ' "
cmd_client2 = "pssh -H 109.0.4.198 -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -c 109.0.4.176 -p 1114 -P 2 -t 10 -u '"

#cmd = "pssh -H 109.0.4.37 -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'ping -c 3 109.0.4.70 '"


print input_dict['tests']

for test_entry in input_dict['tests']:

    print "test_type:", test_entry['test_type']
    src_vm = test_entry['vm_src']
    des_vm = test_entry['vm_dst']
    
    src_ip = input_dict['vm_details'][src_vm]['mgmt_ip']
    des_ip = input_dict['vm_details'][des_vm]['mgmt_ip']

    src_key = input_dict['vm_details'][src_vm]['key']

    print "source key:" ,  input_dict['vm_details'][src_vm]['key']


   #print "SOURCE:", test_entry['vm_src']
    #src = test_entry['vm_src']
   #print "SOURCE IP:", input_dict['vm_details'][src]['mgmt_ip']


   #print "DESTINATION:", test_entry['vm_dst']
    #dest = test_entry['vm_dst']    
   #print "DESTINATION IP:", input_dict['vm_details'][dest]['mgmt_ip']


    if test_entry['test_type'] == 'ping':
        print "It is a PING test" + "->SOURCE:" + src_ip + ";DESTINATION:" + des_ip
        cmd = "pssh -H " +  src_ip  + " -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'ping -c 3 " + des_ip + "'"
        a = subprocess.check_output(cmd, shell=True)
        print a

    if test_entry['test_type'] == 'tcp':
        print "It is a TCP test" + "->SOURCE:" + src_ip + ";DESTINATION:" + des_ip
        cmd_server = "pssh -H " + src_ip + " -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -s -p 1114 -D ' "
        cmd_client = "pssh -H " + des_ip + " -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -c " + src_ip + " -p 1114 -P 2 -t 2 '"
        a = subprocess.check_output(cmd_server, shell=True)
        print a
        b = subprocess.check_output(cmd_client, shell=True)
        print b

    if test_entry['test_type'] == 'udp':
        print "It is a UDP test" + "->SOURCE:" + src_ip + ";DESTINATION:" + des_ip
        cmd_server2 = "pssh -H " + src_ip + " -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -s -p 1114 -D ' "
        cmd_client2 = "pssh -H " + des_ip + " -x \"-oStrictHostKeyChecking=no  -i key.pem\" -P 'iperf3 -c " + src_ip + " -p 1114 -P 2 -t 10 -u '"
        a = subprocess.check_output(cmd_server2, shell=True)
        print a
        b = subprocess.check_output(cmd_client2, shell=True)
        print b







