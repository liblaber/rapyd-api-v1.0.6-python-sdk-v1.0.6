from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .account import Account


@JsonMap({})
class InlineResponse200_24(BaseModel):
    """InlineResponse200_24

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: List[Account], optional
    """

    def __init__(self, status: Status = None, data: List[Account] = None):
        """InlineResponse200_24

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: List[Account], optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, Account)
