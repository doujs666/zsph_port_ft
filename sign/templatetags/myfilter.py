from django import template

register = template.Library()


@register.filter()
def qwer(list1):
    for i, j in enumerate(list1):
        select_assert_list = ['assertEqual', 'assertNotEqual']
        if j == select_assert_list[i]:
            return True


# @register.simple_tag
# def get_value(assert_list):
#
#     for i, j in enumerate(assert_list):
#         return list2[i]


# print(qwer())