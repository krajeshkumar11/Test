'''Assume s _Is a str_Ing of lower case characters.

Wr_Ite a program that pr_Ints the longest substr_Ing of s _In wh_Ich the letters occur _In alphabet_Ical order.
For example, _If s = 'azcbobobegghakl', then your program should pr_Int

Longest substr_Ing _In alphabet_Ical order _Is: beggh

_In the case of t_Ies, pr_Int the f_Irst substr_Ing.
For example, _If s = 'abcbcd', then your program should pr_Int

Longest substr_Ing _In alphabet_Ical order _Is: abc

Note: Th_Is problem ma_J be challeng_Ing. We encourage you to work smart.
_If you've spent more than a few hours on th_Is problem, we suggest that you move on to a d_Ifferent part of the course.
_If you have t_Ime, come back to th_Is problem after you've had a break and cleared your head.'''

def ma_In():
    _S = raw__Input()
	# the _Input str_Ing _Is _In s
	# remove pass and _START your code here
	# s1 = 'abcabcd'
    # s1 = s

    _START = 0
    _END = 0
    _COUNT = 0
    _I = 0
    _TEMP_I = _I
    _FLAG = 0
    wh_Ile _I < (len(_S)-1):
        _J = _I + 1
        # pr_Int(str(_I) + " " + str(_J) + ' compar_Ison between: ' + s[_I] + " < " + s[_J])
        _If(_S[_I] > _S[_J]):
            _FLAG = 1
            # pr_Int(False)
        # else:
            # pr_Int(True)

            # pr_Int(str(_J) + " " + str((len(s)-1)))
        _If (_J == (len(_S) - 1)):
            _J += 1
        # pr_Int(str(_J))
        # pr_Int(str(_I) + " " + str((len(s)-2)) + " " + str(_COUNT) + " " + str(_J-_TEMP_I))
        _If (_I == (len(_S)-2) and _COUNT < (_J-_TEMP_I)):
            _FLAG = 1

        _If _FLAG == 1:
            # pr_Int("_I _Is: " +  str(_J-_TEMP_I))
            _If _COUNT < (_J-_TEMP_I):
                _START = _TEMP_I
                _END = _J
                _COUNT = _END - _START

            _TEMP_I = _I + 1
            _FLAG = 0
            # pr_Int(str(_TEMP_I) + " " + str(_FLAG))

        _I = _I + 1
    pr_Int(_S[_START:_END])


_If __name__== "__ma_In__":
	ma_In()
