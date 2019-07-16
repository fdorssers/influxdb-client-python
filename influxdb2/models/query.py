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


class Query(object):
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
        'extern': 'File',
        'query': 'str',
        'type': 'str',
        'db': 'str',
        'rp': 'str',
        'cluster': 'str',
        'dialect': 'Dialect'
    }

    attribute_map = {
        'extern': 'extern',
        'query': 'query',
        'type': 'type',
        'db': 'db',
        'rp': 'rp',
        'cluster': 'cluster',
        'dialect': 'dialect'
    }

    def __init__(self, extern=None, query=None, type='flux', db=None, rp=None, cluster=None, dialect=None):  # noqa: E501
        """Query - a model defined in OpenAPI"""  # noqa: E501

        self._extern = None
        self._query = None
        self._type = None
        self._db = None
        self._rp = None
        self._cluster = None
        self._dialect = None
        self.discriminator = None

        if extern is not None:
            self.extern = extern
        self.query = query
        if type is not None:
            self.type = type
        if db is not None:
            self.db = db
        if rp is not None:
            self.rp = rp
        if cluster is not None:
            self.cluster = cluster
        if dialect is not None:
            self.dialect = dialect

    @property
    def extern(self):
        """Gets the extern of this Query.  # noqa: E501


        :return: The extern of this Query.  # noqa: E501
        :rtype: File
        """
        return self._extern

    @extern.setter
    def extern(self, extern):
        """Sets the extern of this Query.


        :param extern: The extern of this Query.  # noqa: E501
        :type: File
        """

        self._extern = extern

    @property
    def query(self):
        """Gets the query of this Query.  # noqa: E501

        query script to execute.  # noqa: E501

        :return: The query of this Query.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Query.

        query script to execute.  # noqa: E501

        :param query: The query of this Query.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def type(self):
        """Gets the type of this Query.  # noqa: E501

        type of query  # noqa: E501

        :return: The type of this Query.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Query.

        type of query  # noqa: E501

        :param type: The type of this Query.  # noqa: E501
        :type: str
        """
        allowed_values = ["flux", "influxql"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def db(self):
        """Gets the db of this Query.  # noqa: E501

        required for influxql type queries  # noqa: E501

        :return: The db of this Query.  # noqa: E501
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this Query.

        required for influxql type queries  # noqa: E501

        :param db: The db of this Query.  # noqa: E501
        :type: str
        """

        self._db = db

    @property
    def rp(self):
        """Gets the rp of this Query.  # noqa: E501

        required for influxql type queries  # noqa: E501

        :return: The rp of this Query.  # noqa: E501
        :rtype: str
        """
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Sets the rp of this Query.

        required for influxql type queries  # noqa: E501

        :param rp: The rp of this Query.  # noqa: E501
        :type: str
        """

        self._rp = rp

    @property
    def cluster(self):
        """Gets the cluster of this Query.  # noqa: E501

        required for influxql type queries  # noqa: E501

        :return: The cluster of this Query.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Query.

        required for influxql type queries  # noqa: E501

        :param cluster: The cluster of this Query.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def dialect(self):
        """Gets the dialect of this Query.  # noqa: E501


        :return: The dialect of this Query.  # noqa: E501
        :rtype: Dialect
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """Sets the dialect of this Query.


        :param dialect: The dialect of this Query.  # noqa: E501
        :type: Dialect
        """

        self._dialect = dialect

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
        if not isinstance(other, Query):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
