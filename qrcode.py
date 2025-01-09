import qrcode


async def make_qrcode(link: str, name_img: str = 'qrcode'):
    url = qrcode.make(link)
    file_path = name_img + ".jpg"  # Путь к файлу
    url.save(file_path)  # Сохраняем QR-код
    return file_path  # Возвращаем путь к файлу
