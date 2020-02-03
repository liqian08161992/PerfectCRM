from django.contrib import admin
from crm import models
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','qq','qq_name','source','consultant','content','status','date')
    list_filter = ('source','consultant','date')
    search_fields = ('qq','qq_name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)
    list_per_page = 5
    #readonly_fields = ('qq','consultant')
    #ordering =


    # actions = ["test_action", ]
    #
    #
    # def test_action(self,request,arg2):
    #     print('test action:',self,request,arg2)
    #     return render(request,"king_admin/table_index.html")


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'name')


# class UserProfileAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'name', "is_active","is_staff",'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal', {'fields': ('name','stu_account')}),
#         ('Permissions', {'fields': ('is_admin',"is_active","roles","user_permissions","groups")}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ("roles","user_permissions","groups")
#




#注册操作
admin.site.register(models.Branch)
admin.site.register(models.ClassList)
admin.site.register(models.Course)
admin.site.register(models.CourseRecord)
admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Enrollment)
admin.site.register(models.Payment)
admin.site.register(models.Role)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Tag)
admin.site.register(models.Menu)