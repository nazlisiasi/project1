import yaml
input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))
print input_dict['tests']
for test_entry in input_dict['tests']:
    #print "ENTRY:", test_entry
    print "SOURCE:", test_entry['vm_src']
    src = test_entry['vm_src']
    print "SOURCE IP:", input_dict['vm_details'][src]['mgmt_ip']
    print "DESTINATION:", test_entry['vm_dst']
    dest = test_entry['vm_dst']
    
    print "DESTINATION IP:", input_dict['vm_details'][dest]['mgmt_ip']



    #print input_dict['vm_details'][src]
    #for detail in input_dict['vm_details']:
    #    if test_entry['vm_src'] == detail:
    #        #print detail['mgmt_ip']
