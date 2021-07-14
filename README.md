# flaky-test-ci

Demonstrate usage of [Github Actions Plugin for test fliprate calculations](https://github.com/guotin/fliprate_actions).

## Workflow files

* `flaky-test-analysis-examples` workflow to demonstrate the usage of the plugin
    * Examples with existing `test_history.csv` and `JUnit` test result files
    * Heatmap images uploaded as `heatmaps` artifact
* `full-workflow` workflow to demonstrate flaky test analysis with previous test result artifacts
  * Download and unzip previous test result artifacts with `download_artifacts.py`
  * Upload test result and heatmap artifacts
* `full-workflow-with-download-plugin` to download artifacts with [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact)
  * Latest artifact zip contains all of the history -> download latest zip for flaky test analysis
  * Upload heatmaps and append current test result to the artifact  

### Scripts to generate test history

* Create `test_history.csv` with a fake 7 day history, 40 runs of each test per day (runs `pytest` 280 times)
  * `pip install -r requirements.txt` and `python generate_test_results.py`
* Create 15 `JUnit` test reports
  * `pip install -r requirements.txt` and `python generate_junit_history.py`   
