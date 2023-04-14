from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
 
import json
 
app = QApplication([])

#2.Hafta
'''json'daki notlar'''
notes = {
    "Hoş geldiniz!" : {
        "metin" : "Bu dünyanın en iyi not alma uygulaması!",
        "etiketler" : ["iyilik", "talimat"]
    }
}
with open("notes_data.json", "w" ) as file:
    json.dump(notes, file)

#2.Hafta


'''Uygulama arayüzü'''
#uygulama penceresi parametreleri
notes_win = QWidget()
notes_win.setWindowTitle('Akıllı notlar')
notes_win.resize(900, 600)
 
#uygulama penceresi widget'ları
list_notes = QListWidget() #Liste için alan oluştur
list_notes_label = QLabel('Notların listesi') #Liste başlığı
 
button_note_create = QPushButton('Not oluştur') #"notun adını girin" alanlı bir pencere belirir
button_note_del = QPushButton('Notu sil')
button_note_save = QPushButton('Notu kaydet')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Etiketi giriniz...')
field_text = QTextEdit()
button_tag_add = QPushButton('Nota ekle')
button_tag_del = QPushButton('Nottan çıkar')
button_tag_search = QPushButton('Notları etikete göre ara')
list_tags = QListWidget()
list_tags_label = QLabel('Etiket listesi')
 
#anahat düzenine göre widget'ların konumu
layout_notes = QHBoxLayout() #genel yatay hizalama oluşturuldu.
col_1 = QVBoxLayout() #1. dikey hizalama 1. sütun oluşturuldu
col_1.addWidget(field_text) #metin alanı 1. sütuna yerleştirildi
 
col_2 = QVBoxLayout() #2. dikey hizalama 2. sütun oluşturuldu
col_2.addWidget(list_notes_label) #notların listesi etiketi 2. sütuna yerleştirildi
col_2.addWidget(list_notes) #not listesi alanı 2. sütuna yerleştirildi
row_1 = QHBoxLayout() #1. yatay hiza 1. satır oluşturuldu
row_1.addWidget(button_note_create) #not oluşturma butonu 1. satıra yerleştirildi
row_1.addWidget(button_note_del) #not silme butonu 1. satıra yerleştirildi
row_2 = QHBoxLayout() #2.satır oluşturuldu
row_2.addWidget(button_note_save) #not kaydetme butonu 2. satıra yerleştirildi
col_2.addLayout(row_1) # not oluşturma ve not silme butonlarının olduğu 1.satır 2.sütuna hizalandı 
col_2.addLayout(row_2) #not kaydetme butonunun olduğu 2.satır, 2.sütuna hizalandı
 
col_2.addWidget(list_tags_label) #etiket listesi etiketi 2. sütuna yerleştirild
col_2.addWidget(list_tags) #etiket listesi alanı 2. sütuna yerleştirildi
col_2.addWidget(field_tag) #etiketi giriniz alanı 2. sütuna yerleştirildi
row_3 = QHBoxLayout()  #3. satır oluşturuldu
row_3.addWidget(button_tag_add)  #nota ekle butonu 3. satıra yerleştirildi
row_3.addWidget(button_tag_del) #nottan çıkar butonu 3. satıra yerleştirildi
row_4 = QHBoxLayout() #4. satır oluşturuld
row_4.addWidget(button_tag_search) #notları etikete göre arama butonu 4. satıra yerleştirildi
 
col_2.addLayout(row_3)  #not ekle ve nottan çıkar butonlarının olduğu 3. satır, 2. sütuna hizalandı
col_2.addLayout(row_4) # notları etikete göre arama butonun olduğu 4. satır 2. sütuna hizalandı
#ekranı totelde 3 olarak düşünürsek bunun 2'si sol taraf 1'i sağ tarafı oluşturacak. bu şekilde:
layout_notes.addLayout(col_1, stretch = 2) #sütun 1'de yer alan metin alanı yatay hizalandı ve  2 büyüklüğünde
layout_notes.addLayout(col_2, stretch = 1) #sütun 2'de yer alan not, etiket alanları ve butonlar yatay hizalandı ve 1 büyüklüğünde
notes_win.setLayout(layout_notes)

#2.Hafta
'''Uygulama işlevselliği'''
def show_note():
    #nottan metni vurgulanan adıyla alır ve düzenle alanında görüntüleriz
    key = list_notes.selectedItems()[0].text() #not isimlerinin bulunduğu notlar listesinden seçili olan değerin metnini key değişkenine aktar
    print(key) #key değişkenini consol ekranda yazdır
    field_text.setText(notes[key]["metin"]) #not içeriklerinin bulunduğu field_text kısmını seçilen nota ait metinle değiştir
    list_tags.clear() #etiketler listesi kısmını temizle 
    list_tags.addItems(notes[key]["etiketler"]) #seçilen nota ait etiketleri etiketler listesinde göster

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Not ekle", "Notun adı: ") #note_name isminde kullanıcıdan veri alabileceğimiz bir metin girişi penceresi oluştur
    if ok and note_name != "": #eğer kullanıcı metin alanına değer girmişse ve ok butonuna tıklamışsa
        notes[note_name] = {"metin" : "", "etiketler" : []} #notes sözlüğünde girilen ada sahip metin ve etiket kısmı boş bir not oluştur
        list_notes.addItem(note_name) #kullanıcı tarafından girilen not ismini notlar listesine ekle
        #list_tags.addItems(notes[note_name]["etiketler"]) #girilen not ismine ait etiketleri etiketler listesine ekle
        print(notes) #notlar sözlüğünü consol ekrana yazdır

def save_note():
    if list_notes.selectedItems(): #eğer notlar listesinden bir değer seçiliyse 
        key = list_notes.selectedItems()[0].text() #seçili olan notun ismini key değikenine aktar
        notes[key]["metin"] = field_text.toPlainText() #field_text kısmına girilen metni seçili olan notun metin alanına al toPlainText fonksiyonu
        with open("notes_data.json", "w") as file: #json dosyasını yazmak için aç
            json.dump(notes, file, sort_keys=True, ensure_ascii=False) #json dosyasının içerisine file ve notes sözlüğündeki değerleri aktar
        print(notes) #notes sözlüğünü consolda yazdır
    else:
        print("Kaydedilecek not seçili değil!") #eğer notlar listesinden bir değer seçili değilse consola yaz

def del_note():
    if list_notes.selectedItems(): #eğer notlar listesinden bir değer seçiliyse 
        key = list_notes.selectedItems()[0].text() #seçili olan notun ismini key değikenine aktar
        del notes[key] #notlar sözlüğünden seçili olan ada sahip notu sil
        list_notes.clear() #notlar listesini temizle
        list_tags.clear() #not etiketleri listesini temizle
        field_text.clear() #not metni kısmını temizle
        list_notes.addItems(notes) #notlar listesini güncelledim silinen not çıktıktan sonra notları tekrar listeledim
        with open("notes_data.json", "w") as file: #json dosyasını yazmak için aç
            json.dump(notes, file, sort_keys=True, ensure_ascii=False) #json dosyasının içerisine file ve notes sözlüğündeki değerleri aktar
        print(notes) #notes sözlüğünü consolda yazdır
    else:
        print("Silinecek not seçili değil!") #eğer notlar listesinden bir değer seçili değilse consola yaz

#2.Hafta

#2.Hafta
'''Uygulamayı başlatma'''
#olay işlemeyi bağlama
list_notes.itemClicked.connect(show_note) #not isimlerinin bulunduğu notlar listesinden bir değerin üzerine tıklandığında show_not fonksiyonunu çalıştır
button_note_create.clicked.connect(add_note) #not ekle butonuna tıklanğında gerçekleşecek olan işlem
button_note_save.clicked.connect(save_note) #notu kaydet butonuna tıklanğında gerçekleşecek olan işlem
button_note_del.clicked.connect(del_note) #notu sil butonuna tıklanğında gerçekleşecek olan işlem

#2.Hafta

#uygulamayı başlatma 
notes_win.show()

#2.Hafta
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
#2.Hafta
app.exec_()
 
