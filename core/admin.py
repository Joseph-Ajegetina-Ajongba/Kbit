from django.contrib import admin
from .models import OrderItem, Order, Item, Payment, Coupon, Refund, Address, UserProfile


def make_refund_accepted(modeladadmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = "Update orders to refund granted"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'coupon',
                    'payment'
                    ]

    list_filter = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted'
    ]

    list_display_links = [
        'user',
        'billing_address',
        'shipping_address',
        'coupon', 'payment'
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'zipcode',
        'country',
        'address_type',
        'default',
    ]

    list_filter = [
        'default',
        'address_type',
        'country',
    ]

    search_fields = [
        'user',
        'street_address',
        'apartment_address',
        'zipcode',
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)