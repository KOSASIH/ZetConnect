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
