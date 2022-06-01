import json


context = []
def get_components(data):
    if data.get('components'):
        for i in data.get('components'):
            if i.get('input') == True:
                # if fields is required
                # if i.get('validate'):
                #     if i.get('validate').get('required') is True:
                context.append(i.get('key'))
            if i.get('components'):
                get_components(i)
            if i.get('columns'):
                for j in i.get('columns'):
                    get_components(j)
    return context


print(get_components(json.loads(open('data.json', 'r').read())))
