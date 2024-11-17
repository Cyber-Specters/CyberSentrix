import binascii
from scapy.all import *
from struct import pack

# USB HID key map as a dictionary
keyMap = {
    '04': 'a', '05': 'b', '06': 'c', '07': 'd', '08': 'e', '09': 'f', '0a': 'g', '0b': 'h', '0c': 'i', '0d': 'j',
    '0e': 'k', '0f': 'l', '10': 'm', '11': 'n', '12': 'o', '13': 'p', '14': 'q', '15': 'r', '16': 's', '17': 't',
    '18': 'u', '19': 'v', '1a': 'w', '1b': 'x', '1c': 'y', '1d': 'z', '1e': '1', '1f': '2', '20': '3', '21': '4',
    '22': '5', '23': '6', '24': '7', '25': '8', '26': '9', '27': '0', '28': '\n', '2a': '\x08', '2c': ' ',
    '34': '"', '36': ',', '37': '.', '38': '?', '2d': '_', '2e': '!', '2f': '@', '30': '#', '31': '$', '33': ';',
    '30': '}', '2f': '{'
}

# Function to convert string to HID keymap values
def convert_to_hid_keys(data):
    # Convert each character to corresponding USB HID keycode
    hid_keys = []
    for char in data:
        for keycode, value in keyMap.items():
            if char == value:
                hid_keys.append(keycode)
                break
    return hid_keys

# Function to send HID-mapped data using ICMP
def send_icmp_data(hid_keys, target_ip):
    for key in hid_keys:
        payload = bytes.fromhex(key)
        packet = IP(dst=target_ip) / ICMP(type=8) / Raw(load=payload)
        send(packet)
        time.sleep(0.01)  # Optional: Add delay between packets

# Main logic
def main():
    # Step 1: Read content from story.zlib
    with open("story.zlib", "r") as file:
        data = file.read()

    # Step 2: Convert characters to HID key codes
    hid_keys = convert_to_hid_keys(data)

    # Step 3: Send HID-mapped data via ICMP
    target_ip = "192.168.1.2"  # Replace with the target IP address
    send_icmp_data(hid_keys, target_ip)

if __name__ == "__main__":
    main()
