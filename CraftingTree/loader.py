import yaml
import os
from crafting_tree import Tree
from crafting_method import Recipe, CraftingMethod
from item import ItemStack
from tool import Tool

def load(game: str):
    with open(os.path.join('craftingLists', game + '.yaml')) as f:
        data = yaml.safe_load(f)

    tree = Tree()

    for r in data.get('recipes'):
        inputs = [ItemStack.from_data(i) for i in r.get('inputs', [])]
        outputs = [ItemStack.from_data(i) for i in r.get('outputs', [])]
        dependencies = r.get('dependencies', [])
        tools = [Tool.from_data(t) for t in r.get('tools', [])]
        recipe = Recipe(inputs, outputs, dependencies, tools)
        tree.add_recipe(recipe)
        for tool in tools:
            tree.crafting_methods.append(CraftingMethod(recipe, tool))

    print(tree)

if __name__ == "__main__":
    load('factorio')
