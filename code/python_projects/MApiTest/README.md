# ApiTest 框架（最终版）

Python + Requests + Pytest + YAML + Allure 接口自动化测试框架。

## 框架分层

```
testcases/    测试用例（两种模式，可并存）
  ├─ test_posts_driven.py   数据驱动模式：用例写在 YAML 里，改 YAML 即可加用例
  └─ test_posts_manual.py   手写模式：api 层封装 + 直接断言
api/          业务接口层：组装参数、处理返回（business_api.py）
core/         核心引擎
  ├─ http_client.py   底层 HTTP 客户端（发请求 + 日志）
  ├─ api_factory.py   接口方法层（把 HTTP 接口封装成 Python 方法）
  ├─ api_service.py   数据驱动引擎（解析 YAML 用例 -> 发请求 -> 提取 -> 断言）
  └─ result_base.py   统一响应结果类
utils/        工具层
  ├─ file_reader.py   读取 settings.ini / data.yaml
  ├─ log_util.py      日志（控制台 + log/ 按日文件）
  ├─ yaml_util.py     读用例 YAML、读写 extract.yaml
  ├─ extract_util.py  ${} 变量/函数动态解析、提取响应变量
  ├─ assert_util.py   jsonpath 断言（eq/lt/le/gt/ge/ne/contains/startswith/endswith/length）
  ├─ response_util.py 响应统一解析
  └─ mysql_util.py    MySQL 校验（惰性连接）
config/       配置（settings.ini：host、mysql）
data/         测试数据与用例 YAML
message/      钉钉/企微消息推送（需自配 webhook）
log/          运行日志
report/       allure 报告原始数据
```

## 快速开始

1. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

2. 修改 `config/settings.ini` 的 `api_sit_url` 为被测系统地址。

3. 运行全部用例：

   ```bash
   pytest
   ```

4. 生成 allure 报告（需本地安装 allure 命令行工具）：

   ```bash
   allure serve ./report
   ```

## 加一条用例（数据驱动模式）

编辑 `data/posts_center.yaml`，按格式追加：

```yaml
my_case:
  - request_info:
      case_title: 我的用例标题
      url: /my/api
      method: POST
      headers:
        Content-Type: application/json
    case_info:
      - json:
          name: test
        extract:            # 可选：提取响应变量供后续用例复用
          my_id: $.id
        validate:           # 可选：断言
          - eq: [ '$.code', 200 ]
```

然后在 `testcases/` 下写一个三行用例文件：

```python
import allure
import pytest
from core.api_service import ApiService
from utils.yaml_util import YamlUtil

@allure.feature("我的模块")
class TestMyModule:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("posts_center.yaml", "my_case"))
    def test_my_case(self, data):
        ApiService().handle_case(data)
```

## 支持的动态表达式

- `${get_time()}` 当前时间戳
- `${get_random(1,100)}` 随机数
- `${get_add(1,2)}` 加法
- `${get_extract_value(post_id)}` 引用 extract.yaml 中提取的变量

## 说明

- 示例用例基于公共测试接口 jsonplaceholder（https://jsonplaceholder.typicode.com），开箱即可运行；
- 原教学框架针对 5istudy 商城的业务用例依赖其后端和数据库，已替换为通用示例，迁移到自己的项目时改 `settings.ini` + `api_factory.py` + `business_api.py` 即可；
- MySQL 校验为可选能力，未配置连接时不会连接数据库。
