'''Simple Web Browser'''


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple Web Browser')
        self.layout = QVBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText('Enter URL and press Enter')
        self.url_bar.returnPressed.connect(self.load_url)
        self.layout.addWidget(self.url_bar)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        self.load_url('https://www.example.com')

        self.setLayout(self.layout)

    def load_url(self, url=None):
        if url is None:
            url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith("https://"):
            url = 'http://' + url
        self.web_view.setUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    app.exec()
