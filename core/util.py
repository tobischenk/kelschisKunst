from random import shuffle

from django.db.models import QuerySet


def shuffle_queryset(queryset: QuerySet):
    queryset_list = list(queryset)
    shuffle(queryset_list)

    return queryset_list
