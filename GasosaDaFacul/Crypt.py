import hashlib as hl

class Crypt():
    @staticmethod
    def Encrypt(s):
        sb = s.encode("utf-8")
        sha = hl.sha256()

        sha.update(sb)
        hb = sha.digest()
        hs = "".join(format(b, "02x") for b in hb)

        return hs
