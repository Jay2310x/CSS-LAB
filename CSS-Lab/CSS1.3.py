# Task 3: Python script with string manipulation, file read/write, and basic network communication

# -------- Part 1: String Manipulation --------
def reverse_string(s):
    return s[::-1]

# -------- Part 2: File Read and Write --------
def read_and_reverse_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        reversed_content = reverse_string(content)
        
        with open(output_file, 'w') as file:
            file.write(reversed_content)
        
        print(f"File content reversed and written to {output_file}")
        
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# -------- Part 3: Basic Network Communication --------
import socket

def start_echo_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server started on {host}:{port}. Waiting for connection...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection closed by client.")
                    break
                print(f"Received message: {data.decode()}")
                conn.sendall(data)  # Echo the same message back

# -------- Main Execution --------
if __name__ == "__main__":
    # Part 1 and 2: File manipulation
    input_file = 'input.txt'
    output_file = 'output.txt'
    read_and_reverse_file(input_file, output_file)
    
    # Part 3: Start the echo server
    start_echo_server()
