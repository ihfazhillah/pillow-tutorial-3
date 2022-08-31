import csv
import re

from PIL import Image, ImageDraw, ImageFont


def wrap_text(words, font, max_width):
    lines = []
    current_line = ""

    for word in words:
        if not current_line:
            temp_line = word
        else:
            temp_line = " ".join([current_line, word])
        width = font.getbbox(temp_line)[2]  # x,y,x,y
        if width >= max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = temp_line

    lines.append(current_line)

    # lines
    return lines


def split_text(text, special_words):
    special_words_pattern = "|".join(special_words)
    separators = "[,.?!]?"
    text_pattern = f"(?P<result>({special_words_pattern}|[\w-]+){separators})"
    pattern = re.compile(text_pattern)

    final_texts = []
    for match in re.finditer(pattern, text):
        res = match.groupdict().get("result")
        if res:
            final_texts.append(res)

    return final_texts


def transform_value(original, destination):
    # dapatkan index tiap kata dari destination
    word_and_index = []
    for index, text in enumerate(destination):
        for word in text.split(" "):
            word_and_index.append((word, index))

    # siapkan final destination, list of the pair of text and list
    final_destination = [(text, []) for text in destination]

    # map original data ke final destination
    for (word, value), (word_dest, index) in zip(original, word_and_index):

        # index 0 adalah text, 1 adalah list value
        final_destination[index][1].append(value)

    return final_destination


def generate_bounding_boxes(canvas, font, coordinate, line, space_right):
    bboxes = []

    l_left, l_top, l_right, l_bottom = canvas.textbbox(coordinate, line, font=font, anchor="ra")

    x = l_left

    for word in line.split(" "):
        w_left, w_top, w_right, w_bottom = font.getbbox(word)
        bboxes.append((word, (w_left + x, l_top, w_right + x, l_bottom)))

        x += w_right + space_right
    return bboxes


def main():
    image = Image.new("RGB", (1080, 920), (100, 200, 150))
    canvas = ImageDraw.Draw(image)
    font = ImageFont.truetype("Raleway-VariableFont_wght.ttf", size=90)

    _, _, space_right, _ = font.getbbox(" ")

    text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
    lines = wrap_text(text.split(" "), font, image.width * 0.8)

    y = 100
    x = image.width - (image.width * 0.1)

    ascender, descender = font.getmetrics()

    bboxes = []
    for line in lines:
        canvas.text((x, y), line, font=font, fill="white", anchor="ra")
        bboxes += generate_bounding_boxes(canvas, font, (x, y), line, space_right)

        y += ascender + descender

    image.save("image-without-bboxes.png")

    for word, bbox in bboxes:
        canvas.rectangle(bbox, outline="pink")

    image.save("image-with-bboxes.png")

    save_bboxes(bboxes)


def save_bboxes(bboxes):
    with open("text-bboxes.csv", "w") as text:
        writer = csv.writer(text)
        writer.writerow(["word", "coordinates"])
        for word, bbox in bboxes:
            writer.writerow([word, ",".join([str(p) for p in bbox])])


if __name__ == '__main__':
    main()

