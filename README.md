# EPL_assert_demo

Prototyping for an event to provide assertions in Apama EPL.

API documentation can be found [here](https://sag-tgo.github.io/EPL_assert_demo/).

## Building docs
From an Apama command prompt:

`> apamadoc docs src/Assert.mon src/AssertHelper.mon`

## Running demo tests
> Note: The tests intentionally fail to demonstrate failure output.

Make sure you have the EPL_TESTING_SDK environment variable set to the location
of your [apama-eplapps-tools](https://github.com/SoftwareAG/apama-eplapps-tools).

From an Apama command prompt in the tests directory:

`> pysys run` (to run all the tests)

`> pysys run <test name>` to run one test by name - e.g. `> pysys run Callback`

You can then look at the correlator.log files in each test's Output directory.

## Excerpt from tests/Callback correlator output
```
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: This should not happen!
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'The sky is blue' to equal true, got false
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'Pigs can fly' to equal false, got true
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'two plus two' to equal 4, got 5
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'sequential events IDs' to not equal, got 42
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'event count' to be greater than 7, got 3
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'event count' to be less than 0, got 3
2021-01-19 16:40:05.574 ERROR [140311279957760] - Demo [5] Assertion failed: Expected 'event count' to be >=5 and <=10, got 3
```
