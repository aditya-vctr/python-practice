# Server Network Analysis 
'''
You are given a dictionary data where the keys are server names and the values are dictionaries containing "uptime", "cpu", and "active_users".

Write a function network_analysis(data, task) that returns a set of server names based on the given task.

Tasks
"high_cpu": servers where CPU usage >= 80
"stable_servers": servers where uptime >= 99
"busy_servers": servers where active users >= 1000
"idle_servers": servers where active users < 100

# Examples:
data = {
    "server1": {"uptime": 99.9, "cpu": 85, "active_users": 1200},
    "server2": {"uptime": 97.5, "cpu": 45, "active_users": 80},
    "server3": {"uptime": 99.2, "cpu": 70, "active_users": 600}
}

'''
data = {
    "server1": {"uptime": 99.9, "cpu": 85, "active_users": 1200},
    "server2": {"uptime": 97.5, "cpu": 45, "active_users": 80},
    "server3": {"uptime": 99.2, "cpu": 70, "active_users": 600}
}

def network_analysis(data, task):
    result = set()

    for server, details in data.items():
        if task == "high_cpu":
            if details["cpu"] >= 80:
                result.add(server)

        elif task == "stable_servers":
            if details['uptime'] >= 99:
                result.add(server)

        elif task == "busy_servers":
            if details["active_users"] >= 1000:
                result.add(server)

        elif task == "idle_servers":
                    if details["active_users"] < 100:
                        result.add(server)

    return result

# Testing

print(network_analysis(data, "high_cpu"))
print(network_analysis(data, "stable_servers"))
print(network_analysis(data, "busy_servers"))
print(network_analysis(data, "idle_servers"))

# Output
'''
{"server1"}
{"server1", "server3"}
{"server1"}
{"server2"}
'''

