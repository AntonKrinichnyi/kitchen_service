from django.contrib import admin
from kitchen_managment.models import Cook, Dish, DishType
from django.contrib.auth.admin import UserAdmin


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience"
                    )
                }
            )
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dishtype",)


admin.site.register(DishType)
