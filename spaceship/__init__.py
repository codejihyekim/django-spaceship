from spaceship.templates import SpaceShipTemplates

if __name__ == '__main__':

    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print('### 1.템플릿 ###')
            templates = SpaceShipTemplates(fname='train.csv')
            templates.visualize()
            break
        if menu == '2':
            print('### 2. 전처리 ###')