from unstructured.partition.auto import partition
import time
import os


total_start = time.time()
for file_name in os.listdir("db"):
    file_path = os.path.join("db", file_name)
    print(file_path)
    start = time.time()
    elements = partition(file_path, strategy="fast")
    end = time.time()
    print(end - start)
print("finished")
total_end = time.time()
print(total_end- total_start)

