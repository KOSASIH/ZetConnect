[![Mark stale issues and pull requests](https://github.com/KOSASIH/internet-speed/actions/workflows/stale.yml/badge.svg)](https://github.com/KOSASIH/internet-speed/actions/workflows/stale.yml)
[![StackHawk](https://github.com/KOSASIH/internet-speed/actions/workflows/stackhawk.yml/badge.svg)](https://github.com/KOSASIH/internet-speed/actions/workflows/stackhawk.yml)


# Zetconnect 

# Class

To measure the current internet speed of a user's connection using Python, we can use the speedtest-cli library. Here's how you can install the necessary libraries and dependencies and develop a Python script for this task:

1. Install the required libraries:
   - Open a terminal or command prompt.
   - Run the following command to install the speedtest-cli library:
     ```
     pip install speedtest-cli
     ```

2. Develop the Python script:
   - Create a new Python file, e.g., `internet_speed_test.py`, and open it in a text editor.
   - Import the `speedtest` module from the `speedtest_cli` library:
     ```python
     import speedtest
     ```

   - Create a function to perform the speed test and print the results:
     ```python
     def measure_internet_speed():
         # Create a Speedtest object
         st = speedtest.Speedtest()
         
         # Perform the speed test
         download_speed = st.download() / 10**6  # Convert to Mbps
         upload_speed = st.upload() / 10**6  # Convert to Mbps
         ping = st.results.ping

         # Print the results
         print(f"Download Speed: {download_speed:.2f} Mbps")
         print(f"Upload Speed: {upload_speed:.2f} Mbps")
         print(f"Ping: {ping:.2f} ms")
     ```

   - Call the `measure_internet_speed()` function to perform the speed test:
     ```python
     if __name__ == "__main__":
         measure_internet_speed()
     ```

3. Save the file and exit the text editor.

To run the script and measure the internet speed:
- Open a terminal or command prompt.
- Navigate to the directory where you saved the `internet_speed_test.py` file.
- Run the following command:
  ```
  python internet_speed_test.py
  ```

The script will perform the speed test and print the download speed, upload speed, and ping in Mbps and milliseconds, respectively.

Note: Make sure you have a stable internet connection before running the script for accurate results.

# State Of The Art

To achieve the task of compressing a file using a state-of-the-art compression algorithm, such as LZ77 or DEFLATE, you can use the zlib library in Python. The zlib library provides functions for compression and decompression using the DEFLATE algorithm.

Here's a Python function that takes a file as input, compresses it using zlib, and outputs the compressed file along with the compression ratio:

```python
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
```

To use this function, you need to have the zlib library installed. If you're using Python 3, zlib is usually included in the standard library, so no additional installation is required.

Make sure to replace `'input.txt'` with the actual path to your input file, and `'compressed_file.txt'` with the desired output file path. After running the code, the compressed file will be created, and the compression ratio achieved will be printed.

Please note that the compression ratio achieved will vary depending on the input file and the compression algorithm used.
