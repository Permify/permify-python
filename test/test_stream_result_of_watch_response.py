# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.7.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.stream_result_of_watch_response import StreamResultOfWatchResponse

class TestStreamResultOfWatchResponse(unittest.TestCase):
    """StreamResultOfWatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamResultOfWatchResponse:
        """Test StreamResultOfWatchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamResultOfWatchResponse`
        """
        model = StreamResultOfWatchResponse()
        if include_optional:
            return StreamResultOfWatchResponse(
                result = permify.models.watch_response.WatchResponse(
                    changes = permify.models.data_changes.DataChanges(
                        snap_token = '', 
                        data_changes = [
                            permify.models.data_change.DataChange(
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
                                    value = {
                                        'key' : None
                                        }, ), )
                            ], ), ),
                error = permify.models.status.Status(
                    code = 56, 
                    message = '', 
                    details = [
                        {
                            'key' : None
                            }
                        ], )
            )
        else:
            return StreamResultOfWatchResponse(
        )
        """

    def testStreamResultOfWatchResponse(self):
        """Test StreamResultOfWatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
