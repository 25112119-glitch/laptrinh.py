import json

class CanBo:
    def__init__(self, ho_ten, tuoi, 
                gioi_tinh, dia_chi):
        self.ho_ten   = ho_ten
        self.tuoi     = tuoi
        self.dia_chi  = dia_chi
        self.gioi_tinh= gioi_tinh
    
    def to_dict(self):
        return {
            "ho_ten":    self.ho_ten,
            "tuoi"  :    self.tuoi,
            "gioi_tinh":  self.gioi_tinh,
            "dia_chi":   self.dia_chi,
            "loai":   self.__class__.__name__,
        }
    
    @classmethod
    def from_dict(cls, d):
        return cls(d["ho_ten"], d["tuoi"],
                   d["gioi_tinh"], d["dia_chi"])