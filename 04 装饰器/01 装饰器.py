"""
装饰器的常见应用场景
    日志记录： 在函数执行前后打印日志信息。
    性能监测： 统计函数的执行时间。
    权限验证： 检查用户是否有权限执行操作。
    输入参数检查： 验证函数输入参数的合法性。
    函数缓存： 缓存函数计算结果，提高性能。
"""

"""
编写装饰器的注意事项
1.保留原函数的元信息
    import functools
    使用 functools.wraps 保留被装饰函数的原始属性（如 __name__ 和 __doc__）。
2.装饰器带参数
    如果装饰器需要参数，通常需要再多嵌套一层。
"""
import functools

# 访问控制（权限验证）
def requires_permission(permission):
    def decorator(func):  # outer
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # inner
            if args[0].get("permission") == permission:
                return func(*args, **kwargs)
            else:
                print(f"Access denied for user: {args[0].get('name')}")
        return wrapper
    return decorator

@requires_permission("admin")
def delete_user(user, target_user):
    """
    :param user:
    :param target_user:
    :return: null
    写删除用户逻辑
    """
    print(f"User {target_user} deleted by {user['name']}")

print(delete_user.__doc__)

# 测试
admin_user = {"name": "Alice", "permission": "admin"}
regular_user = {"name": "Bob", "permission": "user"}

delete_user(admin_user, "Charlie")  # 有权限
delete_user(regular_user, "Charlie")  # 无权限
