# from PIL import Image
# from flask import Flask
# import pyocr
# from flask import render_template

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


# tools = pyocr.get_available_tools()
# tool = tools[0]

# # print(tool)
# # print(tool.get_name())

# # img = Image.open("SpartaCamp英語.png")
# # img_ja = Image.open("スパルタキャンプ.png")
# # img2 = Image.open("IMG_3522.jpeg")
# # # img.show()

# # txt = tool.image_to_string(img, lang="eng", builder=pyocr.builders.TextBuilder())
# # txt1 = tool.image_to_string(img_ja, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
# # txt2 = tool.image_to_string(img2, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
# # print(txt2)

# if (__name__) == ("__main__"):
#     app.run(debug=True)
