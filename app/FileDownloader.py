import requests
import threading

class FileDownloader:
    def __init__(self, url, num_threads=4):
        self.url = url
        self.num_threads = num_threads
        self.total_size = 0
        self.downloaded_size = 0
        self.is_downloading = False
        self.file = None
        self.threads = []

    def _download_chunk(self, start, end):
        headers = {"Range": f"bytes={start}-{end}"}
        response = requests.get(self.url, headers=headers, stream=True)

        with self.file as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    self.downloaded_size += len(chunk)

    def _get_file_size(self):
        response = requests.head(self.url)
        self.total_size = int(response.headers.get("Content-Length", 0))

    def start_download(self, file_path):
        self.is_downloading = True
        self.file = open(file_path, "wb")

        self._get_file_size()

        chunk_size = self.total_size // self.num_threads
        self.threads = []

        for i in range(self.num_threads):
            start = i * chunk_size
            end = start + chunk_size - 1 if i < self.num_threads - 1 else self.total_size - 1

            thread = threading.Thread(target=self._download_chunk, args=(start, end))
            thread.start()
            self.threads.append(thread)

    def monitor_progress(self):
        while self.is_downloading:
            downloaded_percentage = (self.downloaded_size / self.total_size) * 100
            print(f"Downloaded: {downloaded_percentage:.2f}%")

            if self.downloaded_size >= self.total_size:
                self.is_downloading = False

    def wait_for_completion(self):
        for thread in self.threads:
            thread.join()

    def handle_interruption(self):
        self.is_downloading = False
        self.wait_for_completion()
        self.file.close()

# Example usage
downloader = FileDownloader("https://example.com/file.zip", num_threads=8)
downloader.start_download("file.zip")

# Start monitoring the progress in a separate thread
progress_thread = threading.Thread(target=downloader.monitor_progress)
progress_thread.start()

# Simulate interruption after 5 seconds
import time
time.sleep(5)
downloader.handle_interruption()

# Wait for the download to complete
downloader.wait_for_completion()

# Close the file
downloader.file.close()
