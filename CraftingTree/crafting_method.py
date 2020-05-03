import datetime
from typing import List, Set

import attr

from item import Item, ItemStack
from tool import Tool


@attr.s(auto_attribs=True)
class Recipe():
    items: List[ItemStack]
    results: List[ItemStack]
    dependancies: List[str]
    valid_tools: List[Tool]
    def get_ingredients(self) -> Set[Item]:
        ingredients: Set[Item]= set()
        for i in self.items:
            ingredients.add(i.item)
        return ingredients
    def get_result(self) -> Set[Item]:
        result: Set[Item]= set()
        for i in self.results:
            result.add(i.item)
        return result



@attr.s(auto_attribs=True)
class CraftingMethod():
    recipe: Recipe
    tool: Tool
    # time: datetime.timedelta
