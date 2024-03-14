# pycodestyle

Voor de opdrachten in deze cursus wordt een style checker gebruikt: `pycodestyle`. Deze checkt of je code aan bepaalde style regels voldoet en zal feedback geven als er iets nog niet helemaal klopt. Je kan `pycodestyle` als volgt draaien:

    pycodestyle --select=E101,E112,E113,E115,E116,E117,E501,E502,W505,W291 --max-line-length=99 --max-doc-length=79`

Lange regel he? Dit is wat de geselecteerde errors en waarschuwingen betekenen:

* `E101` - indentation contains mixed spaces and tabs
* `E112` - expected an indented block
* `E113` - unexpected indentation
* `E115` - expected an indented block (comment)
* `E116` - unexpected indentation (comment)
* `E117` - over-indented
* `E501` - line too long
* `E502` - the backslash is redundant between brackets
* `W505` - doc line too long
* `W291` - trailing whitespace

Vervolgens geven `--max-line-length` en `--max-doc-length` de maximale regellengte aan: 99 tekens voor code, 79 voor comments.

> Draai `pycodestyle` zelf. Alleen op die manier krijg je goede feedback over wat er nog niet klopt. De nakijkserver zal ook `pycodestyle` draaien, maar geeft maar weinig feedback.