from __future__ import annotations


class Category:

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name

    def is_parent_of(self, category: Category) -> bool:
        if self.depth() + 1 != category.depth():
            return False
        return category.code.startswith(self.code)

    def depth(self) -> int:
        return len(self.code)

    def to_dict(self) -> list:
        return {
            'code': self.code,
            'name': self.name
            }
