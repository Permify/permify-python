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

from permify.models.subjects import Subjects

class TestSubjects(unittest.TestCase):
    """Subjects unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Subjects:
        """Test Subjects
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Subjects`
        """
        model = Subjects()
        if include_optional:
            return Subjects(
                subjects = [
                    permify.models.subject.Subject(
                        type = '', 
                        id = '', 
                        relation = '', )
                    ]
            )
        else:
            return Subjects(
        )
        """

    def testSubjects(self):
        """Test Subjects"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
