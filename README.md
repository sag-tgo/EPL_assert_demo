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

## Excerpt from tests/Simple correlator output
```
2021-05-24 14:25:23.639 ERROR [16948] - Demo [1] Assertion failed: This should not happen! @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:12}
2021-05-24 14:25:23.639 ERROR [16948] - Demo [1] Assertion failed: Expected 'The sky is blue' to equal true, got false @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:13}
2021-05-24 14:25:23.639 ERROR [16948] - Demo [1] Assertion failed: Expected 'Pigs can fly' to equal false, got true @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:14}
2021-05-24 14:25:23.639 ERROR [16948] - Demo [1] Assertion failed: Expected 'two plus two' to equal 4, got 5 @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:15}
2021-05-24 14:25:23.639 ERROR [16948] - Demo [1] Assertion failed: Expected 'sequential events IDs' to not equal, got 42 @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:17}
2021-05-24 14:25:23.640 ERROR [16948] - Demo [1] Assertion failed: Expected 'event count' to be greater than 7, got 3 @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:18}
2021-05-24 14:25:23.640 ERROR [16948] - Demo [1] Assertion failed: Expected 'event count' to be less than 0, got 3 @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:19}
2021-05-24 14:25:23.640 ERROR [16948] - Demo [1] Assertion failed: Expected 'event count' to be >=5 and <=10, got 3 @{Demo.onload() C:\dev\git\EPL_assert_demo\tests\Simple\Input\Demo.mon:20}
```
