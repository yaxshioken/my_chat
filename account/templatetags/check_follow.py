from django import template

from account.models import Account

register = template.Library()


@register.filter(name="follow")
def check_follow(account: Account, user: Account) -> str:
    if user in account.followers.all():
        return "unfollow"
    else:
        return "follow"

