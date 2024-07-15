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

from permify.models.schema_definition import SchemaDefinition

class TestSchemaDefinition(unittest.TestCase):
    """SchemaDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaDefinition:
        """Test SchemaDefinition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaDefinition`
        """
        model = SchemaDefinition()
        if include_optional:
            return SchemaDefinition(
                entity_definitions = {
                    'key' : permify.models.entity_definition.EntityDefinition(
                        name = '', 
                        relations = {
                            'key' : permify.models.relation_definition.RelationDefinition(
                                name = '', 
                                relation_references = [
                                    permify.models.relation_reference.RelationReference(
                                        type = '', 
                                        relation = '', )
                                    ], )
                            }, 
                        permissions = {
                            'key' : permify.models.permission_definition.PermissionDefinition(
                                name = '', 
                                child = permify.models.child.Child(
                                    leaf = permify.models.leaf.Leaf(
                                        computed_user_set = permify.models.computed_user_set.ComputedUserSet(
                                            relation = '', ), 
                                        tuple_to_user_set = permify.models.tuple_to_user_set.TupleToUserSet(
                                            tuple_set = permify.models.tuple_set.TupleSet(
                                                relation = '', ), 
                                            computed = permify.models.computed_user_set.ComputedUserSet(
                                                relation = '', ), ), 
                                        computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                                            name = '', ), 
                                        call = permify.models.v1/call.v1.Call(
                                            rule_name = '', 
                                            arguments = [
                                                permify.models.argument.Argument(
                                                    context_attribute = permify.models.context_attribute.ContextAttribute(
                                                        name = '', ), )
                                                ], ), ), 
                                    rewrite = permify.models.rewrite.Rewrite(
                                        rewrite_operation = 'OPERATION_UNION', 
                                        children = [
                                            permify.models.child.Child()
                                            ], ), ), )
                            }, 
                        attributes = {
                            'key' : permify.models.attribute_definition.AttributeDefinition(
                                name = '', 
                                type = 'ATTRIBUTE_TYPE_BOOLEAN', )
                            }, 
                        references = {
                            'key' : 'REFERENCE_RELATION'
                            }, )
                    },
                rule_definitions = {
                    'key' : permify.models.rule_definition.RuleDefinition(
                        name = '', 
                        arguments = {
                            'key' : 'ATTRIBUTE_TYPE_BOOLEAN'
                            }, 
                        expression = permify.models.checked_expr.CheckedExpr(
                            reference_map = {
                                'key' : permify.models.v1alpha1/reference.v1alpha1.Reference(
                                    name = '', 
                                    overload_id = [
                                        ''
                                        ], 
                                    value = permify.models.constant.Constant(
                                        null_value = '', 
                                        bool_value = True, 
                                        int64_value = '', 
                                        uint64_value = '', 
                                        double_value = 1.337, 
                                        string_value = '', 
                                        bytes_value = 'YQ==', 
                                        duration_value = '', 
                                        timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                                }, 
                            type_map = {
                                'key' : permify.models.v1alpha1/type.v1alpha1.Type(
                                    dyn = permify.models.dyn.dyn(), 
                                    null = '', 
                                    primitive = 'BOOL', 
                                    wrapper = 'BOOL', 
                                    well_known = 'ANY', 
                                    list_type = permify.models.list_type.ListType(
                                        elem_type = permify.models.v1alpha1/type.v1alpha1.Type(
                                            dyn = permify.models.dyn.dyn(), 
                                            null = '', 
                                            map_type = permify.models.map_type.MapType(
                                                key_type = , 
                                                value_type = , ), 
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
                                                    
                                                    ], ), ), ), 
                                    map_type = permify.models.map_type.MapType(), 
                                    function = permify.models.function_type.FunctionType(), 
                                    message_type = '', 
                                    type_param = '', 
                                    type = , 
                                    error = permify.models.error.error(), 
                                    abstract_type = permify.models.abstract_type.AbstractType(
                                        name = '', ), )
                                }, 
                            source_info = permify.models.source_info.SourceInfo(
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
                                        call_expr = permify.models.expr/call.Expr.Call(), 
                                        list_expr = permify.models.create_list.CreateList(), 
                                        struct_expr = permify.models.create_struct.CreateStruct(
                                            message_name = '', ), 
                                        comprehension_expr = permify.models.comprehension.Comprehension(
                                            iter_var = '', 
                                            accu_var = '', ), )
                                    }, ), 
                            expr_version = '', 
                            expr = , ), )
                    },
                references = {
                    'key' : 'REFERENCE_ENTITY'
                    }
            )
        else:
            return SchemaDefinition(
        )
        """

    def testSchemaDefinition(self):
        """Test SchemaDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
