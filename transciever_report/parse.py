#! /usr/bin/python

import sys

def main(input_filename,output_filename):
    infile = open(input_filename, 'r')
    rows =  infile.readlines()
    sfps = {}
    sfp = {}
    for line in rows:
        if line.startswith("Ethernet"):
            if any(sfp):
                sfps[current_interface] = sfp
                sfp={}
            current_interface = line.rstrip()
        elif line == "    transceiver is not applicable":
            continue
        elif line.startswith("    type is "):
            sfp.update(interface=current_interface)
            line.strip()
            sfp.update(type=line.split()[2])
        elif line.startswith("    name is "):
            line.strip()
            sfp.update(name=line.split()[2])
        elif line.startswith("    part number is "):
            line.strip()
            sfp.update(part_number=line.split()[3])
        elif line.startswith("    serial number is "):
            line.strip()
            sfp.update(serial_number=line.split()[3])
        elif line.startswith("  Temperature"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                sfp.update(fault=line.rstrip())
        elif line.startswith("  Voltage"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                sfp.update(fault=line.rstrip())
        elif line.startswith("  Current"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                sfp.update(fault=line.rstrip())
        elif line.startswith("  Tx Power"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                # should filter out "Tx Power        N/A     --" to eliminate false-positive
                sfp.update(fault=line.rstrip())
        elif line.startswith("  Rx Power"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                if "Rx Power        N/A     --" not in line:
                    sfp.update(fault=line.rstrip())
        else:
            continue
    outfile = open(output_filename,'w');
    outfile.write('###############################\n')
    outfile.write('# ' + input_filename + '\n')
    outfile.write('###############################\n')
    for key in sorted(sfps):
        interface = sfps[key]
        if 'fault' in interface.keys():
            outfile.write(key + '\n')
            outfile.write('  type:          ' + sfps[key]['type'] + '\n')
            outfile.write('  name:          ' + sfps[key]['name'] + '\n')
            outfile.write('  part_number:   ' + sfps[key]['part_number'] + '\n')
            outfile.write('  serial_number: ' + sfps[key]['serial_number'] + '\n')
            outfile.write('  fault:         ' + sfps[key]['fault'] + '\n')
    outfile.close()

#####

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])