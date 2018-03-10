def main():
    infile = open("./output/stdout.raw", 'r')
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
                sfp.update(fault=line.rstrip())
        elif line.startswith("  Rx Power"):
            line.strip()
            if ' - ' in line or ' -- ' in line or ' + ' in line or ' ++ ' in line:
                if "Rx Power        N/A     --" not in line:
                    sfp.update(fault=line.rstrip())
        else:
            continue
    for key in sfps:
        s = sfps[key]
        if 'fault' in s.keys():
            print (key)
            for item in sfps[key]:
                print '  {0}: {1}'.format(item, sfps[key][item])

#####

main()

