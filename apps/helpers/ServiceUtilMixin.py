from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class ServiceUtilMixin:
    def change_key_create(self, fields, data):
        payload = {}

        for field, key in fields:
            if field not in data:
                payload[field] = data[key]

        return payload

    def change_key_update(self, fields, form_data):
        data = {}
        for model_field, form_field in fields:
            if form_field in form_data:
                data[model_field] = form_data[form_field]
        return data

    def relationship(self, payload, *arg, **kwargs):
        return payload

    def media(self, data, file):
        return data

    def remove_media(self, data):
        pass

    def before_create(self, data):
        return data

    def before_update(self, entity, data):
        pass

    def prepare_data(self, request, *arg, **kwargs):
        data = request.POST.copy()

        user = request.user
        if data.get("id") is None:
            data["created_by"] = user.username
        data["updated_by"] = user.username

        return self.relationship(data, *arg, **kwargs)

    def paginate(self, data, start, length, draw):
        entities = data[start : start + length]
        paginator = Paginator(entities, length)

        try:
            items = paginator.page(draw).object_list
        except PageNotAnInteger:
            items = paginator.page(draw).object_list
        except EmptyPage:
            items = paginator.page(paginator.num_pages).object_list
        return items

    def response(self, entities, start, length, draw):
        response = {}
        data = []
        payload = self.paginate(entities, start, length, draw)
        for item in payload:
            data.append(item)

        try:
            records_total = entities.count()
        except Exception:
            records_total = len(entities)

        response["draw"] = draw
        response["entities"] = data
        response["recordsTotal"] = records_total
        response["recordsFiltered"] = records_total
        return response

    class Meta:
        abstract = True
