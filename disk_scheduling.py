import random


# Disk specifications
ROTATIONAL_LATENCY = 4.17
TRANSFER_TIME = 0.13
HEAD_START_STOP_TIME = 1.0
CYLINDERS_PER_MS = 4000
MIN_CYLINDER = 1
MAX_CYLINDER = 65535


def get_input():
    """Read the initial head position and I/O requests from the user."""
    head_position = int(input("Enter initial head position: "))
    num_requests = int(input("Enter number of I/O requests: "))

    requests = []

    for _ in range(num_requests):
        cylinder, arrival_time = map(int, input().strip().split())
        requests.append((cylinder, arrival_time))

    # Requests must be processed according to their arrival times
    requests.sort(key=lambda request: request[1])

    return head_position, requests


def generate_random_input(num_requests):
    """Generate random I/O requests for simulation."""
    requests = []

    head_position = random.randint(MIN_CYLINDER, MAX_CYLINDER)
    arrival_time = random.randint(0, 4)

    for _ in range(num_requests):
        cylinder = random.randint(MIN_CYLINDER, MAX_CYLINDER)
        requests.append((cylinder, arrival_time))

        arrival_time += random.randint(2, 12)

    return head_position, requests


def calculate_seek_time(head_position, request_position):
    """Calculate the head movement time between two cylinders."""
    if head_position == request_position:
        return 0

    cylinder_distance = abs(head_position - request_position)

    return (
        cylinder_distance / CYLINDERS_PER_MS
        + HEAD_START_STOP_TIME
    )


def elevator(requests, head_position):
    """
    Simulate the Elevator disk scheduling algorithm.

    The head initially moves toward cylinders with larger numbers.
    When no pending request exists in the current direction,
    the direction is reversed.
    """
    # Work on a copy so the original request list is not modified.
    requests = requests.copy()

    current_time = 0
    direction = 1

    responses = []
    pending_requests = []

    while requests or pending_requests:

        # Add all requests that have already arrived.
        while requests and requests[0][1] <= current_time:
            pending_requests.append(requests.pop(0))

        # If there are no pending requests, move time forward
        # to the arrival time of the next request.
        if not pending_requests:
            if requests:
                current_time = requests[0][1]
                continue

            break

        # Sort requests according to the current head direction.
        pending_requests.sort(
            key=lambda request: request[0],
            reverse=(direction == -1),
        )

        next_request = None

        for index, (cylinder, _) in enumerate(pending_requests):
            moving_up = direction == 1 and cylinder >= head_position
            moving_down = direction == -1 and cylinder <= head_position

            if moving_up or moving_down:
                next_request = pending_requests.pop(index)
                break

        # Reverse direction if no request exists ahead.
        if next_request is None:
            direction *= -1
            continue

        cylinder, _ = next_request

        current_time += (
            calculate_seek_time(head_position, cylinder)
            + ROTATIONAL_LATENCY
            + TRANSFER_TIME
        )

        head_position = cylinder

        responses.append(
            (cylinder, round(current_time, 2))
        )

    return responses


def fcfs(requests, head_position):
    """Simulate the First-Come, First-Served disk scheduling algorithm."""
    responses = []
    current_time = 0

    for cylinder, arrival_time in requests:

        # If the request has not arrived yet, wait until it arrives.
        current_time = max(current_time, arrival_time)

        current_time += (
            calculate_seek_time(head_position, cylinder)
            + ROTATIONAL_LATENCY
            + TRANSFER_TIME
        )

        responses.append(
            (cylinder, round(current_time, 2))
        )

        head_position = cylinder

    return responses


def print_results(algorithm_name, responses):
    """Print simulation results in a readable format."""
    print(f"\n{algorithm_name}")

    for cylinder, response_time in responses:
        print(f"Cylinder {cylinder}: {response_time} ms")


def main():
    print("Disk Scheduling Simulator")
    print("-------------------------")
    print("1. Enter I/O requests manually")
    print("2. Generate random requests")

    choice = int(input("Select an option: "))

    if choice == 1:
        head_position, requests = get_input()

    elif choice == 2:
        num_requests = int(
            input("Enter number of random requests: ")
        )

        head_position, requests = generate_random_input(
            num_requests
        )

    else:
        print("Invalid option.")
        return

    print(f"\nInitial head position: {head_position}")
    print(f"Number of requests: {len(requests)}")

    fcfs_results = fcfs(
        requests,
        head_position,
    )

    elevator_results = elevator(
        requests,
        head_position,
    )

    print_results(
        "FCFS Results:",
        fcfs_results,
    )

    print_results(
        "Elevator Results:",
        elevator_results,
    )


if __name__ == "__main__":
    main()