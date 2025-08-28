from django.contrib.auth.models import Group
from helpers.RepositoryMixin import Repository


class GroupRepository(Repository):
    def __init__(self):
        self.entity = Group
