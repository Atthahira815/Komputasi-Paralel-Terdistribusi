import matplotlib.pyplot as plt

# =========================================
# Grafik 1 - Speedup vs Jumlah Process
# =========================================

plt.figure(figsize=(10,6))

plt.plot(process_counts, speedups, 'bo-', label='Speedup Aktual')
plt.plot(process_counts, process_counts, 'r--', label='Speedup Ideal')

plt.xlabel('Jumlah Process')
plt.ylabel('Speedup')
plt.title('Speedup vs Jumlah Process')

plt.legend()
plt.grid(True)

plt.show()

# =========================================
# Grafik 2 - Waktu Eksekusi vs Ukuran Sampel
# =========================================

sample_sizes = [100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]

execution_times = []

fixed_process = 4

for sample in sample_sizes:
    start = time.time()

    calculate_pi_parallel(sample, fixed_process)

    exec_time = time.time() - start

    execution_times.append(exec_time)

    print(f"Sample: {sample}, Waktu: {exec_time:.4f} detik")

plt.figure(figsize=(10,6))

plt.plot(sample_sizes, execution_times, 'mo-')

plt.xlabel('Ukuran Sampel')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Waktu Eksekusi vs Ukuran Sampel')

plt.grid(True)

plt.show()

# =========================================
# Grafik 3 - Efficiency vs Jumlah Process
# =========================================

plt.figure(figsize=(10,6))

plt.plot(process_counts, efficiencies, 'go-')

plt.xlabel('Jumlah Process')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Jumlah Process')

plt.grid(True)

plt.show()
