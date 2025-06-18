import random
import csv
from datetime import datetime, timedelta

# Simulate synthetic traffic data
def generate_synthetic_logs(filename='data/synthetic/sample_log.csv', num_entries=1000):
    attack_types = ['normal', 'DDoS', 'SQLi', 'PortScan', 'BruteForce']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['timestamp', 'src_ip', 'dst_ip', 'packet_size', 'attack_type'])
        base_time = datetime.now()
        for _ in range(num_entries):
            timestamp = base_time + timedelta(seconds=random.randint(0, 10000))
            src_ip = f"192.168.0.{random.randint(1, 255)}"
            dst_ip = f"10.0.0.{random.randint(1, 255)}"
            packet_size = random.randint(64, 1500)
            attack_type = random.choices(attack_types, weights=[80, 5, 5, 5, 5])[0]
            writer.writerow([timestamp.isoformat(), src_ip, dst_ip, packet_size, attack_type])

if __name__ == "__main__":
    generate_synthetic_logs()
