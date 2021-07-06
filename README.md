# flaky-test-ci

Demonstrate usage of [Github Actions Plugin for test fliprate calculations](https://github.com/guotin/fliprate_actions).

## Workflow files

* Analysis workflow to demonstrate the usage of the plugin
    * Examples with existing `test_history.csv` and `JUnit` test result files
    * Example with downloading artifacts as `JUnit` files (to be added)
* Workflow that runs example test set with `pytest`, produces `report.xml` in `JUnit` format and uploads the artifact for later analysis 

### Scripts to generate test history

* Create `test_history.csv` with a fake 7 day history, 40 runs of each test per day (runs `pytest` 280 times)
  * `pip install -r requirements.txt` and `python generate_test_results.py`
* Create 15 `JUnit` test reports
  * `pip install -r requirements.txt` and `python generate_junit_history.py`   
