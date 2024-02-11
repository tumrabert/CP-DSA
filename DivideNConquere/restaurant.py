import sys
import heapq
kb = sys.stdin
# Example implementation in Python
def calculate_seating_times(N, A, T, customers):
    available_chefs = []
    chef_last_task = [0] * (N + 1)
    pending_customers = []
    output = []

    for i, chef_id in enumerate(range(1, N + 1)):
        heapq.heappush(available_chefs, (T[i - 1], chef_id))
        chef_last_task[i] = T[i - 1]

    for customer_id, arrival_time in customers:
        heapq.heappush(pending_customers, (arrival_time, customer_id))

    time = 0
    while available_chefs or pending_customers:
        next_available_time = heapq.heappop(available_chefs)[0]
        if time < next_available_time:
            time = next_available_time
        while pending_customers and pending_customers[0][0] <= time:
            customer_id, arrival_time = heapq.heappop(pending_customers)
            seat_time = time
            output.append((customer_id, seat_time))
            # Handle delayed customer case:
            if arrival_time > time:
                chef_id = heapq.heappop(available_chefs)[1]  # Get chef ID without popping time
                # Update chef's last task and re-add to heap
                chef_last_task[chef_id] = arrival_time
                heapq.heappush(available_chefs, (chef_last_task[chef_id], chef_id))
            # Continue processing waiting customers

    return output

# Example usage
N,A = [int(e) for e in kb.readline().split()]
T = [int(e) for e in kb.readline().split()]
customers = [int(e) for e in kb.readline().split()]
waiting_times = calculate_seating_times(N, A, T, customers)

print(waiting_times)