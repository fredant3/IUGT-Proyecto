from django.contrib.auth.models import Group, Permission


class Roles:
    def execute_old():
        Group.objects.get_or_create(name="admin")
        adminGroup = Group.objects.get(name="admin")
        permissionsAdmin = []

        for module in [
            # "users", TODO: Pendiente
            # ADMINISTRACION,
            "asignacion",
            "averia",
            "compra",
            "departamento",
            "articulo",
            "sede"
            # RRHH
            "cargo",
            "contrato",
            "cuenta",
            "dotacion",
            "educacion",
            "empleado",
            "familiares",
            "sueldoEmpleado",
            "tipoEmpleado",
            "tipoSueldo",
            # TECNOLOGIA
            "grupos",
            "usuarios",
        ]:
            # LOS PERMISOS
            list = Permission.objects.get(codename=f"listar_{module}")
            read = Permission.objects.get(codename=f"ver_{module}")
            add = Permission.objects.get(codename=f"agregar_{module}")
            change = Permission.objects.get(codename=f"editar_{module}")
            delete = Permission.objects.get(codename=f"eliminar_{module}")
            # excel = Permission.objects.get(codename=f"exel_{module}")

            Group.objects.get_or_create(name=f"{module} director")
            Group.objects.get_or_create(name=f"{module} coordinador")
            Group.objects.get_or_create(name=f"{module} supervisor")
            Group.objects.get_or_create(name=f"{module} analista")

            director = Group.objects.get(name=f"{module} director")
            permissionsDirector = []
            permissionsDirector.append(list.id)
            permissionsDirector.append(add.id)
            permissionsDirector.append(read.id)
            permissionsDirector.append(change.id)
            permissionsDirector.append(delete.id)
            # permissionsDirector.append(excel.id)
            director.permissions.set(permissionsDirector)

            gerente = Group.objects.get(name=f"{module} coordinador")
            permissionsGerente = []
            permissionsGerente.append(list.id)
            permissionsGerente.append(add.id)
            permissionsGerente.append(read.id)
            permissionsGerente.append(change.id)
            permissionsGerente.append(delete.id)
            # permissionsDirector.append(excel.id)
            gerente.permissions.set(permissionsGerente)

            supervisor = Group.objects.get(name=f"{module} supervisor")
            permissionsSupervisor = []
            permissionsSupervisor.append(list.id)
            permissionsSupervisor.append(add.id)
            permissionsSupervisor.append(read.id)
            permissionsGerente.append(change.id)
            supervisor.permissions.set(permissionsSupervisor)

            analista = Group.objects.get(name=f"{module} analista")
            permissionsAnalista = []
            permissionsAnalista.append(list.id)
            permissionsSupervisor.append(add.id)
            permissionsAnalista.append(read.id)
            analista.permissions.set(permissionsAnalista)

            permissionsAdmin.append(list.id)
            permissionsAdmin.append(read.id)
            permissionsAdmin.append(add.id)
            permissionsAdmin.append(change.id)
            permissionsAdmin.append(delete.id)

        adminGroup.permissions.set(permissionsAdmin)

        print(f"Grupo {adminGroup.name} creado exitosamente.")

    def execute():
        admin_group, _ = Group.objects.get_or_create(name="admin")

        areas_modulos = {
            "Administracion": [
                "asignacion",
                "averia",
                "compra",
                "departamento",
                "articulo",
                "sede",
            ],
        }

        permisos_por_rol = {
            "Director": ["listar", "ver", "agregar", "editar", "eliminar", "reporte"],
            "Coordinador": [
                "listar",
                "ver",
                "agregar",
                "editar",
                "eliminar",
                "reporte",
            ],
            "Supervisor": ["listar", "ver", "agregar", "editar", "reporte"],
            "Analista": ["listar", "ver", "reporte"],
        }

        admin_permissions = []

        for area, modulos in areas_modulos.items():
            director, _ = Group.objects.get_or_create(name=f"Director de {area}")
            coordinador, _ = Group.objects.get_or_create(name=f"Coordinador de {area}")
            supervisor, _ = Group.objects.get_or_create(name=f"Supervisor de {area}")
            analista, _ = Group.objects.get_or_create(name=f"Analista de {area}")

            for modulo in modulos:
                try:
                    available_permissions = {}
                    for perm_type in [
                        "listar",
                        "ver",
                        "agregar",
                        "editar",
                        "eliminar",
                        "reporte",
                    ]:
                        try:
                            perm = Permission.objects.get(
                                codename=f"{perm_type}_{modulo}"
                            )
                            available_permissions[perm_type] = perm
                            admin_permissions.append(perm.id)  # Agregar al admin
                        except Permission.DoesNotExist:
                            continue

                    for rol, permisos_necesarios in permisos_por_rol.items():
                        group = None
                        if rol == "Director":
                            group = director
                        elif rol == "Coordinador":
                            group = coordinador
                        elif rol == "Supervisor":
                            group = supervisor
                        elif rol == "Analista":
                            group = analista

                        for perm_type in permisos_necesarios:
                            if perm_type in available_permissions:
                                group.permissions.add(available_permissions[perm_type])

                except Exception as e:
                    print(f"Error procesando módulo {modulo}: {str(e)}")
                    continue

        admin_group.permissions.set(admin_permissions)

        print("Grupos y permisos creados exitosamente.")
