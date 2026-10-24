def Change(Paid, Amount):
    Paid = float(Paid)
    Amount = float(Amount)
    Change = Paid - Amount

    Fifty = Change//50
    Fifty = f"£50 Notes: {int(Fifty)}"
    Change %= 50
    Twenty = Change//20
    Twenty = f"£20 Notes: {int(Twenty)}"
    Change %= 20
    Ten = Change//10
    Ten = f"£10 Notes: {int(Ten)}"
    Change %= 10
    Five = Change//5
    Five = f"£5 Notes: {int(Five)}"
    Change %= 5
    Two = Change//2
    Two = f"£2 Coin: {int(Two)}"
    Change %= 2
    One = Change//1
    One = f"£1 Coins: {int(One)}"
    Change %= 1
    FiftyP = Change//0.5
    FiftyP = f"50p Coins: {int(FiftyP)}"
    Change %= 0.5
    TwentyP = Change//0.2
    TwentyP = f"20p Coins: {int(TwentyP)}"
    Change %= 0.2
    TenP = Change//0.1
    TenP = f"10p Coins: {int(TenP)}"
    Change %= 0.1
    FiveP = Change//0.05
    FiveP = f"5p Coins: {int(FiveP)}"
    Change %= 0.05
    TwoP = Change//0.02
    TwoP = f"2p Coins: {int(TwoP)}"
    Change %= 0.02
    OneP = Change//0.01
    OneP = f"1p Coins: {int(OneP)}"

    Change = print(Fifty, Twenty, Ten, Five, Two, One, FiftyP, TwentyP, TenP, FiveP, TwoP, OneP, sep='\n')
    return Change 
        

        


        
        
