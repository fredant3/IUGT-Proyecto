from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ReglamentoRepository
import os
from django.conf import settings


class ReglamentoService(CrudService):
    def __init__(self):
        self.repository = ReglamentoRepository()

    def media(self, data, media):
        custom_folder = "reglamentos"
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

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(name__icontains=search) | Q(progre__icontains=search)

        return query
