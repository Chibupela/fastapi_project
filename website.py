from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image

put_html('<h1> Hurrrraaaa endlich Sommerferien </h1>')

gedicht = """Ich gratuliere alle mit diesem langerwartenen Zeit fur Schluler/ihnen, mein Rat klingt so:
             1.Vesuchen sie Freizeit vergebens nicht verbringen.
             2.Ernahren sie sich gesund, um sich gut zu fuhlen.
             3.Machen sie Notizen, welche gute Geschafte haben sie gemacht.
             4.Viel Spass und Gluck.
          """

put_text(gedicht)

sommer_ferien_plane = input_pw('Erganz bitte ihre Sommerferien Plane >>> ')
name_des_nutzers = input_pw('Schreib ihre Name >>> ')

put_html(f'<h3>{sommer_ferien_plane}</h3> <h5>{name_des_nutzers}</h5>')

img = open('huy.jfif', 'rb').read()
put_image(img, width='20000px')


