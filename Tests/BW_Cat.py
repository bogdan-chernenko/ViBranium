import datetime
import logging

__author__ = "M_O_D_E_R"
__doc__ = """

    MTest this class for testing your apps

    All methods:

        -checkEqual()
        -checkNotEqual()
        -checkTrue()
        -checkFalse()
        -checkIn()
        -checkNotIn()
        -checkIs()
        -checkNotIs()
        -checkNone()

        -checkPositiveNumber()
        -checkNegativeNumber()
        -checkA_Less_B()
        -checkA_More_B()

"""


class MTest:
    """
        B      W
         \\    /
           Cat

        This module was created for testing ORM-module (Black-White Cat) BW Cat

            Example:
                test = MTest(True, True)

                test.check(1, 1)
                test.check(1, 2)

                test.results()
            
                Result:
                        -----------------------------------------------------
                            AssertionError
                                assert 1 == 2

                            Time: 2021-01-22 13:21:41.904296

                        -----------------------------------------------------


                        -----------------------------------------------------
                                Number of tests: 2
                                Number of failed tests: 1
                                Number of passed tests: 1
                        -----------------------------------------------------
    """
    def __init__(self, logging = False, show_info = False):
        self.num_of_tests = 0
        self.num_of_errors = 0
        self.num_of_passed_tests = 0

        self.logging = logging
        self.show_info = show_info

        self.time_start = 0

        self.text_error = """
        -----------------------------------------------------
            AssertionError
                assert {} {} {}

            Time: {}
        """


    def checkEqual(self, data_one, result):
        try:
            assert data_one == result, self.text_error.format(data_one, "==", result, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkNotEqual(self, data_one, result):
        try:
            assert data_one != result, self.text_error.format(data_one, "!=", result, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkTrue(self, data_one):
        try:
            assert data_one is True, self.text_error.format(data_one, "is", True, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkFalse(self, data_one):
        try:
            assert data_one is False, self.text_error.format(data_one, "is", False, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkIn(self, data, some_list):
        try:
            assert data in some_list, self.text_error.format(data, "in", some_list, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkNotIn(self, data, some_list):
        try:
            assert data not in some_list, self.text_error.format(data, "not in", some_list, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkIs(self, data, result):
        try:
            assert data is result, self.text_error.format(data, "is", result, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkNotIs(self, data, result):
        try:
            assert data is not result, self.text_error.format(data, "is not", result, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1
        


    def checkNone(self, data):
        try:
            assert data is None, self.text_error.format(data, "is", None, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1

    def checkPositiveNumber(self, number):
        try:
            assert number > 0, self.text_error.format(number, ">", 0, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkNegativeNumber(self, number):
        try:
            assert number < 0, self.text_error.format(number, "<", 0, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkA_Less_B(self, a, b):
        try:
            assert a < b, self.text_error.format(a, "<", b, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1


    def checkA_More_B(self, a, b):
        #if a > b:
        #    self.num_of_passed_tests += 1
        #else:
        #    self.num_of_errors += 1
        
        #self.num_of_tests += 1

        try:
            assert a > b, self.text_error.format(a, ">", b, datetime.datetime.now())
        except Exception as e:
            self.num_of_errors += 1
            print(e)
        else:
            self.num_of_passed_tests += 1
        finally:
            self.num_of_tests += 1





    def results(self):
        print("""\t-----------------------------------------------------
        \n
        -----------------------------------------------------
        \tNumber of tests: {}
        \tNumber of failed tests: {}
        \tNumber of passed tests: {}
        -----------------------------------------------------""".format(
            self.num_of_tests, self.num_of_errors, self.num_of_passed_tests
            ))