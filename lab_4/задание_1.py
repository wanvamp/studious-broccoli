import json


def task() -> float:
    with open("input.json") as f:
        python_object = json.load(f)
    return round(sum(map(lambda x: x["score"]*x["weight"], python_object)), 3)


print(task())