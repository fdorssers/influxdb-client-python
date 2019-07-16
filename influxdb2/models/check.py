# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Check(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'message': 'str',
        'checks': 'list[Check]',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'message': 'message',
        'checks': 'checks',
        'status': 'status'
    }

    def __init__(self, name=None, message=None, checks=None, status=None):  # noqa: E501
        """Check - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._message = None
        self._checks = None
        self._status = None
        self.discriminator = None

        self.name = name
        if message is not None:
            self.message = message
        if checks is not None:
            self.checks = checks
        self.status = status

    @property
    def name(self):
        """Gets the name of this Check.  # noqa: E501


        :return: The name of this Check.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Check.


        :param name: The name of this Check.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def message(self):
        """Gets the message of this Check.  # noqa: E501


        :return: The message of this Check.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Check.


        :param message: The message of this Check.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def checks(self):
        """Gets the checks of this Check.  # noqa: E501


        :return: The checks of this Check.  # noqa: E501
        :rtype: list[Check]
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this Check.


        :param checks: The checks of this Check.  # noqa: E501
        :type: list[Check]
        """

        self._checks = checks

    @property
    def status(self):
        """Gets the status of this Check.  # noqa: E501


        :return: The status of this Check.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Check.


        :param status: The status of this Check.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["pass", "fail"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Check):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
