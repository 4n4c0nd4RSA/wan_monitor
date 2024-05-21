# Network Jitter Monitor

This project monitors the network jitter to a set of IP addresses obtained via traceroute. The jitter is calculated as the absolute difference between successive ping response times. The results are visualized using a real-time graph.

## Features

- Traceroute to a specified destination to obtain IP addresses.
- Ping the obtained IP addresses and calculate jitter.
- Real-time graph visualization of jitter.

## Requirements

- Python 3.6+
- `matplotlib` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/4n4c0nd4RSA/wan_monitor.git
    cd wan_monitor
    ```

2. Install the required Python packages:
    ```sh
    pip install matplotlib
    ```

## Usage

1. Run the script with the desired destination (default is `8.8.8.8`):
    ```sh
    python network_jitter_monitor.py [destination]
    ```

    Example:
    ```sh
    python network_jitter_monitor.py google.com
    ```

2. The script will perform a traceroute to the specified destination, obtain the IP addresses, and start pinging them.

3. A real-time graph will be displayed showing the jitter for each IP address.

## Script Explanation

- **Imports**: The script imports necessary libraries such as `subprocess`, `re`, `sys`, and `matplotlib`.

- **Parameters**:
    - `ip_count`: Number of IP addresses to extract from traceroute output.
    - `graph_range`: Range of the x-axis in the graph.
    - `interval`: Interval between updates in milliseconds.

- **Functions**:
    - `traceroute_to(destination)`: Performs a traceroute to the specified destination and extracts IP addresses.
    - `ping(ip)`: Pings the specified IP address and returns the response time.
    - `update(frame)`: Updates the graph with the latest jitter values.

- **Main Script**:
    - Obtains the destination from command-line arguments.
    - Performs traceroute and obtains IP addresses.
    - Initializes data structures for storing ping times and jitter values.
    - Sets up the real-time graph using `matplotlib`.
    - Starts the animation for real-time graph updates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
