# -------- Part 1: String Manipulation --------
def reverse_string(s):
    return s[::-1]

# -------- Part 2: File Read and Write --------
def read_and_reverse_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        print("Original Content:")
        print(content)
        
        reversed_content = reverse_string(content)
        
        with open(output_file, 'w') as file:
            file.write(reversed_content)
        
        print("Reversed content written to", output_file)
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# -------- Main Execution --------
if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    read_and_reverse_file(input_file, output_file)
