import qrcode

img = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLScKE7H9G98OzTUSrUir9feDLZcCNWJMdgGdVWIbYvfkD8sRMA/viewform?usp=dialog")
img.save("universe_qr.png")
