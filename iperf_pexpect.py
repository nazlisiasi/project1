import yaml
input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))


print input_dict['tests']
for test_entry in input_dict['tests']:

    print "test_type:", test_entry['test_type']
    src_vm = test_entry['vm_src']
    des_vm = test_entry['vm_dst']

    src_ip = input_dict['vm_details'][src_vm]['mgmt_ip']
    des_ip = input_dict['vm_details'][des_vm]['mgmt_ip']

    src_key = input_dict['vm_details'][src_vm]['key']

    print "pssh -H " +  src_ip  + " -x \"-oStrictHostKeyChecking=no\" + "-i" +  src_key  +\"-P 'ping -c 3 " + des_ip + "'"
