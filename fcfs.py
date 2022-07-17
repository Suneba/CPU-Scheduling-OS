# Python3 program for implementation
# of FCFS scheduling

# Function to find the waiting
# time for all processes
def findWaitingTime(n,bt, wt):
    # waiting time for
    # first process is 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


# Function to calculate turn
# around time
def findTurnAroundTime(n, bt, wt, tat):
    # calculating turnaround
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# Function to calculate
# average time
def findavgTime( n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    # Function to find waiting
    # time of all processes
    findWaitingTime( n, bt, wt)

    # Function to find turn around
    # time for all processes
    findTurnAroundTime( n,
                       bt, wt, tat)

    # Display processes along
    # with all details
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    # Calculate total waiting time
    # and total turn around time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        table = "Processes Burst time " +" Waiting time " +" Turn around time"+"\n " + str(i + 1) + "\t    \t" +str(bt[i]) + "\t    " +str(wt[i]) + "\t   \t " +str(tat[i])

        print(" " + str(i + 1) + "\t     \t   " +
              str(bt[i]) + "\t       " +
              str(wt[i]) + "\t  \t " +
              str(tat[i]))

    avg_wt = str(total_wt / n)


    avg_tat = str(total_tat / n)


    return( wt,tat,avg_wt,avg_tat)


def run_file(num_process,burst_time):
    # process id's
    # processes = [1, 2, 3]
    n = num_process

    # Burst time of all processes
    # burst_time = [10, 5, 8]
    a,b,c,d =findavgTime(n, burst_time)

    return (a,b,c,d)



# Driver code
if __name__ == "__main__":
    # # process id's
    # processes = [1, 2, 3]
    # n = len(processes)
    #
    # # Burst time of all processes
    # burst_time = [10, 5, 8]
    #
    # findavgTime(processes, n, burst_time)
    run_file(4,[10, 5, 8,1])

