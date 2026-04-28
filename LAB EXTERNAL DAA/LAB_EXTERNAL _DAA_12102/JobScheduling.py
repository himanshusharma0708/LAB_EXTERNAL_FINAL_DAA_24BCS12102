def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(j[1] for j in jobs)
    slots = [-1] * max_deadline
    total_profit = 0
    count = 0
    for arrival, deadline, profit in jobs:
        for i in range(min(deadline-1, max_deadline-1), max(arrival-1, -1), -1):
            if slots[i] == -1:
                slots[i] = profit
                total_profit += profit
                count += 1
                break
    return total_profit, count
