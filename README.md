# EPL_assert_demo

demo for an EPL assert class

API documentation can be found [here](https://sag-tgo.github.io/EPL_assert_demo/).

## Building docs
From an Apama command prompt:

`> apamadoc docs src/callback/Assert.mon src/AssertHelper.mon`

## Running demo tests
> Note: The tests intentionally fail to demonstrate failure output.

From an Apama command prompt in the tests directory:

`> pysys run` (to run all the tests)

`> pysys run <test name>` to run one test by name - e.g. `> pysys run demo_1`

You can then look at the correlator.log files in each test's Output directory.

## Excerpt from tests/Event correlator output
```
2020-09-21 17:21:35.624 ERROR [20812] - AssertTest [1] FAILED sensors should be the same: assertEquals - assert actual = expected
actual: device("CZ-3","droid","127.2.0.1")
expected: device("CZ-3","droid","127.0.0.1")
2020-09-21 17:21:35.624 ERROR [20812] - AssertTest [1] FAILED log messages should be the same : assertEquals - assert actual = expected
actual: Executed engine_inject <correlator> [test.mon]
expected: Executed engine_deploy <correlator> [test.mon]
2020-09-21 17:21:35.624 ERROR [20812] - AssertTest [1] FAILED four is greater than one: 1 <= 4
2020-09-21 17:21:35.624 ERROR [20812] - AssertTest [1] FAILED lesserThanFloatTest: -.19 >= -.2
2020-09-21 17:21:35.624 ERROR [20812] - AssertTest [1] FAILED throwTest2: function did not throw error when expecting to
2020-09-21 17:21:35.625 ERROR [20812] - AssertTest [1] FAILED noThrowTest2: function threw error when not expected to: com.apama.exceptions.Exception("Argument is not 1","IllegalArgumentException")
2020-09-21 17:21:35.625 ERROR [20812] - AssertTest [1] FAILED specificThrowTest2: function threw IllegalArgumentException when expecting a ArithmeticException exception
2020-09-21 17:21:35.625 ERROR [20812] - AssertTest [1] FAILED containsTest1: any(device,device("CZ-3","droid","127.0.0.1")) does not contain field id
```

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
