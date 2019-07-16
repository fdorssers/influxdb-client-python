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


class ViewProperties(object):
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
        'queries': 'list[DashboardQuery]',
        'colors': 'list[DashboardColor]',
        'note': 'str',
        'show_note_when_empty': 'bool'
    }

    attribute_map = {
        'queries': 'queries',
        'colors': 'colors',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty'
    }

    def __init__(self, queries=None, colors=None, note=None, show_note_when_empty=None):  # noqa: E501
        """ViewProperties - a model defined in OpenAPI"""  # noqa: E501

        self._queries = None
        self._colors = None
        self._note = None
        self._show_note_when_empty = None
        self.discriminator = None

        if queries is not None:
            self.queries = queries
        if colors is not None:
            self.colors = colors
        if note is not None:
            self.note = note
        if show_note_when_empty is not None:
            self.show_note_when_empty = show_note_when_empty

    @property
    def queries(self):
        """Gets the queries of this ViewProperties.  # noqa: E501


        :return: The queries of this ViewProperties.  # noqa: E501
        :rtype: list[DashboardQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this ViewProperties.


        :param queries: The queries of this ViewProperties.  # noqa: E501
        :type: list[DashboardQuery]
        """

        self._queries = queries

    @property
    def colors(self):
        """Gets the colors of this ViewProperties.  # noqa: E501

        Colors define color encoding of data into a visualization  # noqa: E501

        :return: The colors of this ViewProperties.  # noqa: E501
        :rtype: list[DashboardColor]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this ViewProperties.

        Colors define color encoding of data into a visualization  # noqa: E501

        :param colors: The colors of this ViewProperties.  # noqa: E501
        :type: list[DashboardColor]
        """

        self._colors = colors

    @property
    def note(self):
        """Gets the note of this ViewProperties.  # noqa: E501


        :return: The note of this ViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ViewProperties.


        :param note: The note of this ViewProperties.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def show_note_when_empty(self):
        """Gets the show_note_when_empty of this ViewProperties.  # noqa: E501

        if true, will display note when empty  # noqa: E501

        :return: The show_note_when_empty of this ViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Sets the show_note_when_empty of this ViewProperties.

        if true, will display note when empty  # noqa: E501

        :param show_note_when_empty: The show_note_when_empty of this ViewProperties.  # noqa: E501
        :type: bool
        """

        self._show_note_when_empty = show_note_when_empty

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
        if not isinstance(other, ViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
