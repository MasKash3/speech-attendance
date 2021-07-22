import os
import time


def deleteFile():
    if os.path.exists('excel/compliance_form.xls'):
        os.remove('excel/compliance_form.xls')
    else:
        print('\nPath currently non existent\nCreating path...')

    for i in range(6):
        sI = str(i)
        if os.path.exists('sounds/trans-' + sI + '.mp3'):
            os.remove('sounds/trans-' + sI + '.mp3')
        else:
            pass
