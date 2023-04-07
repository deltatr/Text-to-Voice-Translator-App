# Text-to-Voice-Translator-App

Merhabalar, Bu konumuzda sizlerle birlikte Python kullanarak Yazıdan Sese çevirme uygulaması yapacağız. Bu sistemi kullanabilmek için Google'nin geliştirmiş olduğu bir servis var ve bu servise ulaşabilmemiz için Python'un geliştirmiş olduğu bir Kütüphaneyi yüklememiz gerekiyor ve bu kütüphaneyi kurmak içinse komut satırı arabirimimiz var. Komut satırının buradaki görevi Google'nin servisine ulaşabilmemiz için bir arabirim oluşturmaktır bunun için Google'nin TextToSpeech denilen kod arabirimini kullanacağız buna gTTS'de denilmekte. Bu işlemleri sırayla gerçekleştireceğiz.
&nbsp;

# Kurulum

- Bilgisayarımıza Python paketini kuralım
https://www.python.org/downloads/
Yukarıda vermiş olduğum linkten istediğiniz sürümü indirip kurabilirsiniz.

- gTTs Kod arabirimini kuracağız bunun için Visual Studio Code terminalini açıp
pip install gTTS 
yazıp ENTER tuşuna basıyoruz ve karşımıza kurulum mesajları gelecek herhangi bir işlem yapmamıza gerek yok otomatik kuracaktır ve işlem tamam.
&nbsp;

# Kodlar

- Kod kısmına geçelim. gTTS Kütüphanesini import ( içe aktarma )etmemiz gerekiyor kütüphane dosyalarını çekebilmemiz için
```
from gtts import gTTS
```
&nbsp;


- İşletim sistemindeki dosyalara erişim için de bir import ( içe aktarma ) kodu ekliyoruz
 ```
import os
```
&nbsp;


- Sırada ise metnimizi oluşturmak için bir değişken oluşturuyoruz bu değişkene sese çevrilmesini istediğimiz mesajı yazabiliriz
```
text = 'Türk Hack Team, Türkiye'nin en eski siber güvenlik ve hacking forumlarından biridir.' 
```
&nbsp;


- Google gTTS Servislerini Türkçe kullanacağımızı belirten kodu yazıyoruz.
```
language = 'tr'
```
&nbsp;


- Ara birim parametrelerini ayarlayalım yani ilk parametrede metni vereceğiz, metnin Türkçe olduğunu belirteceğiz sonrasında ise okuma hızının yavaş mı veya hızlı mı olacağını ayarlayacağız.
```
speech = gTTS(text = text, lang = language, slow = False)
```
&nbsp;


- Speech parametreleri ayarladık şimdide dönüştürülen metnin kaydedilmesini sağlayan kodu yazıyoruz.
```
speech.save("tht.mp3")
```
&nbsp;


- Sistem, metnimizi dönüştürdü ve bu dönüştürülen metni sesli bir şekilde oynatılmasını sağlamak istiyoruz bunun için alttaki kodu yazalım.
```
os.system("start tht.mp3")
```

