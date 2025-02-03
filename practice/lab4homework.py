#Natalie Gardner
#11-17-2024





def ip_classify(first_octet):
    """
    Classifies the IP address based on its first octet.
    """
    if 1 <= first_octet <= 127:
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:
        return "Class C", "255.255.255.0"
    elif 224 <= first_octet <= 239:
        return "Class D", "n/a"
    elif 240 <= first_octet <= 255:
        return "Class E", "n/a"
    else:
        return "Invalid", "n/a"


def more():
    """
    Asks the user if they have more addresses to check.
    """
    while True:
        response = input("Do you have more IP addresses to check? (y/n): ").strip().lower()
        if response in ('y', 'n'):
            return response
        print("Invalid input. Please enter 'y' or 'n'.")


def main():
    """
    Main function to allow users to input IP addresses and classify them.
    """
    print("IP Address Classifier")
    while True:
        ip_address = input("Enter an IP address: ").strip()
        try:
            # Split the IP address and extract the first octet
            octets = ip_address.split('.')
            if len(octets) != 4 or not all(octet.isdigit() for octet in octets):
                raise ValueError("Invalid IP address format.")
            
            first_octet = int(octets[0])
            ip_class, subnet_mask = ip_classify(first_octet)

            # Display the results
            print(f"IP Address: {ip_address}")
            print(f"Class: {ip_class}")
            print(f"Default Subnet Mask: {subnet_mask}")
        
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid IP address.")

        # Check if the user wants to continue
        if more() == 'n':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
