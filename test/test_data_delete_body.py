# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.9
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.data_delete_body import DataDeleteBody

class TestDataDeleteBody(unittest.TestCase):
    """DataDeleteBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataDeleteBody:
        """Test DataDeleteBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataDeleteBody`
        """
        model = DataDeleteBody()
        if include_optional:
            return DataDeleteBody(
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
            return DataDeleteBody(
        )
        """

    def testDataDeleteBody(self):
        """Test DataDeleteBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()