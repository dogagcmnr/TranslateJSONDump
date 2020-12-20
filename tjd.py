import json 
from googletrans import Translator

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

translator = Translator()

json_file = open('turkish.json', 'a') # You should set a specific file for your translations.
translate_block = Object()
dump_file = open('dump.txt','r')

for i in dump_file:
    result = translator.translate(i, dest='tr') # You can set a specific destination (dest) and source (src) in this line. Source is auto for this one.
    translate_block.translation = result.text
    translate_block.word = i
    print(translate_block.toJSON()) # This line is not necessary but its useful for watching over process.
    json_file.write(translate_block.toJSON())

json_file.close()
