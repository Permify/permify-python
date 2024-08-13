# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.partial_write_body import PartialWriteBody

class TestPartialWriteBody(unittest.TestCase):
    """PartialWriteBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartialWriteBody:
        """Test PartialWriteBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartialWriteBody`
        """
        model = PartialWriteBody()
        if include_optional:
            return PartialWriteBody(
                metadata = permify.models.schema_partial_write_request_metadata.SchemaPartialWriteRequestMetadata(
                    schema_version = '', ),
                partials = {
                    'key' : permify.models.partials_contains_the_write,_update_and_delete_definitions.Partials contains the write, update and delete definitions(
                        write = [
                            ''
                            ], 
                        delete = [
                            ''
                            ], 
                        update = [
                            ''
                            ], )
                    }
            )
        else:
            return PartialWriteBody(
        )
        """

    def testPartialWriteBody(self):
        """Test PartialWriteBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
