import json
from django.http import JsonResponse


class GetValueChoicesMixin:
    field_mappings = {}

    def _map_fields(self, data):
        mappings = {
            field: dict(choices) for field, choices in self.field_mappings.items()
        }

        if "entities" in data:
            for item in data["entities"]:
                for field, mapping in mappings.items():
                    item_value = str(item.get(field, ""))
                    item[field] = mapping.get(item_value, item_value)
        return data

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)
                data = self._map_fields(data)
                return JsonResponse(data, safe=False)
            except Exception as e:
                print(f"Error: {str(e)}")
        return response
