from django.contrib import admin
from portfolio.models import Student, Profile

# Custom admin site branding
admin.site.site_header = "My College Administration"
admin.site.site_title = "College Admin"
admin.site.index_title = "Wellcome to college Management"

# Register your models here.
# admin.site.register(Student)
# admin.site.register(Profile)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

    list_display = ('name', 'age', 'city')
    search_fields = ('name', 'city')
    list_filter = ('age', 'city')
    ordering = ('name',)

    list_per_page = 15


    @admin.display(description='status')
    def status(self, obj):
        if obj.age >= 18:
            return 'Adult'
        return 'Minor'