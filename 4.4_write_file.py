# Import the built-in json module
import json

# Define a dictionary named payload
payload = {
    "hostname": "somehost",
    "username": "someuser",
    "interfaces": [
        {
            "name": "eth0",
            "mac": "00:00:00:00:00:00",
        },
        {
            "name": "eth1",
            "mac": "00:00:00:00:00:01",
        },
    ],
    "version": "1.0.0",
    "description": "This is a test",
    "enabled": True,
    "number": 1,
    "float": 1.0,
}

# Save the payload to a file using json.dump
def save_payload(payload):
    with open("payload.json", "w") as f:
        json.dump(payload, f, indent=4, sort_keys=True)

# Call the save_payload function
save_payload(payload)
print("Saved!")
