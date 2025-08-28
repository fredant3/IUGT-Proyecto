from django.core.exceptions import ValidationError

from .ServiceUtilMixin import ServiceUtilMixin


class CrudService(ServiceUtilMixin):
    select = ""

    def criteria(self, search, columns=[]):
        return search

    def queryset_to_dict(self, queryset, fields=None, use_model_json=False):
        if use_model_json:
            return [obj.toJSON() for obj in queryset]

        if fields is None:
            fields = [f.name for f in queryset.model._meta.fields]

        result = []
        for obj in queryset:
            item = {}
            for field in fields:
                if "__" in field:
                    parts = field.split("__")
                    current = obj
                    try:
                        for part in parts:
                            current = getattr(current, part)
                        item[field.replace("__", "_")] = current
                    except AttributeError:
                        item[field.replace("__", "_")] = None
                else:
                    value = getattr(obj, field)
                    item[field] = value() if callable(value) else value
            result.append(item)

        return result

    def getAll(
        self,
        draw,
        start,
        length,
        search=None,
        orderBy=None,
        orderAsc=None,
        select=(""),
        columns=[],
    ):
        select = select if select else self.select
        if search is None and len(columns) == 0:
            entities = self.repository.getAll(select, orderBy, orderAsc)
        else:
            search = self.criteria(search, columns)
            entities = self.repository.getFilter(search, select, orderBy, orderAsc)

        # entities = self.queryset_to_dict(entities, select)
        return self.response(entities, start, length, draw)

    def creator(self, form, request, *arg, **kwargs):
        data = self.prepare_data(request, *arg, **kwargs)
        if form.is_valid():
            form.clean()
            data = self.before_create(data)
            data = self.media(data, request.FILES)
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id, select=("")):
        return self.repository.getById(id, select)

    def updater(self, entity, payload):
        if payload.is_valid():
            payload.clean()
            self.before_update(entity, payload)
            return self.repository.update(entity, payload)
        raise ValidationError(payload.errors.as_json())

    def destroyer(self, payload):
        self.remove_media(payload)
        return self.repository.delete(payload)

    class Meta:
        abstract = True
