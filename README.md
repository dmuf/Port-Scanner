

# Port Scanner

A simple **Python-based Port Scanner** designed to scan a given IP address or domain to identify open ports and their respective services. This tool is efficient, easy to use, and leverages threading for faster scanning.

## Features
- Scan a single port or a range of ports.
- Identify open ports and display the services running on them.
- Simple command-line interface.
- Uses Python’s standard libraries for networking and threading.

## Technologies Used
- **Python** (Libraries: `socket`, `ipaddress`, `threading`).
- **Git & GitHub** for version control.

## Installation

To get started with the project, follow these steps:

### Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/Port-Scanner.git
```

### Navigate to the Project Directory
Change into the project folder:

```bash
cd Port-Scanner
```

### Run the Port Scanner
Run the Python script using the following command:

```bash
python portscanner.py
```

> **Note:** Make sure Python is installed on your system.

## Usage

Once the script is running, provide the IP address or domain you want to scan:

```bash
python portscanner.py <IP_ADDRESS_OR_DOMAIN>
```

For example, to scan a local network device:

```bash
python portscanner.py 192.168.1.1
```

The script will display a list of open ports and services, like this:

```bash
Scanning target: 192.168.1.1
Open ports:
- 22: SSH
- 80: HTTP
- 443: HTTPS
```

## Example Output

### Basic Example
```bash
Scanning target: 192.168.1.1
Open ports:
- 22: SSH
- 80: HTTP
- 443: HTTPS
```

### Handling a Range of Ports
You can also scan a range of ports by adjusting the script to take input for port ranges. The output will list all the open ports within the specified range.

## Contributing

Contributions are welcome! Feel free to fork the repository and create pull requests with improvements or fixes. Please ensure your changes are well-tested before submitting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Screenshots📷
![Port Scanner](https://github.com/user-attachments/assets/f2f41fe0-b072-418f-bc12-d12ab5c05025)
![Port Scanner 2](https://github.com/user-attachments/assets/0bd41017-a631-4da6-af11-df4fe28ef55b)



---
