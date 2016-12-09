class game_map:
    def __init__(self, i, j):
        self.Height = j
        self.Width = i
        self.Map = [[" " for x in range(i)] for y in range(j)]
        
    def At(self, x, y):
        return self.Map[y][x]
    
    def Set(self, x, y, item):
        self.Map[y][x] = item
        
    def Clear(self):
        self.Map = [[" " for x in range(self.Width)] for y in range(self.Height)]
        SetBorder()
        
    def SetBorder(self):
        #TOP/BOT
        for x in range(len(self.Map[0])):
            self.Set(x, 0, "-")
            self.Set(x, -1, "-")
        #LEFT/RIGHT
        for y in range(len(self.Map)):
            self.Set(0, y, "|")
            self.Set(len(self.Map[y]) - 1, y, "|")
        # (+) corners
        self.Set(0, 0, "+")
        self.Set(0, self.Height - 1, "+")
        self.Set(self.Width - 1, 0, "+")
        self.Set(self.Width - 1, self.Height - 1, "+")
            
    def Render(self):
        for y in range(len(self.Map)):
            b = ""
            for x in range(len(self.Map[y])):
                b = b + str(self.Map[y][x])
            print b

