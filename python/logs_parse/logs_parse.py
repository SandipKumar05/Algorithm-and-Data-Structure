# Write a Python script that reads a log file (assume a standard text log file with one log entry per line) and identifies the top N (user-defined) error messages along with their counts.
# # ------------ method one----------------
# from collections import Counter
# with open('logs.txt','r') as logs:
#     error_logs=[]
#     for log in logs.readlines():
#         if log.lower().startswith('error'):
#             error_logs.append(log)
# # print(error_logs)
# error_counts=Counter(error_logs)
# for k,p in error_counts.items():
#     print(k,p)

# # ------------ method two----------------
from collections import defaultdict
with open('logs.txt','r') as file:
    log_dict=defaultdict(int)
    for line in file.readlines():
        log_dict[line.strip()]+=1

log_dict=dict(sorted(log_dict.items(), key=lambda x:x[1]))
print(log_dict)