"""Dorm EP.2 - Latency"""
def main():
    """Main Function"""
    latency1 = int(input())
    latency2 = int(input())
    latency3 = int(input())
    latency4 = int(input())
    latency5 = int(input())
    latency6 = int(input())
    print("%i ms"%(min(latency1, latency2, latency3, latency4, latency5, latency6)))

main()
