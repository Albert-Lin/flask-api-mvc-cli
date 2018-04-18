from .abstract_validator import AbstractValidator
import api.repositories as repos
from api.repositories.base_repository import BaseRepository


class ExistValidator(AbstractValidator):
    def __init__(self):
        AbstractValidator.__init__(self)
        self._all_repos = {}
        for item in dir(repos):
            repo = getattr(repos, item)
            if isinstance(repo, BaseRepository):
                self._all_repos[repo.table_name] = repo

    def validator(self, dict_data, key, params):
        try:
            value = dict_data[key]
            table_name = params[0]
            result = self._all_repos[table_name].get_by_pk(value)
            if result is None:
                self._default_error_message = key + "(" + value + ") is not exist"
            return result
        except Exception as ex:
            self._default_error_message = "Parameter 0 of EXIST as model name is error"
            return False
