from typing import Iterable


ROLE_PERMISSIONS = {
    "Admin": {"*"},
    "Production Manager": {"manufacturing", "planning", "mes", "inventory"},
    "Shop Floor Operator": {"mes"},
    "Quality Inspector": {"quality", "mes"},
    "Store / Inventory Manager": {"inventory", "manufacturing"},
    "Accounts / Finance": {"accounting"},
    "Sales": {"sales", "manufacturing"},
    "HR": {"hr"},
}


def has_access(role: str, module: str, permissions: Iterable[str] | None = None) -> bool:
    allowed = ROLE_PERMISSIONS.get(role, set())
    if "*" in allowed:
        return True
    if permissions:
        return any(permission in allowed for permission in permissions)
    return module in allowed
