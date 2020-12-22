import sys
import os
import copy
import pandas as pd
import numpy as np
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAbstractItemView, QApplication, QDialog, QFileDialog, QHeaderView, QListWidgetItem, \
    QMainWindow, QMessageBox, QTableWidgetItem
from pulp import *
from docxtpl import DocxTemplate
from datetime import datetime

import design
import inputDB
import keysDB
import addElement

# Таблица всех файлов экселя
listOfXls = pd.DataFrame(columns=['Name', 'Category', 'Country', 'Activated'])
# Лист пандасов. Структура таблицы - из xls (решить, какой стандарт)
base = []
# Соответственно, вот тут и есть связь 1-1 по индексам

# Список категорий и стран
countries = []
categories = []

# Заметки того, что надо сделать
# 1. Счётчик на попытки подбора. Дабы не уходило в бесконечность, если решения нет
# 2. Окно редактирования параметров существующих баз (название, категория, страна)

# 3. Если надо - хитрость с форматом, чтобы не загружать случайно обычные xls
# 4. Договориться насчёт структуры таблиц относительно что надо и как называется
# и поменять в коде все наименования

# 5. Не фильтруется по категориям (проверить сигналы)

# 6. Какой-то ОЧЕНЬ странный баг, что когда добавляешь новую базу без элементов,
# он не отображает её. Хз, разбираться, копать.


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.baseInfo.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.addXlsBtn.clicked.connect(self.input_database)
        # self.set_item() #Для теста
        self.categoryBox.currentTextChanged.connect(self.current_text_changed)
        self.countryBox.currentTextChanged.connect(self.current_text_changed)
        self.BDBox.currentTextChanged.connect(self.show_chosen_bd)

        self.listWidget.itemChanged.connect(self.item_selection_changed)
        self.save_bd.triggered.connect(self.save_xls)
        self.load_bd.triggered.connect(self.load_xls)
        self.create_bd.triggered.connect(self.clear_all)
        self.exit_action.triggered.connect(self.exit)
        self.workBtn.clicked.connect(self.upd_result_table)
        self.printBtn.clicked.connect(self.print_specification)
        self.deleteItemBtn.clicked.connect(self.delete_item_from_base)
        self.deleteBaseBtn.clicked.connect(self.delete_base)
        self.addItemBtn.clicked.connect(self.add_new_element)
        self.changeItemBtn.clicked.connect(self.change_item)

        self.baseInfo.cellClicked.connect(self.signal_delete)

        self.ru_lang.toggled.connect(self.change_language_in_table)
        # Уточнить необходимость наличия (если краши - удалить)
        self.dialog = None

    def change_language_in_table(self):
        self.changeItemBtn.setEnabled(False)
        self.deleteItemBtn.setEnabled(False)
        if self.baseInfo.rowCount() > 0:
            self.show_chosen_bd()
        return

    def change_item(self):
        index_base = self.BDBox.currentIndex()
        index_row = self.baseInfo.currentRow()
        temp = base[index_base-1].loc[index_row]
        t = temp.to_list()
        t.insert(0, index_base)
        t.insert(1, index_row)

        self.dialog = AddElementClass(t)

        if self.dialog.exec() == QDialog.Accepted:
            self.show_chosen_bd()
            self.changeItemBtn.setEnabled(False)
            self.deleteItemBtn.setEnabled(False)

    def add_new_element(self):
        index_base = self.BDBox.currentIndex()
        self.dialog = AddElementClass([index_base])

        if self.dialog.exec() == QDialog.Accepted:
            self.show_chosen_bd()

    def signal_delete(self):
        print(self.baseInfo.currentRow())
        print(self.BDBox.currentIndex())
        print('get signal')
        self.changeItemBtn.setEnabled(True)
        self.deleteItemBtn.setEnabled(True)

    def delete_base(self):
        global listOfXls
        msg = QMessageBox.question(self, 'Удаление базы',
                                   'Вы действительно хотите удалить эту базу?',
                                    QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            index_base = self.BDBox.currentIndex() - 1
            base.pop(index_base)
            listOfXls.drop(index_base, inplace=True)
            listOfXls = listOfXls.reset_index(drop=True)
            self.update_boxes()
            self.update_list()
            if len(base) == 0:
                self.workBtn.setEnabled(False)
                self.printBtn.setEnabled(False)

    def delete_item_from_base(self):
        index_base = self.BDBox.currentIndex()
        index_item = self.baseInfo.currentRow()
        if index_item >= 0:
            base[index_base-1] = base[index_base-1].drop(index=index_item).reset_index(drop=True)
            self.baseInfo.removeRow(index_item)
            if len(base[index_base-1]) == 0:
                self.changeItemBtn.setEnabled(False)
                self.deleteItemBtn.setEnabled(False)

    def show_chosen_bd(self):
        name = self.BDBox.currentText()
        index = listOfXls.loc[listOfXls['Name'] == name]
        if not index.empty:
            self.deleteBaseBtn.setEnabled(True)
            self.addItemBtn.setEnabled(True)
            self.langBox.setEnabled(True)
            self.baseInfo.setRowCount(0)
            self.baseInfo.clearContents()
            self.baseInfo.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            self.baseInfo.setColumnWidth(1, 80)
            self.baseInfo.setColumnWidth(2, 80)
            index = index.index[0]
            target = base[index]
            for i, row in target.iterrows():
                # row_name = row['Название']
                if self.ru_lang.isChecked():
                    row_name = row['Название RU']
                else:
                    row_name = row['Name EN']
                row_number = str(int(row['Количество']))

                row_price = str(row['цена $'])
                if "," in row_price:
                    row_price = str(row['цена $']).replace(',', '.')
                    row_price = float(row_price)
                    row_price = str(f"{row_price:.{2}f}")
                row_price = row_price.replace('.', ',')
                self.baseInfo.setRowCount(i+1)
                self.baseInfo.setItem(i, 0, QTableWidgetItem(row_name))
                self.baseInfo.setItem(i, 1, QTableWidgetItem(row_number))
                self.baseInfo.setItem(i, 2, QTableWidgetItem(row_price))
        else:
            self.baseInfo.setRowCount(0)
            self.changeItemBtn.setEnabled(False)
            self.deleteItemBtn.setEnabled(False)
            self.deleteBaseBtn.setEnabled(False)
            self.addItemBtn.setEnabled(False)

    def upd_result_table(self):
        """
        В чём суть: сначала формируем общий фрейм, откуда брать вырезку.
        Вырезка берётся как df.sample(n=count), count = число позиций
        Соответственно, берем только те, которые "включены"
        И, наверное, добавляется столбец с индексом/названием, чтобы потом
        взять и изменить количество при необходимости в исходном месте

        Сразу же: надо сделать так, чтобы нельзя было запросить позиций
        больше, чем есть в проге. То есть, сейчас лимит 20, а пускай у нас
        лежит 5 позиций. И чтобы не было такого, мол max = размер если меньше 20.

        """
        activated = listOfXls[listOfXls.Activated.astype(str).str.contains('True')]
        self.result_label.setText("")
        finish_alg = False
        while not finish_alg:
            full_list = base[0].copy()
            full_list = full_list[0:0]
            for it in activated.index:
                full_list = pd.concat([full_list, base[it]]).copy()

            count = int(self.positions.text())
            print(count)
            # print(full_list.sample(n = count))
            self.resultTable.setRowCount(0)

            full_list = full_list.sample(n=count)
            # Возможно, индексы надо и сохранить, но тут хз
            full_list = full_list.reset_index()

            # А тут идёт блок расчётов, потому что заполнять нужно с итогом

            nums = self.algo(full_list)
            if nums:
                for i, row in full_list.iterrows():
                    print(i, row)
                    # bug сделать общее название (сложить строки ру\енг + слеш между ними)
                    row_name = row['Название RU'] + '/' + row['Name EN']
                    row_number = str(int(nums[i]))

                    row_price = str('%.2f' % row['цена $'])

                    total = row['цена $']*int(nums[i])
                    total = ('%.2f' % total)
                    row_total = str(total)

                    self.resultTable.setRowCount(self.resultTable.rowCount() + 1)
                    self.resultTable.setItem(i, 0, QTableWidgetItem(row_name))
                    self.resultTable.setItem(i, 1, QTableWidgetItem(row_number))
                    self.resultTable.setItem(i, 2, QTableWidgetItem(row_price))
                    self.resultTable.setItem(i, 3, QTableWidgetItem(row_total))
                finish_alg = True

    def algo(self, df):
        # bug скорее всего, достаточно заменить название на RU, роли не играет же?
        df['Итог'] = 1

        sum_res = self.maxValue.text()
        sum_res = float(sum_res.replace(",", "."))

        for item in range(len(df['цена $'])):
            if ',' in str(df['цена $'].iloc[item]):
                df['цена $'].iloc[item] = str(df['цена $'].iloc[item]).replace(',', '.')
        df['цена $'] = df['цена $'].astype(float)
        df['Количество'] = df['Количество'].astype(int)
        items_ratio = 3.5  # Допустимое отношение максимального кол-ва элементов к минимальному
        price_ratio = 0.01  # Допустимое различие между заданной и полученной суммой

        finish = True
        max_item = sys.maxsize
        max_name = None

        # Проверка на достижимость суммы выбранным поддатасетом?
        df['total'] = df['Количество'] * df['цена $']
        agg = df['total'].aggregate(np.sum)
        if agg < sum_res:
            print("Ne, dont work")  # Соответственно, вопрос к обработке
            return

        agg = df['цена $'].aggregate(np.sum)
        if agg > sum_res:
            print("Always too much")
            return

        prob = LpProblem('Sell', LpMaximize)  # Objective function

        if self.ru_lang.isChecked():
            inv_items = list(df['Название RU'])  # Variable name
        else:
            inv_items = list(df['Name EN'])
        inv_items.sort()

        items = dict(zip(inv_items, df['Количество']))  # Function
        prices = dict(zip(inv_items, df['цена $']))

        inv_vars = LpVariable.dicts('Var', inv_items, lowBound=1, cat='Integer')

        prob += lpSum([prices[i] * inv_vars[i] for i in inv_items])
        prob += lpSum([prices[i] * inv_vars[i] for i in inv_items]) <= sum_res, 'Общая функция'

        for val in items:
            prob += inv_vars[val] <= items[val], val+' Demand'

        # values_check = [None,None]
        values_list = []
        old_values = None
        while finish:
            if max_name:
                prob += inv_vars[max_name] <= max_item

            prob.solve()
            values_list = []

            print('The optimal answer\n'+'-'*70)
            for v in prob.variables():
                item = v.varValue
                if item > 0:
                    values_list.append(item)

            if len(values_list) < len(inv_items):
                '''
                Причина, почему просто вернуть:
                Можно было бы обработать, но продавать одновременно одни и те же
                позиции, но с разными ценами/кол-вом - бред. Поэтому просто
                вернуть и не обращать внимания.
                '''
                print("баг с одинаковыми названиями")
                return

            max_item = max(values_list) - 1
            balance = float(max_item / min(values_list))
            max_name = inv_items[values_list.index(max(values_list))]
            print(values_list, max_item, max_name)

            t = list(prices.values())

            if len(values_list) == len(t):
                price_res = [t[i] * values_list[i] for i in range(len(t))]
                price_res = sum(price_res)

            else:
                # В настройках функции стоит, что минимум должен быть один элемент.
                # Если уже меньше, чем нужно - то значит 100% ошибка. Значит выходим.
                print("Обыграть перевызов функции с новым датасетом")
                return

            if old_values == values_list:
                '''
                Тут два варианта развития событий:
                1. Утыкаемся в невозможность на второй итерации. Во времени
                не теряем, так что можно и вывести результаты.
                2. Важнее, но маловероятнее - если долго считаем и упираемся.
                Обидно терять прогресс, лучше вывести что получилось.
                '''
                print("Stop NOW")
                if price_res < sum_res:
                    finish = False
                else:
                    return

            self.result_label.setText(str(price_res))
            curr_price_ratio = (sum_res - price_res) / sum_res
            if balance <= items_ratio and  curr_price_ratio <= price_ratio:
                finish = False

            old_values = values_list

        print("Ответ:") # пока что, для отладки
        for i in range(len(values_list)):
            print(inv_items[i], ":, ", values_list[i])

        return values_list

    def print_specification(self):

        doc = DocxTemplate("spec_template.docx")
        date = datetime.today().strftime('%d.%m.%Y')
        tbl_contents = []

        num_rows = self.resultTable.rowCount()
        for i in range(num_rows):
            label = i+1
            name = self.resultTable.item(i, 0).text()
            piece = "шт/ рс"
            nums = self.resultTable.item(i, 1).text()
            price = self.resultTable.item(i, 2).text()
            total = self.resultTable.item(i, 3).text()
            tbl_contents.append({'label': label, 'cols': [name, piece, nums, price, total]})

        total_price = ('%.2f' % float(self.result_label.text()))
        context = {'date': date,
                   'total_price': total_price,
                   'tbl_contents': tbl_contents}
        doc.render(context)

        doc_result = QFileDialog.getSaveFileName(self, "Сохраните файл:", filter="*.docx")
        if doc_result[0]:
            doc.save(doc_result[0])

    def input_database(self):
        self.dialog = InputDBClass()
        # Блокируем сигналы, чтобы нормально заполнялись боксы после их изменений
        self.categoryBox.blockSignals(True)
        self.countryBox.blockSignals(True)

        if self.dialog.exec() == QDialog.Accepted:
            self.update_boxes()
            self.update_list()
            self.BDBox.setEnabled(True)
            self.current_text_changed()
            # self.update_bd_list()

        self.categoryBox.blockSignals(False)
        self.countryBox.blockSignals(False)

    def load_xls(self):
        global base, listOfXls, countries, categories
        self.categoryBox.blockSignals(True)
        self.countryBox.blockSignals(True)

        bd_path = QFileDialog.getOpenFileName(self, "Выберите БД", filter="*.xlsx")
        if bd_path[0]:
            if not listOfXls.empty:
                self.clear_all()
            bd_item = pd.ExcelFile(bd_path[0], engine='openpyxl')
            listOfXls = pd.concat([listOfXls, bd_item.parse('info')]).copy()

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
            self.BDBox.setEnabled(True)
            self.workBtn.setEnabled(True)
            self.printBtn.setEnabled(True)
            self.langBox.setEnabled(True)
            self.current_text_changed()

        self.categoryBox.blockSignals(False)
        self.countryBox.blockSignals(False)

    def item_selection_changed(self, item):
        # Изменение состояния "включения" в базе (галочки в листбоксе)
        item_index = listOfXls.loc[listOfXls['Name'] == item.text()]
        item_index = item_index.index[0]

        if not item.checkState():
            listOfXls['Activated'].iloc[item_index] = False
        else:
            listOfXls['Activated'].iloc[item_index] = True

    def set_item(self, item):
        # Пока просто выставляет пустой элемент, переписать под заполнение
        # из класса InputDBClass

        # Каким образом - смотреть, что выбрано в категориях и делать срез
        # с пандаса и вставлять его поэлементно
        # Подумать на тему того, чтобы изначально был пункт "Все",
        # и как это красиво можно связать со структурами
        # (в плане редактирования, чтобы не удалить случайно)
        checkbox_item = QListWidgetItem(item)
        checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        checkbox_item.setCheckState(Qt.Checked)
        self.listWidget.addItem(checkbox_item)

    def update_boxes(self):
        # Функция, вызываемая при добавлении\изменении категориальных признаков
        # для обновления списков на главном окне
        self.categoryBox.clear()
        self.categoryBox.addItem("Все")

        for item in categories:
            self.categoryBox.addItem(item)

        self.countryBox.clear()
        self.countryBox.addItem("Все")
        for item in countries:
            self.countryBox.addItem(item)

    def update_list(self, *args):
        # Функция для вывода списка (по фильтрам)
        if args:
            db = args[0]
        else:
            db = listOfXls

        self.listWidget.clear()
        for item in range(len(db)):
            name = db.loc[item].Name
            self.set_item(name)

    def current_text_changed(self):
        # Переопределение функции выбранного элемента комбобокса
        # для заполнения срезами таблицы listOfXls

        current_category = self.categoryBox.currentText()
        current_country = self.countryBox.currentText()

        temp_df = listOfXls  # проверить насчёт копии

        if current_category != 'Все':
            temp_df = temp_df[temp_df.Category.astype(str).str.contains(current_category)]
        if current_country != 'Все':
            temp_df = temp_df[temp_df.Country.astype(str).str.contains(current_country)]
        temp_df = temp_df.reset_index()
        if not temp_df.empty:
            self.update_list(temp_df)
        else:
            self.listWidget.clear()

        self.update_bd_list(temp_df)
        # Нумерация остаётся как взяли (т.е. 2,5... вместо 0,1...). Норм?

    def update_bd_list(self, df):
        # Функция для обновления списка баз в комбобоксе BDBox (самый правый)
        self.categoryBox.blockSignals(False)

        self.BDBox.clear()
        self.BDBox.addItem("Выберите базу...")
        name = df['Name']
        if not name.empty:
            self.BDBox.setEnabled(True)
            for item in name:
                self.BDBox.addItem(item)
        else:
            self.BDBox.setEnabled(False)
        self.categoryBox.blockSignals(True)

    def save_xls(self):
        if not base:  # base = []
            return
        xls_result = QFileDialog.getSaveFileName(self, "Сохраните файл:", filter="*.xlsx")
        if xls_result[0]:
            with pd.ExcelWriter(xls_result[0]) as writer:
                listOfXls.to_excel(writer, sheet_name='info', index=False)
                for table in range(len(base)):
                    table_name = listOfXls.iloc[table].Name
                    base[table].to_excel(writer, sheet_name=table_name, index=False)

    def clear_all(self):
        # Функция для создания новой сессии
        global listOfXls
        self.categoryBox.blockSignals(True)
        self.countryBox.blockSignals(True)
        self.BDBox.blockSignals(True)

        if len(base) > 0:
            msg = QMessageBox.question(self, "Новая сессия",
                                             "Вы действительно хотите начать работу с новой базой?",
                                             QMessageBox.Yes | QMessageBox.No)

            if msg == QMessageBox.No:
                self.categoryBox.blockSignals(False)
                self.countryBox.blockSignals(False)
                self.BDBox.blockSignals(False)
                return

        base.clear()
        listOfXls = listOfXls[0:0]
        countries.clear()
        categories.clear()
        self.update_boxes()
        self.update_list(listOfXls)
        self.categoryBox.blockSignals(False)
        self.countryBox.blockSignals(False)
        self.BDBox.setEnabled(False)
        self.BDBox.blockSignals(False)

        self.workBtn.setEnabled(False)
        self.printBtn.setEnabled(False)
        self.printBtn.setEnabled(False)
        self.deleteBaseBtn.setEnabled(False)
        self.addItemBtn.setEnabled(False)
        self.changeItemBtn.setEnabled(False)
        self.deleteItemBtn.setEnabled(False)
        self.langBox.setEnabled(False)
        self.baseInfo.setRowCount(0)

        self.resultTable.setRowCount(0)
        self.positions.setValue(1)
        self.maxValue.setValue(1.00)
        self.result_label.setText("")
    def exit(self):  # Без комментариев
        exit()


class InputDBClass(QDialog, inputDB.Ui_InputDB_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.inpPathBtn.clicked.connect(self.import_xls)
        self.inpCategoryBtn.clicked.connect(self.open_keys_db)
        self.inpCountryBtn.clicked.connect(self.open_keys_db)

        self.inpAccept.clicked.connect(self.accept_changes)
        self.inpReject.clicked.connect(self.close)

        self.update_comboboxes()

    def import_xls(self):
        # Выбор xls из файловой системы через диалог,
        # установка пути и названия файла
        xls_item = QFileDialog.getOpenFileName(self, "Выберите папку", filter="*.xls *.xlsx")
        self.inpPath.setText(xls_item[0])
        self.inpName.setText(os.path.splitext(os.path.basename(xls_item[0]))[0])
        # Доступ к изменению имени файла (ход, чтобы гарантировано загрузить какой-либо файл)
        self.inpName.setEnabled(True)

    def open_keys_db(self, item):
        # Функция вызова окна редактирования свойств (категория\страна)
        # self.sender_name = self.sender().objectName()
        sender_name = self.sender().objectName()
        # self.keysWindow = KeysDBClass(self.sender_name)
        keys_window = KeysDBClass(sender_name)
        if keys_window.exec() == QDialog.Rejected:
            self.update_comboboxes()

    def update_comboboxes(self):
        # Обновляет допустимые значения в выпадающих листах
        # по категориям и странам
        self.inpCategory.clear()
        self.inpCountry.clear()
        for item in categories:
            self.inpCategory.addItem(item)
        for item in countries:
            self.inpCountry.addItem(item)

    def accept_changes(self):
        # Проверка на заполненность данных

        # дошить фишку проверки правильности xls файла по колонкам
        # Вопрос лишь в том, в какое место это сделать и как
        path = self.inpPath.text()
        name = self.inpName.text()
        category = self.inpCategory.currentText()
        country = self.inpCountry.currentText()

        if path == "" and name == "":
            pass
        elif name == "" or category == "" or country == "":
            QMessageBox.warning(self, "Ошибка", "Не заполнены все необходимые поля", QMessageBox.Ok)
            return
        elif not listOfXls[listOfXls['Name'] == name].empty:
            QMessageBox.warning(self, "Ошибка", "База с таким именем уже существует", QMessageBox.Ok)
            return
        elif len(name) > 32:
            QMessageBox.warning(self, "Ошибка", "Слишком длинное имя базы (больше 32)", QMessageBox.Ok)
            return
        else:
            # Добавляем сами записи товара
            self.append_data(path)
            # Что именно тут: формируем лист [название, категория, страна, True]
            # True - поскольку всё по дефолту будет активировано(включено)
            listOfXls.loc[len(listOfXls)] = [name, category, country, True]

        self.accept()

    def split_languages(self, old_df):
        names = old_df['Название'].to_list()
        ru = []
        en = []
        for i in names:
            n = i.split('/')
            for j in range(len(n)):
                n[j] = n[j].strip()

            mid = int(len(n)/2)
            ru.append(' '.join(n[0:mid]).strip())
            en.append(' '.join(n[mid:]).strip())
        new_df = pd.DataFrame({'Название RU': ru, 'Name EN': en,
                               'Количество': old_df['Количество'], 'цена $': old_df['цена $']})
        return new_df

    def append_data(self, adress):
        # По сути, это тестовая версия проверки файла,
        # если предположить, что наша таблица не строго зафиксирована в левом углу,
        # а болтается неизвестно где.
        # Поэтому мы её импортируем и начинаем проверять всё и вся.

        # df = pd.read_excel(adress, index_col=0)
        # df = pd.ExcelFile.parse(adress, index_col=0,engine='openpyxl')
        df = pd.ExcelFile(adress, engine='openpyxl')
        df = df.parse(index_col=0, engine='openpyxl')

        df = df.iloc[:, 0:4]
        # df = df.dropna(how='all') #Удаляем Nan-строки
        # Вообще, задуматься об обработке таблицы, если слева пусто, но это потом может быть
        '''
        if len(df.columns) > 5:
            df = df.dropna(axis='columns',how='all')
        if df.index.name == 'Номер' or df.iloc[0].name == 'Номер':
            pass
        else:
            df.set_index(df.columns[0], inplace = True)
        if not (df.columns[0] == 'Название') or (df.columns[0] == 'Номер'):
            df.columns = df.iloc[0]
            df.index.name = None
            df = df.drop("Номер")
        if df.columns.name == None:
            df.columns.name = df.index.name
            df.index.name = None
        '''
        df = df.dropna(axis='rows', how='all')
        df['Количество'] = df['Количество'].fillna(0)
        df = self.split_languages(df)  # разбиваем название на русский и английский
        print(df)
        df = df.reset_index(drop=True)
        base.append(df)


class KeysDBClass(QDialog, keysDB.Ui_ListControl):
    def __init__(self, argument):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.keysList.clear()
        self.keysAddBtn.clicked.connect(self.add_item)
        self.keysDeleteBtn.clicked.connect(self.delete_item)

        self.argument = argument
        self.baseSet = []
        self.initialize_base_set()
        for _ in self.baseSet:
            self.update_list()

    def initialize_base_set(self):
        if self.argument == "inpCategoryBtn":
            self.baseSet = categories
        else:
            self.baseSet = countries

    def update_base_set(self):
        global categories, countries
        if self.argument == "inpCategoryBtn":
            categories = sorted(self.baseSet)
            self.baseSet = categories
        else:
            countries = sorted(self.baseSet)
            self.baseSet = countries

    def add_item(self):
        new_item = self.keysInputEdit.text()
        self.keysInputEdit.clear()
        if new_item.strip() != '' and new_item not in self.baseSet:
            self.baseSet.append(new_item)
            self.update_base_set()
            self.update_list()

    def update_list(self):
        self.keysList.clear()
        if self.baseSet:
            for item in self.baseSet:
                self.keysList.addItem(item)

    def delete_item(self):
        if self.keysList.count() > 0:
            item = self.keysList.currentItem()
            index = self.keysList.currentIndex().row()

            if self.argument == "inpCategoryBtn":
                cur_column = 'Category'
            else:
                cur_column = 'Country'

            contains_in_list = listOfXls[cur_column].to_list()
            contains_in_list = [str(x) for x in contains_in_list]

            item_bool = item.text() in contains_in_list
            if not item_bool:  # item_bool == False
                if cur_column == 'Category':
                    categories.pop(index)
                else:
                    countries.pop(index)
                self.keysList.removeItemWidget(item)
                self.update_list()
            else:
                QMessageBox.warning(self, "Невозможно удалить выбранный элемент",
                                    "Существует зависимость элемента внутри базы",
                                    QMessageBox.Ok)


class AddElementClass(QDialog, addElement.Ui_AddElement_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.OKBtn.clicked.connect(self.accept_new_item)
        self.cancelBtn.clicked.connect(self.reject_new_item)
        self.args = args[0]

        if len(self.args) > 1:
            self.row = self.args[1]
            self.nameRu.setText(self.args[2])
            self.nameEn.setText(self.args[3])  # Временно! (пока нет EN названия в таблице)
            self.num.setValue(self.args[4])
            self.args[4] = self.args[5].replace(',', '.')
            self.price.setValue(float(self.args[4]))

        self.index_base = self.args[0] - 1

    def accept_new_item(self):
        name_ru_val = self.nameRu.text()
        name_en_val = self.nameEn.text()
        count_val = self.num.value()
        price_val = self.price.value()
        price_val = str(f"{price_val:.{2}f}")
        price_val = price_val.replace('.', ',')
        if name_ru_val == '':
            QMessageBox.warning(self, "Ошибка", "Введите название на русском языке", QMessageBox.Ok)
            return
        elif name_en_val == '':
            QMessageBox.warning(self, "Ошибка", "Введите название на английском языке", QMessageBox.Ok)
            return
        elif price_val == 0.0:
            QMessageBox.warning(self, "Ошибка", "Нельзя задавать нулевую цену", QMessageBox.Ok)
            return
        else:
            new_val = [name_ru_val, name_en_val, count_val, price_val]

            if len(self.args) > 1:
                base[self.index_base].at[self.row] = new_val
            else:
                new_val = pd.DataFrame([new_val], columns=base[self.index_base].columns)
                base[self.index_base] = base[self.index_base].append(new_val, ignore_index=True)

            self.accept()

    def reject_new_item(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
