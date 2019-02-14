from PIL import Image
import zbarlight


def qrcode_scan(user_image):
    print("Началось сканирование изображения")
    result = None
    image = open(user_image, 'rb')
    image = Image.open(image)
    image.load()
    width = image.size[0]
    height = image.size[1]

    square = []
    if height != width:
        if height > width:
            x0 = 0
            y0 = (height - width) / 2
            x1 = width
            y1 = y0 + width
            height = width
        elif width > height:
            x0 = (width - height) / 2
            y0 = 0
            x1 = x0 + width
            y1 = width
            width = height
        square.append(x0)
        square.append(y0)
        square.append(x1)
        square.append(y1)
        image = image.crop(square)

    for x in range(width):
        for y in range(width):
            red, green, blue = image.getpixel((x, y))
            red = int(red * 1.5)
            red = min(255, max(0, red))
            green = int(green * 1.5)
            green = min(255, max(0, green))
            blue = int(blue * 1.5)
            blue = min(255, max(0, blue))
            image.putpixel((x, y), (red, green, blue))
    for x in range(width):
        for y in range(width):
            red, green, blue = image.getpixel((x, y))
            color = red + green + blue
            if (color > (((255 + 100) // 2) * 3)):
                red, green, blue = 255, 255, 255
            else:
                red, green, blue = 0, 0, 0
            image.putpixel((x, y), (red, green, blue))

    percent = 0

    while percent < 6:
        percent += 5
        new_size = width - width / 100 * percent
        x0 = y0 = (width - new_size) / 2
        x1 = y1 = x0 + new_size
        square = (x0, y0, x1, y1)
        cropped_image = image.crop(square)
        grade = 0
        while grade > -90:
            rotate_image = cropped_image.rotate(grade)
            codes = zbarlight.scan_codes(['qrcode'], rotate_image)
            if codes != None:
                result = codes[0]
                print("codes", codes)
                return result
            else:
                grade -= 1
        while grade > 90:
            rotate_image = cropped_image.rotate(grade)
            codes = zbarlight.scan_codes(['qrcode'], rotate_image)
            if codes != None:
                print("codes", codes)
                result = codes[0]
                return result
            else:
                grade += 1

    return result
