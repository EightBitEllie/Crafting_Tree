from typing import Dict, List

import attr

from crafting_method import CraftingMethod, Recipe
from item import Item


@attr.s(auto_attribs=True)
class Tree():
    recipes: List[Recipe] = attr.ib(factory=list)
    crafting_methods: List[CraftingMethod] = attr.ib(factory=list)
    items: Dict[str, Item] = attr.ib(factory=dict)

    def add_recipe(self, recipe: Recipe) -> None:
        # Add Recipe to recipies
        # for each item in inputs and outputs, check if we have it, and if not, add it
        pass
