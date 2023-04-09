import PIL.Image
import argparse, os


ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(
                    prog='Pic2ASCII',
                    description='Converts the images located in a specified directory to ASCII art',
                    epilog='Text at the bottom of help')


parser = argparse.ArgumentParser()
parser.add_argument('--src_path', type=dir_path, help="Already Existing directory of files to convert")
parser.add_argument('--dest_path', type=dir_path, help="Not-yet existing directory of destination of converted files")


def main():

    parsed_args = parser.parse_args()
    print(parsed_args.src_path)
    # print(len(parsed_args))
    # for arg in parsed_args:
    #     print(arg)
    # print('test')
    # path = input("Enter a pathname to an image:\n")

    # try:
    #     image = Image.open(path)
    # except:
    #     print(path, "is not a valid path.\n")


if __name__ == "__main__":
    main()

    

from PIL import Image

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def main():
    image = Image.open('image.jpg')
    # you can first resize the image if needed
    # image = image.resize((width, height))
    ascii_art = convert_to_ascii_art(image)
    save_as_text(ascii_art)


def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art


def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art):
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()


if __name__ == '__main__':
    main()