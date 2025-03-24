def fcfs(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    current_time = 0
    for p in processes:
        p['completion_time'] = current_time + p['burst_time']
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']
        current_time = p['completion_time']
    return processes

# Similar functions for SJF, Round Robin, Priority Scheduling
