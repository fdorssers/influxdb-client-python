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
from influxdb2.api.authorizations_api import AuthorizationsApi  # noqa: E501
from influxdb2.rest import ApiException


class TestAuthorizationsApi(unittest.TestCase):
    """AuthorizationsApi unit test stubs"""

    def setUp(self):
        self.api = influxdb2.api.authorizations_api.AuthorizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_authorizations_id(self):
        """Test case for delete_authorizations_id

        Delete a authorization  # noqa: E501
        """
        pass

    def test_get_authorizations(self):
        """Test case for get_authorizations

        List all authorizations  # noqa: E501
        """
        pass

    def test_get_authorizations_id(self):
        """Test case for get_authorizations_id

        Retrieve an authorization  # noqa: E501
        """
        pass

    def test_patch_authorizations_id(self):
        """Test case for patch_authorizations_id

        update authorization to be active or inactive. requests using an inactive authorization will be rejected.  # noqa: E501
        """
        pass

    def test_post_authorizations(self):
        """Test case for post_authorizations

        Create an authorization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
