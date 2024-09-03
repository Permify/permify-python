# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.5
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.list_type import ListType

class TestListType(unittest.TestCase):
    """ListType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListType:
        """Test ListType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListType`
        """
        model = ListType()
        if include_optional:
            return ListType(
                elem_type = permify.models.v1alpha1/type.v1alpha1.Type(
                    dyn = permify.models.dyn.dyn(), 
                    null = '', 
                    primitive = 'BOOL', 
                    wrapper = 'BOOL', 
                    well_known = 'ANY', 
                    list_type = permify.models.list_type.ListType(), 
                    map_type = permify.models.map_type.MapType(
                        key_type = permify.models.v1alpha1/type.v1alpha1.Type(
                            dyn = permify.models.dyn.dyn(), 
                            null = '', 
                            function = permify.models.function_type.FunctionType(
                                result_type = , 
                                arg_types = [
                                    
                                    ], ), 
                            message_type = '', 
                            type_param = '', 
                            type = , 
                            error = permify.models.error.error(), 
                            abstract_type = permify.models.abstract_type.AbstractType(
                                name = '', 
                                parameter_types = [
                                    
                                    ], ), ), 
                        value_type = , ), 
                    function = permify.models.function_type.FunctionType(), 
                    message_type = '', 
                    type_param = '', 
                    type = , 
                    error = permify.models.error.error(), 
                    abstract_type = permify.models.abstract_type.AbstractType(
                        name = '', ), )
            )
        else:
            return ListType(
        )
        """

    def testListType(self):
        """Test ListType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
