from helpers.CrudMixin import CrudService
from organizacion.normativas.repositories import NormativaRepository
from django.db.models import Q
import os
from django.conf import settings


class NormativaService(CrudService):
    def __init__(self):
        self.repository = NormativaRepository()

    def media(self, data, media):
        custom_folder = "normativas"
        if media["file"]:
            data["file"] = self.repository.media(media["file"], custom_folder)
        return data

    def remove_media(self, data):
        read = self.reader(data.id)
        file = read.file
        if file:
            try:
                file_path = os.path.join(settings.MEDIA_ROOT, file.name)
                if os.path.exists(file_path) and file_path.startswith(
                    settings.MEDIA_ROOT
                ):
                    self.repository.remove_media(file.name)
            except Exception as e:
                print(f"Error al eliminar archivo: {e}")

    def criteria(self, search, columns):
        query = Q()

        if search:
            query &= Q(name__icontains=search) | Q(progre__icontains=search)

        for col in columns:
            if col["name"] == "id":
                query = Q(id__icontains=col["search"])
            elif col["name"] == "name":
                query = Q(name__icontains=col["search"])
            elif col["name"] == "estado":
                query = Q(estado__icontains=col["search"])

        return query
