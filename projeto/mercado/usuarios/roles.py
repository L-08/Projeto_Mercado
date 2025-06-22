from rolepermissions.roles import AbstractUserRole

class Vendedor(AbstractUserRole):
    available_permissions = {
        'criar_produtos': True,
        'ver_produtos': True,
        }

class Cliente(AbstractUserRole):
    available_permissions = {'ver_produtos':True}

