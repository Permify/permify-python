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

from openapi_client.models.create_struct import CreateStruct

class TestCreateStruct(unittest.TestCase):
    """CreateStruct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateStruct:
        """Test CreateStruct
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateStruct`
        """
        model = CreateStruct()
        if include_optional:
            return CreateStruct(
                message_name = '',
                entries = [
                    openapi_client.models.entry.Entry(
                        id = '', 
                        field_key = '', 
                        map_key = openapi_client.models.expr.Expr(
                            id = '', 
                            const_expr = openapi_client.models.constant.Constant(
                                null_value = '', 
                                bool_value = True, 
                                int64_value = '', 
                                uint64_value = '', 
                                double_value = 1.337, 
                                string_value = '', 
                                bytes_value = 'YQ==', 
                                duration_value = '', 
                                timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            ident_expr = openapi_client.models.ident.Ident(
                                name = '', ), 
                            select_expr = openapi_client.models.select.Select(
                                operand = openapi_client.models.expr.Expr(
                                    id = '', 
                                    call_expr = openapi_client.models.expr/call.Expr.Call(
                                        target = , 
                                        function = '', 
                                        args = [
                                            
                                            ], ), 
                                    list_expr = openapi_client.models.create_list.CreateList(
                                        elements = [
                                            
                                            ], 
                                        optional_indices = [
                                            56
                                            ], ), 
                                    struct_expr = openapi_client.models.create_struct.CreateStruct(
                                        message_name = '', ), 
                                    comprehension_expr = openapi_client.models.comprehension.Comprehension(
                                        iter_var = '', 
                                        iter_range = , 
                                        accu_var = '', 
                                        accu_init = , 
                                        loop_condition = , 
                                        loop_step = , 
                                        result = , ), ), 
                                field = '', 
                                test_only = True, ), 
                            call_expr = openapi_client.models.expr/call.Expr.Call(
                                function = '', ), 
                            list_expr = openapi_client.models.create_list.CreateList(), 
                            struct_expr = openapi_client.models.create_struct.CreateStruct(
                                message_name = '', ), 
                            comprehension_expr = openapi_client.models.comprehension.Comprehension(
                                iter_var = '', 
                                accu_var = '', ), ), 
                        value = , 
                        optional_entry = True, )
                    ]
            )
        else:
            return CreateStruct(
        )
        """

    def testCreateStruct(self):
        """Test CreateStruct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
