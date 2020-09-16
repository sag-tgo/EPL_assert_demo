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
2020-09-16 16:23:29.912 INFO  [28052] - Injected MonitorScript from file C:\dev\git\epl-assert-demo\tests\demo_1\Input\test.mon (d853de08b665bd35b882e0b663ee8fc7), size 2059 bytes, compile time 0.00 seconds
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED sensors should be the same: assertEquals - assert actual = expected
actual: device("CZ-3","droid","127.2.0.1")
expected: device("CZ-3","droid","127.0.0.1")
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED log messages should be the same : assertEquals - assert actual = expected
actual: Executed engine_inject <correlator> [test.mon]
expected: Executed engine_deploy <correlator> [test.mon]
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED four is greater than one: 1 <= 4
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED lesserThanFloatTest: -.19 >= -.2
2020-09-16 16:23:29.913 INFO  [30176] - Sender engine_inject (y509133) (000001D7C75EB5D0) (component ID 6873106495892357376/6873387970869068032) disconnected cleanly: Other party requested disconnection
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED throwTest2: function did not throw error when expecting to
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED noThrowTest2: function threw error when not expected to: com.apama.exceptions.Exception("Argument is not 1","IllegalArgumentException")
2020-09-16 16:23:29.913 ERROR [31140] - AssertTest [1] FAILED specificThrowTest2: function threw IllegalArgumentException when expecting a ArithmeticException exception
2020-09-16 16:23:29.914 ERROR [31140] - AssertTest [1] FAILED containsTest1: any(device,device("CZ-3","droid","127.0.0.1")) does not contain field id
```
