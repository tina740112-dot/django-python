class TaipeiBank:
    def __init__(self, balance=0):#初始化方法，預設帳戶餘額為0，建構方法/建構子/constructor
        self.balance = balance#屬性，帳戶餘額
    def print_balance(self):#方法，列印帳戶餘額
        print(f"帳戶餘額為{self.balance}")
        
t = TaipeiBank(2000)#建立物件，帳戶餘額為2000
t.print_balance()#呼叫方法，列印帳戶餘額