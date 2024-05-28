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

from permify.models.function_type import FunctionType

class TestFunctionType(unittest.TestCase):
    """FunctionType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionType:
        """Test FunctionType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionType`
        """
        model = FunctionType()
        if include_optional:
            return FunctionType(
                result_type = permify.models.v1alpha1/type.v1alpha1.Type(
                    dyn = permify.models.dyn.dyn(), 
                    null = '', 
                    primitive = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                    wrapper = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                    well_known = 'WELL_KNOWN_TYPE_UNSPECIFIED', 
                    list_type = permify.models.list_type.ListType(
                        elem_type = permify.models.v1alpha1/type.v1alpha1.Type(
                            dyn = permify.models.dyn.dyn(), 
                            null = '', 
                            map_type = permify.models.map_type.MapType(
                                key_type = , 
                                value_type = , ), 
                            function = permify.models.function_type.FunctionType(
                                arg_types = [
                                    
                                    ], ), 
                            message_type = '', 
                            type_param = '', 
                            type = , 
                            error = permify.models.error.error(), 
                            abstract_type = permify.models.abstract_type.AbstractType(
                                name = '', 
                                parameter_types = [
                                    
                                    ], ), ), ), 
                    map_type = permify.models.map_type.MapType(), 
                    function = permify.models.function_type.FunctionType(), 
                    message_type = '', 
                    type_param = '', 
                    type = , 
                    error = permify.models.error.error(), 
                    abstract_type = permify.models.abstract_type.AbstractType(
                        name = '', ), ),
                arg_types = [
                    permify.models.v1alpha1/type.v1alpha1.Type(
                        dyn = permify.models.dyn.dyn(), 
                        null = '', 
                        primitive = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                        wrapper = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                        well_known = 'WELL_KNOWN_TYPE_UNSPECIFIED', 
                        list_type = permify.models.list_type.ListType(
                            elem_type = permify.models.v1alpha1/type.v1alpha1.Type(
                                dyn = permify.models.dyn.dyn(), 
                                null = '', 
                                map_type = permify.models.map_type.MapType(
                                    key_type = , 
                                    value_type = , ), 
                                function = permify.models.function_type.FunctionType(
                                    result_type = , ), 
                                message_type = '', 
                                type_param = '', 
                                type = , 
                                error = permify.models.error.error(), 
                                abstract_type = permify.models.abstract_type.AbstractType(
                                    name = '', 
                                    parameter_types = [
                                        
                                        ], ), ), ), 
                        map_type = permify.models.map_type.MapType(), 
                        function = permify.models.function_type.FunctionType(), 
                        message_type = '', 
                        type_param = '', 
                        type = , 
                        error = permify.models.error.error(), 
                        abstract_type = permify.models.abstract_type.AbstractType(
                            name = '', ), )
                    ]
            )
        else:
            return FunctionType(
        )
        """

    def testFunctionType(self):
        """Test FunctionType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
