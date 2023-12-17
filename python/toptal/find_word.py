# def sol(l):
#     s=[]
#     dic={}
#     for c in l:
#         c1,c2=c.split('>')
#         if c1 not in s:
#             start=c1
#         if c2 not in s:
#             s.append(c2)
#         dic[c1]=c2
#     c=start
#     ans=c
#     while True:
#         if c in dic:
#             ans+=dic[c]
#             c=dic[c]
#         else:
#             break
#     return ans
# l=["P>E","E>R","R>U"]
# print(sol(l))

# def format_seconds(seconds):
#     weeks, remainder = divmod(seconds, 604800)  # 1 week = 7 days * 24 hours * 60 minutes * 60 seconds
#     days, remainder = divmod(remainder, 86400)    # 1 day = 24 hours * 60 minutes * 60 seconds
#     hours, remainder = divmod(remainder, 3600)     # 1 hour = 60 minutes * 60 seconds
#     minutes, seconds = divmod(remainder, 60)

#     formatted_time = ""
#     if weeks > 0:
#         formatted_time += f"{weeks}w"
#     if days > 0:
#         formatted_time += f"{days}d"
#     if hours > 0:
#         formatted_time += f"{hours}h"
#     if minutes > 0:
#         formatted_time += f"{minutes}m"
#     if seconds > 0:
#         formatted_time += f"{seconds}s"

#     return formatted_time if formatted_time else "0s"

# # Example usage:
# seconds = 123456
# formatted_time = format_seconds(seconds)
# print(formatted_time)


# def shortest_consecutive_vacation(arr):
#     consecutive_lengths = []
#     current_length = 0

#     for day in arr:
#         if day == 1:  # Assuming 1 represents a vacation day
#             current_length += 1
#         else:
#             if current_length > 0:
#                 consecutive_lengths.append(current_length)
#                 current_length = 0

#     if current_length > 0:
#         consecutive_lengths.append(current_length)

#     return min(consecutive_lengths, default=0)

# # Example usage:
# vacation_days = [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
# result = shortest_consecutive_vacation(vacation_days)
# print(f"The shortest consecutive vacation days are: {result}")
def sol(num):
    b_string=str(bin(num)[2:]).split('1')
    ans=0
    for s in b_string:
        ans=max(ans,len(s))
    return ans
n=1041
print(sol(n))