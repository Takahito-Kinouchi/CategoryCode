from __future__ import annotations
from category import Category


class CategoryList:

    def __init__(self, categories: list[Category]) -> None:
        self.categories = categories

    def filter_by_depth(self, depth: int) -> CategoryList:
        filtered = [
            category for category in self.categories
            if category.depth() == depth
            ]
        return filtered

    def to_list(self) -> list:
        return [
            self.category_to_dict(category)
            for category in self.filter_by_depth(1)
            ]

    def category_to_dict(self, category: Category) -> dict:
        category_dict = category.to_dict()
        children_list = [
            child for child in self.categories
            if category.is_parent_of(child)
            ]

        children_dict = [
            self.category_to_dict(child) for child in children_list
        ]

        category_dict['children'] = children_dict
        return category_dict


def test_factory() -> CategoryList:
    return CategoryList(
        [
            Category('a', 'a'),
            Category('ab', 'ab'),
            Category('ac', 'ac'),
            Category('abc', 'abc'),
            Category('b', 'b'),
            Category('bc', 'bc')
        ]
        )
