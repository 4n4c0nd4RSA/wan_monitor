import subprocess
import re
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ip_count = 5
graph_range = 10
interval = 1000

def traceroute_to(destination):
    try:
        # Run the traceroute command
        print(f"Tracing {destination} to ping.")
        result = subprocess.run(['tracert', destination], capture_output=True, text=True, check=True)
        
        # Extract IP addresses from the output
        ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
        ips = ip_pattern.findall(result.stdout)
        
        # Get the 2nd, 3rd, and 4th IP addresses if they exist
        if len(ips) >= ip_count:
            return ips[1:ip_count+1]
        else:
            print("Not enough IP addresses found in the traceroute output.")
            return ips
    
    except subprocess.CalledProcessError as e:
        print(f"Traceroute failed: {e}")
        return []

def ping(ip):
    try:
        # Run the ping command
        result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True)
        
        # Extract the time from the output
        time_pattern = re.compile(r'time[=<](\d+)ms')
        match = time_pattern.search(result.stdout)
        if match:
            return int(match.group(1))
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Ping to {ip} failed: {e}")
        return None

def update(frame):
    global ping_data, jitter_data, prev_ping_times
    times = []
    for ip in ips:
        rtt = ping(ip)
        times.append(rtt if rtt is not None else 999)
    
    for i, line in enumerate(lines):
        ping_data[i].append(times[i])
        if len(ping_data[i]) > 1:
            jitter = abs(ping_data[i][-1] - ping_data[i][-2])
            jitter_data[i].append(jitter)
        else:
            jitter_data[i].append(0)
        
        if len(jitter_data[i]) > graph_range:
            jitter_data[i].pop(0)
        
        line.set_data(range(len(jitter_data[i])), jitter_data[i])
    
    ax.set_xlim(0, graph_range)
    ax.relim()
    ax.autoscale_view()
    return lines

if __name__ == "__main__":
    try:
        destination = sys.argv[1]
    except:
        destination = "8.8.8.8"
    ips = traceroute_to(destination)
    
    if not ips:
        print("No IP addresses to ping.")
        exit()
    
    ping_data = [[] for _ in range(len(ips))]
    jitter_data = [[] for _ in range(len(ips))]
    prev_ping_times = [None] * len(ips)
    
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    lines = [ax.plot([], [], label=f"Jitter to {ip}")[0] for ip in ips]
    
    ax.set_xlim(0, graph_range)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Time')
    ax.set_ylabel('Jitter (ms)')
    ax.legend()
    
    ani = FuncAnimation(fig, update, frames=range(100), interval=interval, blit=True)
    
    plt.show()
