import matplotlib.pyplot as plt

num_samples = 10_000_000
process_counts = [1, 2, 4, 8, 16, 32]

# Waktu serial
start = time.time()
serial_pi = calculate_pi_serial(num_samples)
serial_time = time.time() - start

print(f"Waktu Serial: {serial_time:.4f} detik")

parallel_times = []
speedups = []
efficiencies = []

# Testing parallel
for num_procs in process_counts:
    start = time.time()

    pi_est = calculate_pi_parallel(num_samples, num_procs)

    parallel_time = time.time() - start

    speedup = serial_time / parallel_time
    efficiency = speedup / num_procs

    parallel_times.append(parallel_time)
    speedups.append(speedup)
    efficiencies.append(efficiency)

    print(f"\nProses: {num_procs}")
    print(f"Estimasi π : {pi_est}")
    print(f"Waktu      : {parallel_time:.4f} detik")
    print(f"Speedup    : {speedup:.4f}")
    print(f"Efficiency : {efficiency:.4f}")
