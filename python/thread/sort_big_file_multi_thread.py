import threading
from concurrent.futures import ThreadPoolExecutor
import heapq

file_name = "tmp.txt"

chunk_size = 1024*1024

def sort_save_chunk(chunk, idx):
    chunk.sort()
    with open(f"{idx}.txt", 'w') as f:
        for l in chunk:
            f.write(l)
    return f"{idx}.txt"

def create_sorted_chunk(file_path):
    chunks =[]
    chunk = []
    chunk_index = 0

    with open(file_name, 'r') as f:
        while True:
            line =  f.readline()
            if not line:
                break
            chunk.append()
            if len(chunk) >= chunk_size:
                chunks.append(chunk)
    
    chunks.append(chunk)
    n = len(chunks)
    sorted_chunk_files = []
    with ThreadPoolExecutor(max_workers=n) as executor:

        futures = [executor.submit(sort_save_chunk, chunk, idx) for idx in range(n)]

        for f in futures:
            sorted_chunk_files.append(f.result())
    return sorted_chunk_files

def merge_sorted_chunk(sorted_file_path, output_file):
    heap = []
    file_pointers = []
    for f in sorted_file_path:
        f = open(f, 'r')
        file_pointers.append(f)
        line = f.readline()

        heapq.heappush(heap, (line, f))

    with open(output_file, 'w') as out_file:
        while heap:
            l, f = heapq.heappop()
            out_file.write(l)
            next_line = f.readline()
            if next_line:
                heapq.heappush(heap, (next_line, f))
    
    for f in file_pointers:
        f.close()