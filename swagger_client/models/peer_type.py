# coding: utf-8

"""
    Semux API

    Semux is an experimental high-performance blockchain platform that powers decentralized application.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PeerType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ip': 'str',
        'port': 'int',
        'network_version': 'int',
        'client_id': 'str',
        'peer_id': 'str',
        'latest_block_number': 'str',
        'latency': 'str',
        'capabilities': 'list[str]'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'network_version': 'networkVersion',
        'client_id': 'clientId',
        'peer_id': 'peerId',
        'latest_block_number': 'latestBlockNumber',
        'latency': 'latency',
        'capabilities': 'capabilities'
    }

    def __init__(self, ip=None, port=None, network_version=None, client_id=None, peer_id=None, latest_block_number=None, latency=None, capabilities=None):  # noqa: E501
        """PeerType - a model defined in Swagger"""  # noqa: E501

        self._ip = None
        self._port = None
        self._network_version = None
        self._client_id = None
        self._peer_id = None
        self._latest_block_number = None
        self._latency = None
        self._capabilities = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if network_version is not None:
            self.network_version = network_version
        if client_id is not None:
            self.client_id = client_id
        if peer_id is not None:
            self.peer_id = peer_id
        if latest_block_number is not None:
            self.latest_block_number = latest_block_number
        if latency is not None:
            self.latency = latency
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def ip(self):
        """Gets the ip of this PeerType.  # noqa: E501


        :return: The ip of this PeerType.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PeerType.


        :param ip: The ip of this PeerType.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this PeerType.  # noqa: E501


        :return: The port of this PeerType.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PeerType.


        :param port: The port of this PeerType.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def network_version(self):
        """Gets the network_version of this PeerType.  # noqa: E501


        :return: The network_version of this PeerType.  # noqa: E501
        :rtype: int
        """
        return self._network_version

    @network_version.setter
    def network_version(self, network_version):
        """Sets the network_version of this PeerType.


        :param network_version: The network_version of this PeerType.  # noqa: E501
        :type: int
        """

        self._network_version = network_version

    @property
    def client_id(self):
        """Gets the client_id of this PeerType.  # noqa: E501


        :return: The client_id of this PeerType.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PeerType.


        :param client_id: The client_id of this PeerType.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def peer_id(self):
        """Gets the peer_id of this PeerType.  # noqa: E501


        :return: The peer_id of this PeerType.  # noqa: E501
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this PeerType.


        :param peer_id: The peer_id of this PeerType.  # noqa: E501
        :type: str
        """

        self._peer_id = peer_id

    @property
    def latest_block_number(self):
        """Gets the latest_block_number of this PeerType.  # noqa: E501


        :return: The latest_block_number of this PeerType.  # noqa: E501
        :rtype: str
        """
        return self._latest_block_number

    @latest_block_number.setter
    def latest_block_number(self, latest_block_number):
        """Sets the latest_block_number of this PeerType.


        :param latest_block_number: The latest_block_number of this PeerType.  # noqa: E501
        :type: str
        """
        if latest_block_number is not None and not re.search('^\\d+$', latest_block_number):  # noqa: E501
            raise ValueError("Invalid value for `latest_block_number`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._latest_block_number = latest_block_number

    @property
    def latency(self):
        """Gets the latency of this PeerType.  # noqa: E501


        :return: The latency of this PeerType.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this PeerType.


        :param latency: The latency of this PeerType.  # noqa: E501
        :type: str
        """
        if latency is not None and not re.search('^\\d+$', latency):  # noqa: E501
            raise ValueError("Invalid value for `latency`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._latency = latency

    @property
    def capabilities(self):
        """Gets the capabilities of this PeerType.  # noqa: E501


        :return: The capabilities of this PeerType.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this PeerType.


        :param capabilities: The capabilities of this PeerType.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PeerType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other