test_cases = [
    {"name": "Login", "status": "PASS", "duration": 2},
    {"name": "Signup", "status": "FAIL", "duration": 5},
    {"name": "Payment", "status": "PASS", "duration": 8},
    {"name": "Search", "status": "FAIL", "duration": 3},
    {"name": "Logout", "status": "PASS", "duration": 1}
]

new=[f"{test_case["name"]}" for test_case in test_cases if test_case["status"]=='PASS']
print(new)