from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool)
# print(tool.get_name())

img = Image.open("SpartaCamp英語.png")
img_ja = Image.open("スパルタキャンプ.png")
img2 = Image.open("IMG_3521.jpeg")
# img.show()

# txt = tool.image_to_string(img, lang="eng", builder=pyocr.builders.TextBuilder())
# txt1 = tool.image_to_string(img_ja, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
txt2 = tool.image_to_string(img2, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
print(txt2)
