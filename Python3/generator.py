import sys
def returnnum(number):
    number_list=[':zero: ', ':one: ', ':two: ', ':three: ', ':four: ', ':five: ', ':six: ', ':seven: ', ':eight: ', ':nine: ']
    return number_list[number]
def Emoji(text):
    emoji=''
    for letter in text:
        if letter.isalpha(): 
            if 65<=ord(letter)<=90 or 97<=ord(letter)<=122: 
                emoji+=':regional_indicator_'+letter.lower()+': '
            else: 
                emoji+=letter
        else: 
            try:
                if 0<=int(letter)<=9:
                    emoji+=returnnum(int(letter))
                else:
                    emoji+=letter
            except ValueError: 
                if letter==' ': 
                    emoji+='  '
                else:
                    emoji+=letter
    print(emoji)

text=input()
if text=='' or text=='help' or text=='usage':
    sys.stdout.write('type \'file\' to generate emoji from file')
elif text=='file':
    filename=input('input text file name to generate discord emoji : ')
    try:
        f=open(filename, 'r')
        for buff in f.readlines():
            Emoji(buff)
    except IOError:
        sys.stdout.write("cannot open file '%s'\n" % filename)
else:
    Emoji(text)
