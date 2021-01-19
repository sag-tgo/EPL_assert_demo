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

## Excerpt from test/Event correlator output
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

## Excerpt from test/Static correlator output
```
2020-09-21 17:21:40.305 ERROR [10796] - Error on line 26 in action fail in event com.apamax.test.static.Assert: FailedAssertException - the sky is blue - C:\dev\git\epl-assert-demo\tests\Static\Input\../../../src/static/Assert.mon
2020-09-21 17:21:40.305 ERROR [10796] - TestAssert [1] Stack dump:
2020-09-21 17:21:40.305 ERROR [10796] - 	com.apamax.test.static.Assert.fail() C:\dev\git\epl-assert-demo\tests\Static\Input\../../../src/static/Assert.mon:26
2020-09-21 17:21:40.305 ERROR [10796] - 	com.apamax.test.static.Assert.true() C:\dev\git\epl-assert-demo\tests\Static\Input\../../../src/static/Assert.mon:36
2020-09-21 17:21:40.305 ERROR [10796] - 	TestAssert.onload() C:\dev\git\epl-assert-demo\tests\Static\Input\TestAssert.mon:6
2020-09-21 17:21:40.305 ERROR [10796] - 	TestAssert.::startupAction::() C:\dev\git\epl-assert-demo\tests\Static\Input\TestAssert.mon:4
...
2020-09-21 17:21:40.487 ERROR [10796] - TestExpect [2] the sky is blue
2020-09-21 17:21:40.487 ERROR [10796] - TestExpect [2] Two plus two = four
```

## Excerpt from test/Callback correlator output
```
2020-09-21 17:21:44.560 ERROR [15800] - TestAssert [1] the sky is blue
```
