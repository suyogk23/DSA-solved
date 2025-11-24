# solution by @suyogk23 GITHUB
# maintain a monotionic stack, monoStk and span, while the top in monoStk <= current price keep popping the stack and increasing the curSpan
# by adding the top element of span, and pop both the stacks
class StockSpanner:

    def __init__(self):
        self.monoStk = []
        self.span = []

    def next(self, price: int) -> int:
        curSpan = 1
        while (self.span and self.monoStk and self.monoStk[-1] <= price):
                curSpan += self.span[-1]
                self.monoStk.pop()
                self.span.pop()
        self.span.append(curSpan)
        self.monoStk.append(price)
        return curSpan



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
