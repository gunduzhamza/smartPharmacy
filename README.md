<h2 align="center"> Smart Pharmacy</h2>

[![My Skills](https://skills.thijs.gg/icons?i=py&theme=light)](https://skills.thijs.gg)

|| Headlines|
| :------: | ------ |
|`1` |[Usecase diagram](#1)|
|`2` |[Web Sitesi Tasarımı](#2)|


#### 1- Kullanım senaryosu diyagramı (Usecase diagram) <a name="1"></a>

> Akıllı eczane sisteminde projeye başlanırken ilk olarak kullanım senaryosu diyagramı oluşturulmuştur. Kullanım senaryosu diyagramı projenin genel taslağını belirler. İzlenilecek olan aşamalar bu diyagramda belirlenmiş olup bir yol haritası çıkarılmıştır. Kullanım senaryosu diyagramı göz önüne alınarak sırasıyla web sitesi, karekod, e-posta, eczane otomatı yapılmıştır.

<h2 align="center"><img src="/img/UseCase.png" height=600 width=560/></h2>

#### 2- Web Sitesi Tasarımı <a name="2"></a>

> Projenin ilk aşaması olan web sitesinde öncelikle doktor, gerekli bilgileri doğru bir şekilde girdikten sonra web sitesine kaydolur. Kayıt formunda kullanıcı adı, e-posta, parola biligileri girilerek doktor kaydı oluşturulur. Kaydolan doktorun bilgileri veri tabanına eklenir. 

<h2 align="center"><img src="/img/01.png" height=400 width=600 /></h2>

> Kayıt işlemi başarılı bir şekilde gerçekleştikten sonra akıllı eczane web sitesinin bütün sayfaları doktorların erişimine açılır. Doktorlar sisteme belirledikleri kullanıcı adı ve parola ile giriş yapar.

<h2 align="center"><img src="/img/00.png" height=400 width=600/></h2>

> Sisteme girişini gerçekleştiren doktor, gerekli işlemleri gerçekleştirmek için kontrol paneline girer. Kontrol panelinde hastaların kayıtlarını oluşturmak için “Hasta Kaydı Oluştur”, ilaçları görüntülemek için “İlaç Listesi”, hastalara reçete oluşturmak için “Reçete Yaz” ve oluşturulan reçeteleri görüntülemek için “Reçete Listesi” butonları yer almaktadır. Kaydı oluşturulan hastaların isim, soyisim, e-posta bilgilerinin bulunduğu bir tablo da kontrol paneli sayfasında görülür. Ek olarak doktoların kolay bir şekilde hastaları bulmasını sağlayan arama butonu eklenmiştir. 

<h2 align="center"><img src="/img/03.png" height=400 width=600/></h2>

>“Hasta Kaydı Oluştur” butonuna tıklandıktan sonra hasta kayıt sayfasına yönlendirilir. Kayıt formunda hastanın isim, soyisim ve e-posta bilgileri doktor tarafından kaydedilir.

<h2 align="center"><img src="/img/04.png" height=400 width=600/></h2>

>Kaydı oluşturulan hastaların reçetesini oluşturmak için “Reçete Yaz” butonuna tıklanır. Reçete oluşturma sayfasına yönlendirilen doktor, hastayı ve hastaya verilecek olan ilaçları ekler. Bu eklenen ilaçlar reçete tablosu olarak veri tabanına eklenir. 
<h2 align="center"><img src="/img/07.png" height=400 width=600/></h2>

>Hasta için oluşturulan reçetenin içeriğinde ilaç isimlerinin yer aldığı bir kare kod oluşturulur. Reçete sayfasında doktor tarafından oluşturulan hasta kayıt bilgileri ve her bir hastaya ait reçeteler yer almaktadır. Doktor, bu sayfada reçetelerin detay bilgilerini görüntüleyebilir ve oluşturulan reçeteyi hastanın e-mailine kare kod formatında gönderebilir.

 <h2 align="center"><img src="/img/05.png" height=400 width=600/></h2>
 
 >Kare kod formatında gönderilen e-posta hastanın ilgili e-posta adresinde aşağıdaki gibi görüntülenir. Gelen maili otomatın kamerasına okutacak olan hasta gerekli ilaçları temin eder.

 
 <h2 align="center"><img src="/img/08.png" height=500 width=600/></h2>
 
 > Hastanın e-mailine gelen kare kod otomat kamerasına okutularak ilaçlar hasta tarafından alınır.