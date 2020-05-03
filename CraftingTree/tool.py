from typing import List
import attr

@attr.s(auto_attribs=True)
class Tool():
    name: str

    @classmethod
    def from_data(cls, data):
        if isinstance(data, str):
            return cls(name=data)
        return cls(name=data.get('name'))


@attr.s(auto_attribs=True)
class Modifier():

    usableIn: List[Tool]

