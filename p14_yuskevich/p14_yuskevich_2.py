import json

with open("image_info_test-dev2017.json") as file:
    a = json.load(file)
    print('Кількість фотографій:', len(a['images']))
    print('Кількість категорій:', len(a['categories']))

    print('\nІнформація про фотографії ', '000000000001.jpg', ':')
    for image in a['images']:
        if image['file_name'] == '000000000001.jpg':
            print(image['coco_url'])
            print(image['height'])
            print(image['width'])
            print(image['id'])

    max_id = max([image['id'] for image in a['images']])
    for image in a['images']:
        if image['id'] == max_id:
            print('\n', image['file_name'])