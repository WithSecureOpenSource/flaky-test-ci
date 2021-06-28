import json

import pandas as pd

GENERATED_TEST_HISTORY_PATH = "generated_test_history.json"
TEST_HISTORY_PATH = "test_history.csv"

with open(GENERATED_TEST_HISTORY_PATH, "r") as json_file:
    test_history = json.load(json_file)

i = 0
x = 0
for testrun in test_history["test_runs"]:
    testrun["timestamp"] = testrun["timestamp"] + x * 24 * 60 * 60
    i += 1
    if i >= 40:
        i = 0
        x += 1

d = []
for run in test_history["test_runs"]:
    time = run["timestamp"]
    for test_identifier, test_status in run["test_results"].items():
        d.append(
            {
                "timestamp": time,
                "test_identifier": test_identifier,
                "test_status": test_status,
            }
        )

df = pd.DataFrame(d)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
df = df.set_index("timestamp")
df = df.sort_index()
df.to_csv(TEST_HISTORY_PATH)
