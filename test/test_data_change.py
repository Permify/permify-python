# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.8
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.data_change import DataChange

class TestDataChange(unittest.TestCase):
    """DataChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataChange:
        """Test DataChange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataChange`
        """
        model = DataChange()
        if include_optional:
            return DataChange(
                operation = 'OPERATION_UNSPECIFIED',
                tuple = permify.models.tuple.Tuple(
                    entity = permify.models.entity.Entity(
                        type = '', 
                        id = '', ), 
                    relation = '', 
                    subject = permify.models.subject.Subject(
                        type = '', 
                        id = '', 
                        relation = '', ), ),
                attribute = permify.models.attribute.Attribute(
                    entity = permify.models.entity.Entity(
                        type = '', 
                        id = '', ), 
                    attribute = '', 
                    value = {
                        'key' : None
                        }, )
            )
        else:
            return DataChange(
        )
        """

    def testDataChange(self):
        """Test DataChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
