from context.domains import Dataset
from context.models import Model
from icecream import ic
import matplotlib.pyplot as plt
import seaborn as sns

class SpaceShipTemplates(object):
    dataset = Dataset()
    model = Model()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위5행: {this.head()}')
        ic(f'트레인의 하위5행: {this.tail()}')

    def visualize(self) -> None:
        this = self.entity
        self.draw_transported(this)

    @staticmethod
    def draw_transported(this) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Transported'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.이동자 vs 1.이동아닌자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.이동자 vs 1.이동아닌자')
        sns.countplot('Transported', data=this, ax=ax[1])
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_transported.png')

