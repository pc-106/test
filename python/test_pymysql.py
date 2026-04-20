try:
    import pymysql
    print("成功导入 pymysql 模块")
    print(f"pymysql 版本: {pymysql.__version__}")
except ImportError as e:
    print(f"导入失败: {e}")
    import sys
    print(f"Python 路径: {sys.path}")