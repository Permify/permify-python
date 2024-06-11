# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.attribute_read_response import AttributeReadResponse

class TestAttributeReadResponse(unittest.TestCase):
    """AttributeReadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeReadResponse:
        """Test AttributeReadResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeReadResponse`
        """
        model = AttributeReadResponse()
        if include_optional:
            return AttributeReadResponse(
                attributes = [
                    permify.models.attribute.Attribute(
                        entity = permify.models.entity.Entity(
                            type = '', 
                            id = '', ), 
                        attribute = '', 
                        value = {
                            'key' : None
                            }, )
                    ],
                continuous_token = ''
            )
        else:
            return AttributeReadResponse(
        )
        """

    def testAttributeReadResponse(self):
        """Test AttributeReadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
