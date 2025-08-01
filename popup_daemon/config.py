#!/bin/python
from typing import TypeAlias

KwargsType: TypeAlias = list[str]

class Config:
    def __new__(cls) -> None:
        raise TypeError(f"{cls.__name__} cannot be instantiated.")

    window_names:list[str] = []

    @classmethod
    def init(cls, **kwargs:KwargsType) -> None:
        if kwargs.get("window_names", None):
            cls.window_names = kwargs["window_names"]


