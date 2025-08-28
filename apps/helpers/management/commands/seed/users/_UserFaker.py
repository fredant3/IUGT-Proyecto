from users.auth.models import User


class UserFaker:
    def admin_user():
        admin = User.objects.filter(dni="100").first()
        if admin is None:
            admin = User.objects.create(
                username="100",
                dni="100",
                password="pbkdf2_sha256$720000$Kz9kinsPg3DmSui1Piw5vy$P9/hiiwNCkYmFuXdDLrP8ZVXctTk7eU0odL2FIMmeEU=",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(
                f"Usuario {admin.username} con cédula de identidad {admin.username} creado como superusuario, su contraseña: admin"
            )

        return admin

    def director_user():
        director = User.objects.filter(dni="200").first()
        if director is None:
            director = User.objects.create(
                username="200",
                dni="200",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=True,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {director.username} con cédula de identidad {director.username} creado como usuario, su contraseña: other"
            )

        return director

    def gerente_user():
        gerente = User.objects.filter(dni="300").first()
        if gerente is None:
            gerente = User.objects.create(
                username="300",
                dni="300",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {gerente.username} con cédula de identidad {gerente.username} creado como usuario, su contraseña: other"
            )

        return gerente

    def supervisor_user():
        supervisor = User.objects.filter(dni="300").first()
        if supervisor is None:
            supervisor = User.objects.create(
                username="300",
                dni="300",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {supervisor.username} con cédula de identidad {supervisor.username} creado como usuario, su contraseña: other"
            )

        return supervisor

    def analista_user():
        analista = User.objects.filter(dni="300").first()
        if analista is None:
            analista = User.objects.create(
                username="300",
                dni="300",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {analista.username} con cédula de identidad {analista.username} creado como usuario, su contraseña: other"
            )

        return analista
