import sys

import pandas as pd

TEST_HISTORY_PATH = sys.argv[1]
TOP_N = int(sys.argv[2])
EWM_ALPHA = 0.1
EWM_ADJUST = False


def calc_fliprate(testruns: pd.Series) -> float:
    """Calculate test result fliprate from given test results series"""
    if len(testruns) == 1:
        return 0
    first = True
    previous = None
    flips = 0
    possible_flips = len(testruns) - 1
    for _, val in testruns.iteritems():
        if first:
            first = False
            previous = val
            continue
        if val != previous:
            flips += 1
        previous = val
    return flips / possible_flips


def calculate_n_day_flipdata(
    testrun_table: pd.DataFrame, days: int, window_count: int
) -> None:
    """Select given history amount and calculate fliprates for given n day groups
    Return visualization data for max top 50 "flaky" test identifiers.
    """
    data = testrun_table[
        testrun_table.index
        >= (testrun_table.index.max() - pd.Timedelta(days=days * window_count))
    ]

    fliprates = data.groupby([pd.Grouper(freq=f"{days}D"), "test_identifier"])[
        "test_status"
    ].apply(calc_fliprate)

    fliprate_table = fliprates.rename("flip_rate").reset_index()
    fliprate_table["flip_rate_ewm"] = (
        fliprate_table.groupby("test_identifier")["flip_rate"]
        .ewm(alpha=EWM_ALPHA, adjust=EWM_ADJUST)
        .mean()
        .droplevel("test_identifier")
    )

    top_fliprates = fliprate_table[
        fliprate_table["timestamp"].max() == fliprate_table["timestamp"]
    ].nlargest(TOP_N, "flip_rate")[["test_identifier", "flip_rate"]]

    top_fliprates_ewm = fliprate_table[
        fliprate_table["timestamp"].max() == fliprate_table["timestamp"]
    ].nlargest(TOP_N, "flip_rate_ewm")[["test_identifier", "flip_rate_ewm"]]

    return top_fliprates.to_records(index=False), top_fliprates_ewm.to_records(
        index=False
    )


if __name__ == "__main__":

    df = pd.read_csv(
        TEST_HISTORY_PATH,
        index_col="timestamp",
        parse_dates=["timestamp"],
    )

    top_fliprates, top_fliprates_ewm = calculate_n_day_flipdata(df, 1, 7)

    print(f"Top {TOP_N} flaky tests based on latest fliprate")
    for testname, score in top_fliprates:
        print(testname, "--- score:", score)
    print(
        f"\nTop {TOP_N} flaky tests based on latest exponential weighted moving average fliprate score"
    )
    for testname, score in top_fliprates_ewm:
        print(testname, "--- score:", score)
