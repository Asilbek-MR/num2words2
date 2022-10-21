from num2words import num2words
save = {1:"o'ndan",
        2:"yuzdan",
        3:"mingdan",
        4:"o'n mindan",
        5:"yuz mingdan",
        6:"bir milliondan",
        7:"on' milliondan",
        8:"yuz milliondan",
        9:"bir milliardan",
        10:"yuz milliardan",
        11:"bir trilliondan"}
def num2word(number):
    num = str(number)
    index = num.find(".")
    if index!=-1:
        ong = num[index+1:]
        p=len(ong)+1
        chap = num[:index]
        chap_ = num2words(int(chap),lang='uz')
        ong_ = num2words(int(ong),lang='uz')
        return chap_+" butun "+save[p]+" " + ong_
        
    else:
        return num2words(number,lang='uz')

print(num2word(1.7898554))


















