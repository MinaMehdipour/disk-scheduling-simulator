# Disk Scheduling Simulator

A Python simulation of two disk scheduling algorithms:

- FCFS (First-Come, First-Served)
- Elevator (SCAN-style scheduling)

This project was originally developed as a university programming assignment for the Database Systems Implementation course.

The simulator processes I/O requests based on their cylinder positions and arrival times and compares the behavior of the two scheduling algorithms.

## Disk Specifications

The simulated disk uses the following parameters:

- Number of cylinders: 65,535
- Rotational latency: 4.17 ms
- Transfer time: 0.13 ms
- Head start/stop overhead: 1 ms
- Head movement time: 1 ms per 4,000 cylinders

The seek time is calculated using:

```text
Seek Time =
|Current Cylinder - Requested Cylinder| / 4000 + 1 ms
```

If the disk head is already positioned on the requested cylinder, the seek time is zero.

## Algorithms

### FCFS

First-Come, First-Served processes I/O requests according to their arrival order.

The disk head moves directly from the current position to the cylinder of the next request.

FCFS is simple to implement, but it can cause unnecessary head movement when consecutive requests are located far from each other.

### Elevator

The Elevator algorithm processes requests according to the current direction of the disk head.

The head initially moves toward cylinders with larger numbers. Requests located in the current direction are processed first.

When no request remains in the current direction, the head reverses its direction.

This approach can reduce unnecessary disk-head movement compared with FCFS.

## Input Format

The program supports both manual and randomly generated input.

For manual input:

```text
initial_head_position
number_of_requests
cylinder arrival_time
cylinder arrival_time
...
```

Example:

```text
8000
6
8000 0
24000 0
56000 0
16000 10
64000 20
40000 30
```

The first line contains the initial disk-head position.

The second line contains the number of I/O requests.

Each following line contains:

```text
cylinder arrival_time
```

## Running the Program

Make sure Python 3 is installed.

Run:

```bash
python disk_scheduling.py
```

The program displays two options:

```text
1. Enter I/O requests manually
2. Generate random requests
```

### Manual Mode

Choose option `1` and enter the initial head position and requests.

### Random Mode

Choose option `2` and specify the number of random requests to generate.

For example:

```text
1000
```

The simulator will generate random cylinder positions and request arrival times.

## Example Output

Example FCFS output:

```text
FCFS Results:

Cylinder 8000: 4.3 ms
Cylinder 24000: 13.6 ms
Cylinder 56000: 26.9 ms
Cylinder 16000: 42.2 ms
Cylinder 64000: 59.5 ms
Cylinder 40000: 70.8 ms
```

Example Elevator service order:

```text
Elevator Results:

Cylinder 8000: 4.3 ms
Cylinder 24000: 13.6 ms
Cylinder 56000: 26.9 ms
Cylinder 64000: 34.2 ms
Cylinder 40000: 45.5 ms
Cylinder 16000: 56.8 ms
```

## Experimental Evaluation

The simulator was also tested using randomly generated workloads with different numbers of I/O requests.

The experiments included workloads such as:

- 10 requests
- 100 requests
- 1000 requests

Each configuration was executed multiple times and the results of FCFS and Elevator scheduling were compared.

The complete experimental results are available in:

```text
results/disk_scheduling_results.xlsx
```

The experiments show that for the tested random workloads, the Elevator algorithm generally reduces unnecessary disk-head movement and achieves lower completion times than FCFS as the number of requests increases.

## Project Structure

```text
disk-scheduling-simulator/
│
├── disk_scheduling.py
├── README.md
├── sample_input.txt
├── results/
    └── disk_scheduling_results.xlsx
```

## Technologies

- Python 3
- Python standard library
- Microsoft Excel for experimental result analysis

## Purpose

This project demonstrates:

- Disk scheduling concepts
- FCFS scheduling
- Elevator / SCAN-style scheduling
- I/O request arrival-time handling
- Random workload generation
- Performance comparison of scheduling algorithms

## License

This project is intended for educational purposes.