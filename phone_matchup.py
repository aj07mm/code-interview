import unittest
import re
from collections import defaultdict

"""
The phone matchup coding test.

A phone company keeps record of all calls that have been successfully
established. For these calls, the company registers
whether they fail mid-call or complete successfully. We are interested in
computing the "success ratio", which is defined by the number of successful
calls vs. absolute number of calls that involved a party.

The format is:
date: day.month.year 24hours:minutes
caller: phone number
callee: phone number
status: COMPLETED/FAILED

When 111 would call 222 and the call would end successfully, the following
entry would show up in the log_data:
1.1.2014 12:33,111,222,COMPLETED
This call is counted as completed for both parties!
If the same call fails mid-call, the line would look like this
1.1.2014 12:33,111,222,FAILED
This call is counted as failed for both parties!

Implement a function that takes log data from a string and turns it into a
data structure that represents the association between a number and a success
percentage-string which is ready for display.

Feel free to use any available modules from the language standard library.
Feel free to add test cases as you see fit.
 Also, send along an estimate of the time it took you
to complete this test.

We evaluate the submission based on: correctness, structure, appropriate
use of data structures, efficiency, appropriate use of standard library
functionality.

An example:

1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED

Resulting output of success rates:

111-222-333: 40.00%
454-333-222: 66.67%
111-333 : 0.00%

"""


def parse(log_data):
    """
        1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
        1.1.2014 13:01,111-222-333,111-333,FAILED
        1.1.2014 13:04,111-222-333,454-333-222,FAILED
        1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
        2.1.2014 13:01,111-333,111-222-333,FAILED

        111-222-333: 40.00%
        454-333-222: 66.67%
        111-333 : 0.00%
    """
    pattern = "\d\.\d\.\d{4}\s\d{2}:\d{2},\d{3}(?:-\d{3})?-\d{3},\d{3}-\d{3}(?:-\d{3})?,(?:COMPLETED|FAILED)"  # noqa: E501
    log_lines = re.findall(pattern, log_data)
    log_calls = defaultdict(lambda: defaultdict(int))
    log_output = defaultdict(float)

    for line in log_lines:
        date, caller, callee, status = line.split(',')
        log_calls[callee]['completed_calls'] += int(status == "COMPLETED")
        log_calls[callee]['calls'] += 1
        log_calls[caller]['completed_calls'] += int(status == "COMPLETED")
        log_calls[caller]['calls'] += 1

    for k, v in log_calls.items():
        log_output[k] = round(v['completed_calls']/v['calls'] * 100, 2)

    return log_output


class TestParse(unittest.TestCase):
    def test_one_line(self):
        log_data = """
            1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
        """
        self.assertEqual(parse(log_data), {
            "111-222-333": 100.00,
            "454-333-222": 100.00,
        })

    def test_two_lines_of_the_same(self):
        log_data = """
            1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
            2.1.2014 12:01,111-222-333,454-333-222,COMPLETED
        """
        self.assertEqual(parse(log_data), {
            "111-222-333": 100.00,
            "454-333-222": 100.00,
        })

    def test_two_lines_with_one_not_completed(self):
        log_data = """
            1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
            2.1.2014 12:01,111-222-333,454-333-222,FAILED
        """
        self.assertEqual(parse(log_data), {
            "111-222-333": 50.00,
            "454-333-222": 50.00,
        })

    def test_three_lines_with_one_not_completed(self):
        log_data = """
            1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
            2.1.2014 12:01,111-222-333,454-333-222,COMPLETED
            2.1.2014 12:01,111-222-333,454-333-222,FAILED
        """
        self.assertEqual(parse(log_data), {
            "111-222-333": 66.67,
            "454-333-222": 66.67,
        })

    def test_example(self):
        log_data = """
            1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
            1.1.2014 13:01,111-222-333,111-333,FAILED
            1.1.2014 13:04,111-222-333,454-333-222,FAILED
            1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
            2.1.2014 13:01,111-333,111-222-333,FAILED
        """
        self.assertEqual(parse(log_data), {
            "111-222-333": 40.00,
            "454-333-222": 66.67,
            "111-333": 0.0,
        })


if __name__ == "__main__":
    unittest.main()
