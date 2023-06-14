import abc

from app.repositories.abstract_repo import AbstractRepository


class AbstractService(abc.ABC):
    _repository: AbstractRepository

    def __init__(self, repo: AbstractRepository):
        self._repository = repo
