documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "namre": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299']
      }

def main():
  while True:
    function = input('Введите одну из команд команду:\n n - вывести имена всех владельцев документов\n p - вывести имя человека по номеру документа\n l - вывести список всех документов\n s - вывести номер полки, на котором находится искомый документ\n a - добавить новый документ в каталог и на полку\n d - удалить документ по его номеру из каталога и с полки\n m - перенести документ на другую полку\n as - добавить новую полку\n q - завершить программу\n')
    print()
    if function == 'p':
      find_people()
    elif function == 'l':
      documents_list()
    elif function == 's':
      shelf_of_document()
    elif function == 'a':
      add_document()
    elif function == 'd':
      delete_document()
    elif function == 'm':
      move_document()
    elif function == 'as':
      add_shelf()
    elif function == 'n':
      documents_name()
    elif function == 'q':
      break
    else:
      print('Неправильная команда, попробуйте еще раз.\n')

def documents_name():
    for i in documents:
        try:
            i['name']
        except KeyError:
            print(f'Документ типа {i["type"]} с номером {i["number"]} не имеет поля Name')
        else:
            print(i['name'])
    print()

def find_people():
  doc_number = input('Введите номер документа: ')
  print()
  count = 0
  for document in documents:
    if doc_number == document['number']:
        try:
            doc_name = document['name']
        except KeyError:
            print(f'Документ с номером {document["number"]} не имеет поля Name')
        else:
            doc_type = document['type']
            doc_name = document['name']
            print(f'{doc_name} имеет {doc_type} с номером {doc_number}\n')
    else:
      count +=1
  if count == len(documents):
    print(f'Человека, которому принадлежит документ с номером {doc_number}, нет в базе.\n')

def documents_list():
  for document in documents:
    for values in document.values():
      print(values, end = ' ')
    print()
  print()

def shelf_of_document():
  doc_number = input('Введите номер документа: ')
  print()
  count = 0
  for keys, values in directories.items():
    if doc_number in values:
      shelf = keys
    else:
      count +=1
  if count == len (directories):
    print(f'Документа с номером {doc_number} нет ни на одной из полок.\n')
  else:
    print(f'Документ с номером {doc_number} находится на полке номер {shelf}.\n')

def add_document():
  new_type = input('Введите тип документа: ')
  new_number = input('Введите номер документа: ')
  new_name = input('Введите имя и фамилию владельца: ')
  print()
  new_documet = {"type": new_type,
                  "number": new_number,
                  "name": new_name}
  documents.append(new_documet)
  shelf = input('Введите полку, на которой будет храниться документ: ')
  print()
  while int(shelf)-int(max(directories)) > 1:
    print(f'Доступна пустая полка номер {int(max(directories))+1}. Добавьте сначала ее, если хотите переместить на новую полку\n')
    shelf = input(f'Введите корректно номер полки от 1 до {int(max(directories))+1}, на которую хотите переместить: ')
    print()
  if shelf not in directories:
    directories[shelf] = []
  for shelfs in directories:
    if shelfs == shelf:
      directories[shelfs].append(new_number)
  for keys,values in directories.items():
    print(f'Полка №{keys}:')
    print(','.join(values))
    print()

def delete_document():
  del_number = input('Введите номер документа для удаления из каталога: ')
  print()
  count = 0
  for document in documents:
    if document['number'] == del_number:
      del_document = document
    else:
      count += 1
  if count == len(documents):
    print(f'Документа с номером {del_number} нет в каталоге.\n')
  else:
    documents.remove(del_document)
    for doc in documents:
      for keys,values in doc.items():
        print(keys, values)
      print('*'*20)
  count = 0
  for values in directories.values():
    if del_number in values:
      values.remove(del_number)
      for keys,values in directories.items():
        print(f'Полка №{keys}:')
        print(','.join(values))
        print()
    else:
      count +=1
  if count == len (directories):
    print(f'Документа с номером {del_number} нет ни на одной полке\n')

def move_document():
  doc_number = input('Введите номер документа, который хотите переместить: ')
  shelf_number = input('Введите номер полки, на которую хотите переместить: ')
  print()
  while int(shelf_number)-int(max(directories)) > 1:
    print(f'Доступна пустая полка номер {int(max(directories))+1}, добавьте сначала ее\n')
    shelf_number = input('Введите корректно номер полки от 1 до {int(max(directories))+1}, на которую хотите переместить: ')
    print()
  print()
  count = 0
  for values in directories.values():
    if doc_number in values:
      values.remove(doc_number)
    else:
      count +=1
  if count == len(directories):
    print(f'Документа с номером {doc_number} нет ни на одной полке\n')
  else:
    if shelf_number not in directories:
      directories[shelf_number] = []
    for shelfs in directories:
      if shelfs == shelf_number:
        directories[shelfs].append(doc_number)
    for keys,values in directories.items():
      print(f'Полка №{keys}:')
      print(','.join(values))
      print()

def add_shelf():
  new_shelf = input('Введите номер новой полки: ')
  print()
  while int(new_shelf)-int(max(directories)) > 1:
    print(f'Доступна пустая полка номер {int(max(directories))+1}, добавьте сначала ее\n')
    new_shelf = input('Введите корректно номер новой полки: ')
    print()
  if new_shelf not in directories:
    directories[new_shelf] = []
    for keys,values in directories.items():
      print(f'Полка №{keys}:')
      print(','.join(values))
  else:
    print(f'Полка с номером {new_shelf} уже существует\n')

main()

