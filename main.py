import sys, os
import pandas as pd
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMessageBox
import design, inputDB, keysDB

listOfXls = pd.DataFrame(columns=['Name','Category','Country','Activated']) #Таблица всех файлов экселя
base = [] #Лист пандасов. Структура таблицы - из xls (решить, какой стандарт)

#Соответственно, вот тут и есть связь 1-1 по индексам

#Список категорий и стран
countries = []
categories = []

#Заметки того, что надо сделать
#1. Ситуация, при которой мы загружаем файл с некоторой категорией\страной,
# а после берём и удаляем их из списка. Придумать, как лучше обработать подобное.
#2. Кнопки удаления самих баз, редактирования параметров существующих
#3. Если надо - хитрость с форматом, чтобы не загружать случайно обычные xls

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)    
        self.addXlsBtn.clicked.connect(self.input_database)
        #self.set_item() #Для теста
        self.categoryBox.currentTextChanged.connect(self.currentTextChanged)
        self.countryBox.currentTextChanged.connect(self.currentTextChanged)
        self.listWidget.itemChanged.connect(self.itemSelectionChanged)
        self.save_bd.triggered.connect(self.save_xls)
        self.load_bd.triggered.connect(self.load_xls)
        self.create_bd.triggered.connect(self.clear_all)
        self.exit_action.triggered.connect(self.exit)


    def input_database(self):
        self.dialog = input_DB()
        #Блокируем сигналы, чтобы нормально заполнялись боксы после их изменений
        self.categoryBox.blockSignals(True) 
        self.countryBox.blockSignals(True) 

        if self.dialog.exec()==QtWidgets.QDialog.Accepted:
            self.update_boxes()
            self.update_list()
        self.categoryBox.blockSignals(False)
        self.countryBox.blockSignals(False)


        
    def load_xls(self):
        global base, listOfXls, countries, categories
        self.categoryBox.blockSignals(True) 
        self.countryBox.blockSignals(True)
        
        if not listOfXls.empty:
            self.clear_all()
        
        bd_path = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите БД",filter="*.xlsx")
        if bd_path[0]:
            bd_item = pd.ExcelFile(bd_path[0])
            listOfXls = bd_item.parse('info')
            categories = listOfXls.Category.unique().tolist()
            countries = listOfXls.Country.unique().tolist()
            categories = list(map(str, categories))
            countries = list(map(str, countries))
            for it in listOfXls.index:
                name = listOfXls.Name[it]
                new_base = bd_item.parse(name)
                base.append(new_base)
            self.update_list()
            self.update_boxes()

        self.categoryBox.blockSignals(False) 
        self.countryBox.blockSignals(False)
        
            
        
    def itemSelectionChanged(self,item):
        item_index = listOfXls.loc[listOfXls['Name'] == item.text()]
        item_index = item_index.index[0]
        if not item.checkState():
            listOfXls.iloc[item_index].Activated = False
        else:
            listOfXls.iloc[item_index].Activated = True



    def set_item(self,item):
        #Пока просто выставляет пустой элемент, переписать под заполнение
        #из класса input_DB

        #Каким образом - смотреть, что выбрано в категориях и делать срез
        #с пандаса и вставлять его поэлементно
        #Подумать на тему того, чтобы изначально был пункт "Все",
        #и как это красиво можно связать со структурами
        #(в плане редактирования, чтобы не удалить случайно)
        chkBoxItem = QtWidgets.QListWidgetItem(item)
        chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkBoxItem.setCheckState(QtCore.Qt.Checked)       
        self.listWidget.addItem(chkBoxItem)



    def update_boxes(self):
        #Функция, вызываемая при добавлении\изменении категориальных признаков
        #для обновления списков на главном окне
        self.categoryBox.clear()
        self.categoryBox.addItem("Все")

        for item in categories:
            self.categoryBox.addItem(item)
        
        self.countryBox.clear()
        self.countryBox.addItem("Все")
        for item in countries:
            self.countryBox.addItem(item)


    
    def update_list(self, *args):
        #Функция для вывода списка (по фильтрам)
        if args:
            db = args[0]
        else:
            db = listOfXls

        self.listWidget.clear()
        for item in range(len(db)):
            name = db.loc[item].Name
            self.set_item(name)
            
        #блок вывода всех элементов(!) выбранной базы
        #        for db in base:
        #            print(db.shape)
        #            print(db.shape[0])
        #            for item in range(1,db.shape[0]):
        #                name = db.loc[item]['Название']
        #                self.set_item(name)



    def currentTextChanged(self):
        #Переопределение функции выбранного элемента комбобокса
        #для заполнения срезами таблицы listofxls
        
        currentCategory = self.categoryBox.currentText()
        currentCountry = self.countryBox.currentText()

        tempdf = listOfXls #проверить насчёт копии

        if currentCategory != 'Все':
            tempdf = tempdf[tempdf.Category.str.contains(currentCategory)]
        if currentCountry != 'Все':
            tempdf = tempdf[tempdf.Country.str.contains(currentCountry)]
        tempdf = tempdf.reset_index()
        if not tempdf.empty:
            self.update_list(tempdf)
        else:
            self.listWidget.clear()
        #Нумерация остаётся как взяли (т.е. 2,5... вместо 0,1...). Норм?



    def save_xls(self):
        if base==[]:
            return
        #Сохраняет сами данные, без категорий. Придумать, как сохранять категорию\страну (в первую строку?)
        xls_result = QtWidgets.QFileDialog.getSaveFileName(self, "Сохраните файл:",filter="*.xlsx")
        if xls_result[0]:
            with pd.ExcelWriter(xls_result[0]) as writer:
                listOfXls.to_excel(writer, sheet_name='info', index=False)
                for table in range(len(base)):
                    table_name = listOfXls.iloc[table].Name
                    base[table].to_excel(writer, sheet_name=table_name, index=False)



    def clear_all(self):
        #Функция для создания новой сессии
        global listOfXls
        self.categoryBox.blockSignals(True) 
        self.countryBox.blockSignals(True)
        base.clear()
        listOfXls = listOfXls[0:0]
        countries.clear()
        categories.clear()
        self.update_boxes()
        self.update_list(listOfXls)
        self.categoryBox.blockSignals(False) 
        self.countryBox.blockSignals(False)



    def exit(self): #Без комментариев
        exit()




        
class input_DB(QtWidgets.QDialog, inputDB.Ui_InputDB_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.inpPathBtn.clicked.connect(self.import_xls)
        self.inpCategoryBtn.clicked.connect(self.open_keysDB)
        self.inpCountryBtn.clicked.connect(self.open_keysDB)

        self.inpAccept.clicked.connect(self.accept_changes)
        self.inpReject.clicked.connect(self.close)
    
        self.update_comboboxes()


        
    def import_xls(self):
        #Выбор xls из файловой системы через диалог,
        #установка пути и названия файла
        xls_item = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку",filter="*.xls *.xlsx")
        self.inpPath.setText(xls_item[0])
        self.inpName.setText(os.path.splitext(os.path.basename(xls_item[0]))[0])
        #Доступ к изменению имени файла (ход, чтобы гарантировано загрузить какой-либо файл)
        self.inpName.setEnabled(True)


        
    def open_keysDB(self,item):
        #Функция вызова окна редактирования свойств (категория\страна)
        self.sender_name = self.sender().objectName()
        self.keysWindow = keys_DB(self.sender_name)
        if self.keysWindow.exec()==QtWidgets.QDialog.Rejected:
            self.update_comboboxes()



    def update_comboboxes(self):
        #Обновляет допустимые значения в выпадающих листах
        #по категориям и странам
        self.inpCategory.clear()
        self.inpCountry.clear()
        for item in categories:
            self.inpCategory.addItem(item)
        for item in countries:
            self.inpCountry.addItem(item)



    def accept_changes(self):
        #Проверка на заполненность данных
        
        #дошить фишку проверки правильности xls файла по колонкам
        #Вопрос лишь в том, в какое место это сделать и как
        path = self.inpPath.text()
        name = self.inpName.text()
        category = self.inpCategory.currentText()
        country = self.inpCountry.currentText()

        if path == "" and name == "":
            pass
        elif name =="" or category == "" or country == "":
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не заполнены все необходимые поля", QMessageBox.Ok)
            return
        elif not listOfXls[listOfXls['Name'] == name].empty:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "База с таким именем уже существует", QMessageBox.Ok)
            return
        elif len(name)>32:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Слишком длинное имя базы (больше 32)", QMessageBox.Ok)
            return
        else:
            #Добавляем сами записи товара
            self.append_data(path)
            #Что именно тут: формируем лист [название, категория, страна, True]
            #True - поскольку всё по дефолту будет активировано(включено)
            listOfXls.loc[len(listOfXls)]=[name, category, country, True]
        self.accept()



    def append_data(self,adress):
        #По сути, это тестовая версия проверки файла,
        #если предположить, что наша таблица не строго зафиксирована в левом углу,
        #а болтается неизвестно где.
        #Поэтому мы её импортируем и начинаем проверять всё и вся.

        df = pd.read_excel(adress, index_col=0)
        df = df.dropna(how='all') #Удаляем Nan-строки
        if len(df.columns)>5:
            df = df.dropna(axis='columns',how='all')
        if df.index.name=='Номер' or df.iloc[0].name=='Номер':
            pass
        else:
            df.set_index(df.columns[0], inplace = True)
        if not (df.columns[0]=='Название') or (df.columns[0]=='Номер'):
            df.columns = df.iloc[0]
            df.index.name=None
            df = df.drop("Номер")
        if df.columns.name == None:
            df.columns.name = df.index.name
            df.index.name = None
        base.append(df)





class keys_DB(QtWidgets.QDialog, keysDB.Ui_ListControl):
    def __init__(self, argument):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.keysList.clear()
        self.keysAddBtn.clicked.connect(self.add_item)
        self.keysDeleteBtn.clicked.connect(self.delete_item)
        
        self.argument = argument
        self.initialize_baseSet()
        
        for item in self.baseSet:
            self.update_list()
              


    def initialize_baseSet(self):
        if self.argument == "inpCategoryBtn":
            self.baseSet = categories
        else:
            self.baseSet = countries



    def update_baseSet(self):
        global categories, countries
        if self.argument == "inpCategoryBtn":
            categories = sorted(self.baseSet)
            self.baseSet = categories
        else:
            countries = sorted(self.baseSet)
            self.baseSet = countries



    def add_item(self):
        newItem = self.keysInputEdit.text()
        self.keysInputEdit.clear()
        if newItem.strip()!='' and newItem not in self.baseSet:
            self.baseSet.append(newItem)
            self.update_baseSet()
            self.update_list()
        

        
    def update_list(self):
        self.keysList.clear()
        if self.baseSet:
            for item in self.baseSet:
                self.keysList.addItem(item)


                
    def delete_item(self):
        if self.keysList.count()>0:
            item = self.keysList.currentItem()
            index = self.keysList.currentIndex().row()
            if self.argument == "inpCategoryBtn":
                categories.pop(index)
            else:
                countries.pop(index)
            self.keysList.removeItemWidget(item)
            self.update_list()




            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()  
    

