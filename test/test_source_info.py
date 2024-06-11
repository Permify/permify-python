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

from permify.models.source_info import SourceInfo

class TestSourceInfo(unittest.TestCase):
    """SourceInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceInfo:
        """Test SourceInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceInfo`
        """
        model = SourceInfo()
        if include_optional:
            return SourceInfo(
                syntax_version = '',
                location = '',
                line_offsets = [
                    56
                    ],
                positions = {
                    'key' : 56
                    },
                macro_calls = {
                    'key' : permify.models.expr.Expr(
                        id = '', 
                        const_expr = permify.models.constant.Constant(
                            null_value = '', 
                            bool_value = True, 
                            int64_value = '', 
                            uint64_value = '', 
                            double_value = 1.337, 
                            string_value = '', 
                            bytes_value = 'YQ==', 
                            duration_value = '', 
                            timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        ident_expr = permify.models.ident.Ident(
                            name = '', ), 
                        select_expr = permify.models.select.Select(
                            operand = permify.models.expr.Expr(
                                id = '', 
                                call_expr = permify.models.expr/call.Expr.Call(
                                    target = , 
                                    function = '', 
                                    args = [
                                        
                                        ], ), 
                                list_expr = permify.models.create_list.CreateList(
                                    elements = [
                                        
                                        ], 
                                    optional_indices = [
                                        56
                                        ], ), 
                                struct_expr = permify.models.create_struct.CreateStruct(
                                    message_name = '', 
                                    entries = [
                                        permify.models.entry.Entry(
                                            id = '', 
                                            field_key = '', 
                                            map_key = , 
                                            value = , 
                                            optional_entry = True, )
                                        ], ), 
                                comprehension_expr = permify.models.comprehension.Comprehension(
                                    iter_var = '', 
                                    iter_range = , 
                                    accu_var = '', 
                                    accu_init = , 
                                    loop_condition = , 
                                    loop_step = , 
                                    result = , ), ), 
                            field = '', 
                            test_only = True, ), 
                        call_expr = permify.models.expr/call.Expr.Call(
                            function = '', ), 
                        list_expr = permify.models.create_list.CreateList(), 
                        struct_expr = permify.models.create_struct.CreateStruct(
                            message_name = '', ), 
                        comprehension_expr = permify.models.comprehension.Comprehension(
                            iter_var = '', 
                            accu_var = '', ), )
                    }
            )
        else:
            return SourceInfo(
        )
        """

    def testSourceInfo(self):
        """Test SourceInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
