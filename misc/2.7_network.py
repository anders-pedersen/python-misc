"""
An example of using the learned datatypes, flow control and input function
to create a network config generator for an access switch
The script below is not neccessarily the most efficient way to achieve
the desired outcome, but it intends to showcase and build on some of the skills
that we have learned so far.
"""

# Create a tuple containing 3 items
config_lines = (
    "switchport mode access",
    "switcport access vlan {}",
    "shutdown\n no shutdown",
)

# ask the for the user input
number_of_interfaces = input("how many access interfaces? ")
vlan_id = input("access vlan id? ")

# typecasting the answer to an integer to be able to use it for arithmetics
# we add one to the number because of the way the range function works.
index = int(number_of_interfaces) + 1

# use the range command to generate a list of interfaces.
interfaces = [f"Gi1/0/{i}" for i in range(1, index)]
# print(interfaces)

# iterate over the generated interfaces
for interface in interfaces:
    # use unpacking to clearly name each line of configuration
    mode_access, access_vlan, shut_no_shut = config_lines
    # prints the configuration to the prompt
    print(f"interface {interface}")
    print(f" {mode_access}")
    print(f" {access_vlan.format(vlan_id)}")
    print(f" {shut_no_shut}")
    print("!")
