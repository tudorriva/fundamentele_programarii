class Fraction:
    def __init__(self, n, z):
        self.n = n
        self.z = z

    def extend(self, k):
        self.n = self.n * k

    def simplify(self, k):
        self.n = self.n//k
        self.z = self.z//k

    def