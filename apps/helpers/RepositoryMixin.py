from django.core.exceptions import ObjectDoesNotExist
import os
from django.conf import settings
from pathlib import Path


class Repository:
    def after_get_all(self, entities):
        return entities

    def getAll(self, select, orderBy, orderAsc):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy
        entities = self.entity.objects.all().order_by(order).values(*select)
        return self.after_get_all(entities)

    def getFilter(self, criteria, select="", orderBy="id", orderAsc="-"):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy
        entities = self.entity.objects.filter(criteria).order_by(order).values(*select)
        # entities = self.entity.objects.filter(criteria).order_by(order).only(*select)
        return self.after_get_all(entities)

    def getById(self, id, select=""):
        # entity = self.entity.objects.get(pk=id).values(*select)
        entity = self.entity.objects.get(pk=id)

        if entity is None:
            raise ObjectDoesNotExist(
                "No %s matches the given query." % self.entity.__name__
            )

        return entity

    def getEntity(self, criteria, select=""):
        entity = self.entity.objects.filter(criteria).only(*select).first()

        if entity is None:
            raise ObjectDoesNotExist(
                "No %s matches the given query." % self.entity.__name__
            )

        return entity

    def media(self, file, custom_folder):
        path = self.media_folder(file, custom_folder)
        self.seve_media(path, file)

        return path.replace(settings.MEDIA_ROOT, "").replace("\\", "/")

    def media_folder(self, file, custom_folder):
        file_extension = Path(file.name).suffix.lower()

        if file_extension in [".jpg", ".png", ".gif", ".bmp"]:
            folder = "images"
        elif file_extension == ".pdf":
            folder = "pdfs"
        elif file_extension in [".mp4", ".avi", ".mov", ".mkv"]:
            folder = "videos"
        else:
            raise ObjectDoesNotExist(
                "El archivo %s, tiene un formato no soportado: ." % file.name
            )

        return self.ensure_folder(folder, file, custom_folder)

    def ensure_folder(self, folder, file, custom_folder):
        if custom_folder:
            file_path = os.path.join(
                settings.MEDIA_ROOT, custom_folder, folder, file.name
            )
        else:
            file_path = os.path.join(settings.MEDIA_ROOT, folder, file.name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        return file_path

    def seve_media(self, path, file):
        with open(path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    def remove_media(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    def create(self, data):
        # data = {k: v for k, v in data.items() if k != "csrfmiddlewaretoken"}
        # entity = self.entity(**data)
        # entity.save()
        # return entity

        # 1. Filtrar campos ManyToMany y campos no existentes en el modelo
        m2m_data = {}
        valid_fields = [
            f.name for f in self.entity._meta.get_fields()
        ]  # Nombres de campos válidos

        # Extraer campos no válidos y M2M
        data_filtered = {}
        for key, value in data.items():
            if key in valid_fields:
                if key in [field.name for field in self.entity._meta.many_to_many]:
                    m2m_data[key] = value
                else:
                    data_filtered[key] = value

        # 2. Crear instancia base con campos válidos
        entity = self.entity.objects.create(**data_filtered)

        # 3. Asignar relaciones ManyToMany
        for field_name, values in m2m_data.items():
            getattr(entity, field_name).set(values)

        return entity

    def update(self, entity, payload):
        # Si payload es un diccionario (datos ya procesados)
        if isinstance(payload, dict):
            for field, value in payload.items():
                if hasattr(entity, field):
                    setattr(entity, field, value)
            entity.save()
            return entity

        # Si payload es un formulario (comportamiento original)
        m2m_fields = []
        regular_fields = []

        # Separar campos ManyToMany de campos regulares
        for field in payload.fields:
            if hasattr(entity, field):
                field_obj = entity._meta.get_field(field)
                if field_obj.many_to_many:
                    m2m_fields.append(field)
                else:
                    regular_fields.append(field)

        # Actualizar campos regulares
        for field in regular_fields:
            setattr(entity, field, payload.cleaned_data[field])

        # Guardar la entidad primero para tener un ID si es nueva
        entity.save()

        # Actualizar campos ManyToMany
        for field in m2m_fields:
            getattr(entity, field).set(payload.cleaned_data[field])

        return entity

    def delete(self, payload):
        return payload.delete()

    def destroy(self, payload):
        return payload.delete()

    class Meta:
        abstract = True
