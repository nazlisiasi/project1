import yaml



 

input_file = 'vm_info.yaml'
input_dict = yaml.load(open(input_file))
#print input_dict[0]['vm_details']['mgmt_ip']
print input_dict.keys()
print input_dict['vm_details'][0]['mgmt_ip']
print input_dict['vm_details'][1]['mgmt_ip']
print input_dict['vm_details'][2]['mgmt_ip']
print input_dict['vm_details'][3]['mgmt_ip']
