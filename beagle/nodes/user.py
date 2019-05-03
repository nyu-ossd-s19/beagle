from collections import defaultdict
from typing import DefaultDict, List, Optional

from beagle.nodes import Edge, Node

class Assign_Rights(Edge):
    __name__ = "Assign Rights To"

    # Still contemplating whether this should be in the edge
    rights_assigned: Optional[str]

    def __init__(self) -> None:
        super().__init__()


class User(Node):
    __name__ = "User"
    __color__ = "F79805"  # orange

    user_name: Optional[str]
    assigned_rights: DefaultDict["User", Assign_Rights]
    
    key_fields: List[str] = ["user_name", "assigned_rights"]

    def __init__(
        self,
        user_name: str = None,
    ) -> None:
        self.user_name = user_name
        self.assigned_rights = defaultdict(Assign_Rights)

    @property
    def edges(self) -> List[DefaultDict]:
        return [self.assigned_rights]

    @property
    def _display(self) -> str:
        return self.user_name or super()._display
