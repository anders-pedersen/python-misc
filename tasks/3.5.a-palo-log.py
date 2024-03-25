s_log_path = '.'

# Open Palo syslog-file for reading
o_file = open(s_log_path + '/' + 'palo.log', 'r')

# Read contents of file into variable
s_syslog = o_file.read()

# Split contents on line-break - produce list of lines
l_syslog = s_syslog.split('\n')

# Close file
o_file.close()


# Iterate over syslog list of lines
for s_line in l_syslog:

    # Split line into columns
    l_columns = s_line.split(',')

    # Will extract lines with TRAFFIC keyword and print whole line
    if 'TRAFFIC' in l_columns:
        print(s_line)







