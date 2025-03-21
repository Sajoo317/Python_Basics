# desired output is '''Dear <|Name|>
#                       you are selected!
#                         <|Date|>
letter = '''Dear <|Name|>
you are selected!    
<|Date|>'''
print(letter.replace("<|Name|>", "Sajeel").replace("<|Date|>", "16th March"))