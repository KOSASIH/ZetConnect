import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()

    compressed_data = zlib.compress(data)

    with open(output_file, 'wb') as file:
        file.write(compressed_data)

    compression_ratio = len(compressed_data) / len(data)
    print(f"Compression ratio achieved: {compression_ratio:.2f}")

# Usage example:
input_file = 'input.txt'
output_file = 'compressed_file.txt'
compress_file(input_file, output_file)
