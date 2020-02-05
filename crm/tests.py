"""
使用django-admin，不够灵活，样式也是很难改变，

展示客户列表页面

把admin_class传递到前端：
1，{% for filter_field in admin_class.list_filters %}
2，{% for column in admin_class.list_display %}
3，{% for action in admin_class.actions %}
4，{% get_query_sets  admin_class as query_sets %}   return admin_class.model.objects.all()
5，



"""