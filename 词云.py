import wordcloud
import jieba
txt = "中国航空发动机总公司（中国发动机巨头）、中国航空工业集团公司（中国主要军用飞机制造企业）、中国航天科工股份有限公司（中国最重要的战术导弹研制企业之一）、中国航天科技集团公司（中国最主要的运载火箭和战略导弹研制企业）、中国兵器工业集团有限公司（陆军重型装备研制企业）、中国兵器装备集团有限公司（陆军轻武器研制企业）、中国船舶重工股份有限公司（中国最重要的军用舰艇制造企业）、中国核工业集团公司（不解释）"
txt = jieba.lcut(txt)
txt = " ".join(txt)
print(txt)
w = wordcloud.WordCloud(background_color="red", max_words=20, font_path="C:\Windows\Fonts\simsun.ttc")
w.generate(txt)
w.to_file("d:\\123.png")