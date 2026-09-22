# -*- coding: utf-8 -*-
"""断言工具：jsonpath 取值 + 多种断言方式，供数据驱动 validate 使用。

YAML validate 写法：
  - eq: [ '$.id', 1 ]          # 相等
  - contains: [ '$.title', 'x' ]  # 包含
  - length: [ '$..id', 4 ]     # 数量
"""
import jsonpath


class AssertUtil:

    @staticmethod
    def equals(check_value, expect_value):
        """相等"""
        assert check_value == expect_value, "{} != {}".format(check_value, expect_value)

    @staticmethod
    def less_than(check_value, expect_value):
        """小于"""
        assert check_value < expect_value, "{} < {}".format(check_value, expect_value)

    @staticmethod
    def less_than_or_equals(check_value, expect_value):
        """小于等于"""
        assert check_value <= expect_value, "{} <= {}".format(check_value, expect_value)

    @staticmethod
    def greater_than(check_value, expect_value):
        """大于"""
        assert check_value > expect_value, "{} > {}".format(check_value, expect_value)

    @staticmethod
    def greater_than_or_equals(check_value, expect_value):
        """大于等于"""
        assert check_value >= expect_value, "{} >= {}".format(check_value, expect_value)

    @staticmethod
    def not_equals(check_value, expect_value):
        """不等于"""
        assert check_value != expect_value, "{} != {}".format(check_value, expect_value)

    @staticmethod
    def contains(check_value, expect_value):
        """包含"""
        assert expect_value in check_value, "{} 不包含 {}".format(check_value, expect_value)

    @staticmethod
    def startswith(check_value, expect_value):
        """以什么开头"""
        assert str(check_value).startswith(str(expect_value)), "{} 不以 {} 开头".format(
            check_value, expect_value)

    @staticmethod
    def endswith(check_value, expect_value):
        """以什么结尾"""
        assert str(check_value).endswith(str(expect_value)), "{} 不以 {} 结尾".format(
            check_value, expect_value)

    @staticmethod
    def length(check_value, expect_value):
        """校验数量"""
        if not isinstance(check_value, list):
            check_value = [check_value]
        assert len(check_value) == expect_value, "长度 {} != {}".format(
            len(check_value), expect_value)

    def extract_by_jsonpath(self, extract_value, extract_expression):
        """jsonpath 取值：'$.code' / '$..id' / '$[0].title'"""
        if not isinstance(extract_expression, str):
            return extract_expression
        result = jsonpath.jsonpath(extract_value, extract_expression)
        if not result:
            return None
        if len(result) == 1:
            return result[0]
        return result

    def validate_response(self, response, validate_check):
        """按 validate 规则逐条断言"""
        for check in validate_check:
            for check_type, check_value in check.items():
                actual_value = self.extract_by_jsonpath(response, check_value[0])
                expect_value = check_value[1]
                if check_type in ["eq", "equals", "equal"]:
                    self.equals(actual_value, expect_value)
                elif check_type in ["lt", "less_than"]:
                    self.less_than(actual_value, expect_value)
                elif check_type in ["le", "less_or_equals"]:
                    self.less_than_or_equals(actual_value, expect_value)
                elif check_type in ["gt", "greater_than"]:
                    self.greater_than(actual_value, expect_value)
                elif check_type in ["ge", "greater_or_equals"]:
                    self.greater_than_or_equals(actual_value, expect_value)
                elif check_type in ["ne", "not_equal"]:
                    self.not_equals(actual_value, expect_value)
                elif check_type in ["contains"]:
                    self.contains(actual_value, expect_value)
                elif check_type in ["startswith"]:
                    self.startswith(actual_value, expect_value)
                elif check_type in ["endswith"]:
                    self.endswith(actual_value, expect_value)
                elif check_type in ["length"]:
                    self.length(actual_value, expect_value)
                else:
                    raise ValueError("不支持的断言类型: {}".format(check_type))
