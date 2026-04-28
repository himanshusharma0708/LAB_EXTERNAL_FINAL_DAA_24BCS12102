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

if __name__ == "__main__":
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        arrival = int(input(f"Enter arrival time for job {i+1}: "))
        deadline = int(input(f"Enter deadline for job {i+1}: "))
        profit = int(input(f"Enter profit for job {i+1}: "))
        jobs.append((arrival, deadline, profit))
    
    total_profit, count = job_scheduling(jobs)
    print(f"Total profit: {total_profit}")
    print(f"Number of jobs scheduled: {count}")
