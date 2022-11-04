result = ''

for i in range(129):
    result += f"<div class='grid-item item animate-box' data-animate-effect='fadeIn'> \n \t <a href='images/image_{i}.jpg' class='image-popup'> \n \t\t <div class='img-wrap'> \n \t\t\t <img src='images/image_{i}.jpg' class='img-responsive'> \n \t\t </div> \n \t\t  \n \t </a> \n </div> \n "

print(result)



