# EPL_assert_demo

demo for an EPL assert class

API documentation can be found [here](https://sag-tgo.github.io/EPL_assert_demo/).

## Building docs
From an Apama command prompt:

`> apamadoc docs Asserts.mon`

## Running demo tests
> Note: The tests intentionally fail to demonstrate failure output.

From an Apama command prompt in the tests directory:

`> pysys run` (to run all the tests)

`> pysys run <test name>` to run one test by name - e.g. `> pysys run demo_1`

## Excerpt from demo_1 output
This is what appears in the correlator log when running the demo_1 test:
```
2020-09-17 10:24:22.167 ERROR [34628] - Error on line 18 in action fail in event com.apamax.test.Assert: FailedAssertException - the sky is blue - C:\dev\git\epl-assert-demo\tests\demo_1\Input\../../../Assert.mon
2020-09-17 10:24:22.167 ERROR [34628] - TestAssert [1] Stack dump:
2020-09-17 10:24:22.167 ERROR [34628] - 	com.apamax.test.Assert.fail() C:\dev\git\epl-assert-demo\tests\demo_1\Input\../../../Assert.mon:18
2020-09-17 10:24:22.167 ERROR [34628] - 	com.apamax.test.Assert.true() C:\dev\git\epl-assert-demo\tests\demo_1\Input\../../../Assert.mon:23
2020-09-17 10:24:22.167 ERROR [34628] - 	TestAssert.onload() C:\dev\git\epl-assert-demo\tests\demo_1\Input\TestAssert.mon:6
2020-09-17 10:24:22.167 ERROR [34628] - 	TestAssert.::startupAction::() C:\dev\git\epl-assert-demo\tests\demo_1\Input\TestAssert.mon:4
...
2020-09-17 10:24:22.407 ERROR [34628] - TestExpect [2] the sky is blue
2020-09-17 10:24:22.408 ERROR [34628] - TestExpect [2] Two plus two = four
...
2020-09-17 10:24:22.622 ERROR [34628] - AssertTest [3] FAILED sensors should be the same: assertEquals - assert actual = expected
actual: device("CZ-3","droid","127.2.0.1")
expected: device("CZ-3","droid","127.0.0.1")
2020-09-17 10:24:22.622 ERROR [34628] - AssertTest [3] FAILED log messages should be the same : assertEquals - assert actual = expected
actual: Executed engine_inject <correlator> [test.mon]
expected: Executed engine_deploy <correlator> [test.mon]
2020-09-17 10:24:22.624 ERROR [34628] - AssertTest [3] FAILED four is greater than one: 1 <= 4
2020-09-17 10:24:22.624 ERROR [34628] - AssertTest [3] FAILED lesserThanFloatTest: -.19 >= -.2
2020-09-17 10:24:22.625 ERROR [34628] - AssertTest [3] FAILED throwTest2: function did not throw error when expecting to
2020-09-17 10:24:22.626 ERROR [34628] - AssertTest [3] FAILED noThrowTest2: function threw error when not expected to: com.apama.exceptions.Exception("Argument is not 1","IllegalArgumentException")
2020-09-17 10:24:22.626 ERROR [34628] - AssertTest [3] FAILED specificThrowTest2: function threw IllegalArgumentException when expecting a ArithmeticException exception
2020-09-17 10:24:22.629 ERROR [34628] - AssertTest [3] FAILED containsTest1: any(device,device("CZ-3","droid","127.0.0.1")) does not contain field id
```
