import os
import json

TEST_REPORT_PATH = ".report.json"
TEST_HISTORY_PATH = "test_history.json"

with open(TEST_REPORT_PATH, "r") as json_file:
    new_test_results = json.load(json_file)

new_json_entry = {
    "timestamp": new_test_results["created"],
    "test_results": {
        test["nodeid"]: test["outcome"] for test in new_test_results["tests"]
    },
}

if not os.path.isfile(TEST_HISTORY_PATH):
    with open(TEST_HISTORY_PATH, "w") as json_file:
        json.dump({"test_runs": [new_json_entry]}, json_file)

else:
    with open(TEST_HISTORY_PATH, "r") as json_file:
        test_history = json.load(json_file)

    test_history["test_runs"].append(new_json_entry)

    with open(TEST_HISTORY_PATH, "w") as json_file:
        json.dump(test_history, json_file)
