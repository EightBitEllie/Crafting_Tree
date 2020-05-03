import attr

@attr.s(auto_attribs=True)
class Item():

    name: str
    max_stack_size: int

@attr.s(auto_attribs=True)
class ItemStack():
    item: Item
    quantity: int

    @classmethod
    def from_data(cls, data):
        if isinstance(data, str):
            return cls(item=data, quantity=1)
        return cls(item=data.get('name'), quantity=data.get('count', 1))
