import json

def export_to_csv():
    with open("data.json") as f:
        list1 = []
        data = json.loads(f.read())
        temp = data[0]
        header_items = []
        get_header_items(header_items, temp)
        list1.append(header_items)
      
        for obj in data:
            d = []
            add_items_to_data(d, obj)
            list1.append(d)
        
        with open('output.csv', 'w') as output_file:
            for a in list1:
                output_file.write(','.join(map(str, a)) + "\r")


def get_header_items(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)


def add_items_to_data(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append("")
            add_items_to_data(items, obj[x])
        else:
            items.append(obj[x])

export_to_csv()
