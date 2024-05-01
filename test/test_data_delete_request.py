# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.2
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.data_delete_request import DataDeleteRequest

class TestDataDeleteRequest(unittest.TestCase):
    """DataDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataDeleteRequest:
        """Test DataDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataDeleteRequest`
        """
        model = DataDeleteRequest()
        if include_optional:
            return DataDeleteRequest(
                tuple_filter = permify.models.tuple_filter.TupleFilter(
                    entity = permify.models.entity_filter.EntityFilter(
                        type = '', 
                        ids = [
                            ''
                            ], ), 
                    relation = '', 
                    subject = permify.models.subject_filter.SubjectFilter(
                        type = '', 
                        ids = [
                            ''
                            ], 
                        relation = '', ), ),
                attribute_filter = permify.models.attribute_filter.AttributeFilter(
                    entity = permify.models.entity_filter.EntityFilter(
                        type = '', 
                        ids = [
                            ''
                            ], ), 
                    attributes = [
                        ''
                        ], )
            )
        else:
            return DataDeleteRequest(
        )
        """

    def testDataDeleteRequest(self):
        """Test DataDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
