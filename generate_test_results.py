import subprocess

for i in range(280):
    subprocess.run(["pytest", "--json-report"])
    subprocess.run(["python", "append_test_result.py"])

subprocess.run(["python", "create_test_history.py"])
