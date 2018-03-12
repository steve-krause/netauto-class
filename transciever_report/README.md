<b>Overview</b>

./transcievers.yml is an Ansible playbook that will log into all the hosts listed in the hosts file and run the command "show interface transciever details" and copies the stdout to ./output/raw/\<hostname>.

For each host it then calls the parse.py <infile> <outfile> script which goes through the raw output and keys off of any warnings or alarm conditions for any of the SFPs. If it finds a warning or a fault it will save the interface name and SFP details to ./output/parsed/\<hostname>.

Finally, the assemble module is called to assemble all of the ./output/parsed/ files into a single ./output/transciever-alarms.report


<b>Caveats</b>

* This version of parse.py will find some false-positives. I left them in to make the example report more interesting.

* This playbook has only been tested with nxos