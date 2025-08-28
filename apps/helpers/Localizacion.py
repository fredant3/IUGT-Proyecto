import json

with open("./venezuela.json", "r") as file:
    data = json.load(file)


def state():
    return sorted(
        [{"value": item["estado"], "label": item["estado"]} for item in data],
        key=lambda x: x["label"],
    )


def municipality(state_name):
    state_data = next((item for item in data if item["estado"] == state_name), None)
    if state_data:
        return sorted(
            [
                {"value": item["municipio"], "label": item["municipio"]}
                for item in state_data["municipios"]
            ],
            key=lambda x: x["label"],
        )
    return None


def parish(state_name, municipality_name):
    state_data = next((item for item in data if item["estado"] == state_name), None)
    if state_data:
        municipality_data = next(
            (
                item
                for item in state_data["municipios"]
                if item["municipio"] == municipality_name
            ),
            None,
        )
        if municipality_data:
            return sorted(
                [
                    {"value": parish, "label": parish}
                    for parish in municipality_data["parroquias"]
                ],
                key=lambda x: x["label"],
            )
    return None
