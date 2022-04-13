from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
def test_version():
    assert __version__ == '0.1.0'


def test_web_count():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_count(URL)
    expected = 5
    assert actual == expected

def test_Web_report():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(URL).strip().startswith("The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed]")
    expected = True
   
    assert actual == expected


def test_Web_report2():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(URL).strip().startswith('''The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed]

The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed]

over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed]

The Spanish had no intention to turn over Tenochtitlan to the Tlaxcalteca. While Tlaxcalteca troops continued to help the Spaniards, and Tlaxcala received better treatment than other indigenous nations, the Spanish eventually disowned the treaty. Forty years after the conquest, the Tlaxcalteca had to pay the same tax as any other indigenous community.[citation needed]

During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed]''')
    expected = True
   
    assert actual == expected