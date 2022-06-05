from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from currency.models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'base_type',
        'type',
        'created',
    )
    readonly_fields = (
        'type',
        'base_type',
    )
    list_filter = (
        'type',
        'base_type',
        ('created', DateRangeFilter),
        # ('buy', RangeNumericFilter),
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
