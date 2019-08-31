from supreme import Supreme
import datetime

def main(category, name, color, size, checkoutDelay, url):
    if releaseType == 'R':
        supreme = Supreme(category, name, color, size, checkoutDelay)
        supreme.addToCart(supreme.restock(url))
        supreme.checkOut()
    else:
        supreme = Supreme(category, name, color, size, checkoutDelay)
        supreme.addToCart(supreme.search())
        supreme.checkOut()

if __name__ == '__main__':
    # Enter R for restock mode else leave blank
    releaseType = 'R'.upper()
    # Enter category for release mode else leave blank
    category = 'accessories'
    # Enter name for release mode else leave blank
    name = 'Supreme®/Hanes® Crew Socks (4 Pack)'
    # Enter color for release mode else leave blank
    color = 'Red'
    # Enter size for desired size else leave blank for O/S or random
    size = ''
    # Enter checkout delay to avoid ghost checkout or else enter None
    checkoutDelay = None

    # This will be prompt if restock mode is selected else ignore this
    url = input('Enter url: ').strip() if releaseType == 'R' else None

    # Don't make any changes here
    print(datetime.datetime.now().strftime('%x %X'), 'Starting the script')
    main(category, name, color, size, checkoutDelay, url) 
