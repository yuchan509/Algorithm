import re

def solution(files):
    file = [re.split('(\d+)', file) for file in files]
    file.sort(key=lambda x: (x[0].lower(), int(x[1])))

    ans = [''.join(f) for f in file]

    return ans


# Run.
'''
output : ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
'''