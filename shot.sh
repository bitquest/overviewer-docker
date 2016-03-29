python contrib/png-it.py -m 256 -z 4 -o /var/www/html/shot.png /var/www/html/mini
convert /var/www/html/shot.png -gravity center -crop 1920x1200+-64+512 -quality 95 -strip -interlace Plane /var/www/html/shot.jpg
