from context.domains import Dataset
import pandas as pd
class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dname = './data/'
        this.sname = './sava/'

    def new_model(self, fname):
        this = self.ds
        return pd.read_csv(f'{this.dname}{fname}')

    def get_sname(self):
        return self.ds.sname