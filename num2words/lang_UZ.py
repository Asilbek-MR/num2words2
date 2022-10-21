

from __future__ import division, print_function, unicode_literals

from . import lang_EU


class Num2Word_UZ(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            if n==9:
                self.cards[10**9]="millard"
            else:

                self.cards[10 ** n] =  word + "illion"

    def setup(self):
        super(Num2Word_UZ, self).setup()

        self.negword = "minus "
        self.pointword = "butun"
        self.exclude_title = ["and", "butun", "minus"]

        self.mid_numwords = [(1000, "ming"), (100, "yuz"),
                             (90, "to'qson"), (80, "sakson"), (70, "yetmish"),
                             (60, "oltimish"), (50, "ellik"), (40, "qriq"),
                             (30, "o'ttiz")]
        self.low_numwords = ["yigirma", "o'n to'qqiz", "o'n sakkiz", "o'n yetti",
                             "o'n olti", "o'n besh", "o'n to'rt", "o'n uch",
                             "o'n ikki", "o'n bir", "o'n", "to'qqiz", "sakkiz",
                             "yetti", "olti", "besh", "to'rt", "uch", "ikki",
                             "bir", "no'l"]
        self.ords = {"bir": "birinchi",
                     "ikki": "ikkinchi",
                     "uch": "uchinchi",
                     "to'rt": "to'rtinchi",
                     "besh": "beshinchi",
                     "olti": "oltinchi",
                     "yetti": "yettinchi",
                     "sakkiz": "sakkizinchi",
                     "to'qqiz": "to'qqizinchi",
                     "o'n": "o'ninchi",
                     "o'n bir": "o'n birinchi",
                     "o'n ikki": "o'n ikkinchi"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s, %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie"
            lastword += "th"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'BC' if not suffix else suffix
        high, low = (val // 100, val % 100)
        # If year is 00XX, X00X, or beyond 9999, go cardinal.
        if (high == 0
                or (high % 10 == 0 and low < 10)
                or high >= 100):
            valtext = self.to_cardinal(val)
        else:
            hightext = self.to_cardinal(high)
            if low == 0:
                lowtext = "yuz"
            elif low < 10:
                lowtext = "oh-%s" % self.to_cardinal(low)
            else:
                lowtext = self.to_cardinal(low)
            valtext = "%s %s" % (hightext, lowtext)
        return (valtext if not suffix
                else "%s %s" % (valtext, suffix))
