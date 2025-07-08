def check_pin(pin):
    # Simulated correct PIN for testing
    correct_pin = "0427"
    return pin == correct_pin

def brute_force_pin():
    for i in range(10000):
        attempt = f"{i:04d}"  # Format number as 4-digit string, e.g., "0001"
        if check_pin(attempt):
            print(f"PIN found: {attempt}")
            return attempt
    print("PIN not found")
    return None

if __name__ == "__main__":
    brute_force_pin()
