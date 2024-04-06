import hashlib

def login(end_str):
    for i in range(10000000000000000):
        if hashlib.sha256(f"CNS2024{i}".encode()).hexdigest().endswith(end_str):
            print(f"CNS2024{i}, {hashlib.sha256(f'CNS2024{i}'.encode()).hexdigest()}")
            return f"CNS2024{i}"
        
if __name__ == "__main__":
    end_str = input("Enter the end string: ")
    login(end_str)


