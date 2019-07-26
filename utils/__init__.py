def json_ify(instance, allow=None, exclude=()):  # exclude是排除在外的字段
    """此函数的作用是过滤输出字段"""
    # allow优先，如果有，就使用allow指定的字段，这时候exclude无效
    # allow如果为空，就全体，但要将exclude中的排除

    cls = type(instance)
    if allow:
        fn = (lambda x: x.name in allow)
    else:
        fn = (lambda x: x.name not in exclude)

    return {k.name: getattr(instance, k.name) for k in filter(fn, cls._meta.fields)}


d = {
    '400': {'error': "用户或密码错误"},
    '401': {'error': "用户输入错误"},
    '404': {'error': 'Not found'},
    '204': {'Good!': '删除成功'}
}
