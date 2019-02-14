from keyboard import inline_keyboard


def listRender(offset, renderList):
    number_text = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    number_data = ['/1', '/2', '/3', '/4', '/5']
    text_navi = ['⬅', '➡']
    data_navi = ['button_back', 'button_next']

    text = [[]]
    data = [[]]
    if offset != 0:
        text[0].append(text_navi[0])
        data[0].append(data_navi[0])
    for i in range(len(renderList)):
        text[0].append(number_text[i])
        data[0].append(number_data[i])
    if len(renderList) == 5:
        text[0].append(text_navi[1])
        data[0].append(data_navi[1])

    print(text)
    print(data)

    return inline_keyboard(text, data)
