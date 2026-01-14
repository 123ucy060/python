
""" TASK 1: LOGIN STATUS COUNTER
logs = [
    "SUCCESS",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED",
    "SUCCESS",
    "FAILED"
]

👉 Tasks:

1)Count how many times SUCCESS
2)Count how many times FAILED
3)Print which one is higher

Expected Output:
SUCCESS count: 3
FAILED count: 4
More FAILED attempts
"""




logs = [
    "SUCCESS",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED",
    "SUCCESS",
    "FAILED"
]

success_count=0
failed_count=0

for status in logs:
    if status=="SUCCESS":
        success_count=success_count+1
    else:
        failed_count=failed_count+1

print('success count :',success_count)
print('failed count :',failed_count)

if success_count>failed_count:
    print('success count is higher')
else:
      print('failes count is higher')