# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.data_write_body import DataWriteBody

class TestDataWriteBody(unittest.TestCase):
    """DataWriteBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataWriteBody:
        """Test DataWriteBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataWriteBody`
        """
        model = DataWriteBody()
        if include_optional:
            return DataWriteBody(
                metadata = permify.models.data_write_request_metadata.DataWriteRequestMetadata(
                    schema_version = '', ),
                tuples = [
                    permify.models.tuple.Tuple(
                        entity = permify.models.entity.Entity(
                            type = '', 
                            id = '', ), 
                        relation = '', 
                        subject = permify.models.subject.Subject(
                            type = '', 
                            id = '', 
                            relation = '', ), )
                    ],
                attributes = [
                    permify.models.attribute.Attribute(
                        entity = permify.models.entity.Entity(
                            type = '', 
                            id = '', ), 
                        attribute = '', 
                        value = {
                            'key' : None
                            }, )
                    ]
            )
        else:
            return DataWriteBody(
        )
        """

    def testDataWriteBody(self):
        """Test DataWriteBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
