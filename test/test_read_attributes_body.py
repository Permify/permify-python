# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.read_attributes_body import ReadAttributesBody

class TestReadAttributesBody(unittest.TestCase):
    """ReadAttributesBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadAttributesBody:
        """Test ReadAttributesBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadAttributesBody`
        """
        model = ReadAttributesBody()
        if include_optional:
            return ReadAttributesBody(
                metadata = permify.models.attribute_read_request_metadata.AttributeReadRequestMetadata(
                    snap_token = '', ),
                filter = permify.models.attribute_filter.AttributeFilter(
                    entity = permify.models.entity_filter.EntityFilter(
                        type = '', 
                        ids = [
                            ''
                            ], ), 
                    attributes = [
                        ''
                        ], ),
                page_size = 56,
                continuous_token = ''
            )
        else:
            return ReadAttributesBody(
        )
        """

    def testReadAttributesBody(self):
        """Test ReadAttributesBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
