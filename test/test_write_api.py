# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import influxdb2
from influxdb2.api.write_api import WriteApi  # noqa: E501
from influxdb2.rest import ApiException


class TestWriteApi(unittest.TestCase):
    """WriteApi unit test stubs"""

    def setUp(self):
        self.api = influxdb2.api.write_api.WriteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_write(self):
        """Test case for post_write

        write time-series data into influxdb  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
