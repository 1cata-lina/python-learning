import os
import platform
import sys

class SystemInfo:
    """系统信息获取工具类"""

    def get_os_name(self):
        """获取操作系统名称：Windows / Linux / Darwin(mac)"""
        return platform.system()

    def get_os_detail(self):
        """获取系统完整版本信息"""
        return platform.platform()

    def get_os_version(self):
        """系统内部版本号"""
        return platform.version()

    def get_architecture(self):
        """系统位数：32bit / 64bit"""
        return platform.architecture()[0]

    def get_host_name(self):
        """计算机主机名"""
        return platform.node()

    def get_cpu_info(self):
        """CPU处理器型号"""
        return platform.processor()

    def get_current_user(self):
        """当前登录用户名"""
        try:
            return os.getlogin()
        except:
            # 部分IDE环境os.getlogin()报错，改用环境变量兼容
            if self.get_os_name() == "Windows":
                return os.environ.get("USERNAME")
            else:
                return os.environ.get("USER")

    def get_current_work_dir(self):
        """当前工作目录"""
        return os.getcwd()

    def get_python_bits(self):
        """Python解释器是32位还是64位"""
        return "64位" if sys.maxsize > 2 ** 32 else "32位"

    def get_temp_path(self):
        """系统临时文件夹路径"""
        if self.get_os_name() == "Windows":
            return os.environ.get("TEMP")
        else:
            return "/tmp"

    def get_home_dir(self):
        """用户家目录"""
        if self.get_os_name() == "Windows":
            return os.environ.get("USERPROFILE")
        else:
            return os.environ.get("HOME")

    def get_path_env(self):
        """系统PATH环境变量"""
        return os.environ.get("PATH")

    def get_all_info(self):
        """一键汇总所有系统信息，返回字典"""
        info = {
            "系统名称": self.get_os_name(),
            "完整系统信息": self.get_os_detail(),
            "系统版本号": self.get_os_version(),
            "系统架构位数": self.get_architecture(),
            "主机名称": self.get_host_name(),
            "CPU型号": self.get_cpu_info(),
            "当前用户": self.get_current_user(),
            "当前工作目录": self.get_current_work_dir(),
            "Python位数": self.get_python_bits(),
            "临时目录": self.get_temp_path(),
            "用户根目录": self.get_home_dir()
        }
        return info


# ========== 测试调用 ==========
if __name__ == "__main__":
    # 实例化对象
    sys_info = SystemInfo()

    # 单独调用某个方法
    print("操作系统：", sys_info.get_os_name())
    print("CPU：", sys_info.get_cpu_info())
    print("当前用户：", sys_info.get_current_user())

    print("-" * 50)

    # 一次性打印全部信息
    all_data = sys_info.get_all_info()
    for key, value in all_data.items():
        print(f"{key} : {value}")