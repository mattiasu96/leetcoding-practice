class WebPage:
    def __init__(self, nxt, prev, url):
        self.nxt = nxt
        self.prev = prev
        self.url = url


class BrowserHistory:
    def __init__(self, homepage: str):
        homepage_node = WebPage(None, None, homepage)
        self.head = homepage_node
        self.cur = self.head

    def visit(self, url: str) -> None:
        self.cur.nxt = WebPage(None, self.cur, url)
        self.cur = self.cur.nxt

    def back(self, steps: int) -> str:
        while steps != 0 and self.cur.prev is not None:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps != 0 and self.cur.nxt is not None:
            self.cur = self.cur.nxt
            steps -= 1
        return self.cur.url


homepage = "www.facebook.com"
url = "www.linkedin.com"

obj = BrowserHistory(homepage)
obj.visit(url)
param_2 = obj.back(1)
param_3 = obj.forward(1)
