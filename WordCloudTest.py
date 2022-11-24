from wordcloud import WordCloud
from matplotlib import pyplot
from translate import Translator
import pandas


CSV_FILE_PATH = "imdb_movies.csv"
TTF_FILE_PATH = "GaoDuanHeiXiuDing151105-1.ttf"
TRANSLATE = False

title_list = pandas.read_csv(CSV_FILE_PATH).sort_values(axis=0, by="Rating", ascending=False)["Title"].tolist()

if TRANSLATE:
    # 开始翻译

    # 初始化翻译列表
    translated_title_list = []

    # 设置尝试翻译的次数
    attempts = 20

    # 初始化翻译器
    translator = Translator(from_lang="EN-US", to_lang="ZH")

    for title in title_list:
        translated_title = translator.translate(title)
        print(attempts, title, translated_title)
        translated_title_list.append(translated_title)
        attempts -= 1
        if attempts <= 0:
            break

    text = "/".join(translated_title_list)
else:
    text = "/".join(title_list)

# 生成词云图片
image = WordCloud(background_color='white', font_path=TTF_FILE_PATH, width=1000, height=860, margin=2).generate(text)

pyplot.axis('off')
pyplot.imshow(image)
pyplot.show()



