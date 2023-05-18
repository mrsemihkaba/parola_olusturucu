# Parola Oluşturucu
İlk olarak, `parola_olustur()` adında bir fonksiyon tanımlıyoruz. Bu fonksiyon, uzunluk adında bir parametre alıyor. Bu parametre, oluşturulacak parolanın kaç karakter uzunluğunda olacağını belirlemek için kullanılıyor.<br>

Ardından, `string()` modülünü kullanarak, parolada kullanılacak olan karakter kümesini belirliyoruz. Bu karakter kümesi, `ascii_letters()` (büyük ve küçük harfler), digits (rakamlar) ve `punctuation()` (noktalama işaretleri) gibi karakterleri içerir. Bu karakterler, genel olarak parola oluştururken yaygın olarak kullanılan karakterlerdir.<br>

`random.choice()` ve `random.range()` fonksiyonlarını kullanarak, belirlenen karakter kümesinden rastgele karakterler seçilerek parola oluşturulur. `random.choice()` fonksiyonu, karakter kümesinden rastgele bir karakter seçmek için kullanılırken, `random.range()` fonksiyonu ise belirli bir uzunlukta bir döngü oluşturmak için kullanılır.<br>

Son olarak, oluşturulan parola `parola()` değişkenine atılır ve return ifadesiyle fonksiyondan geri döndürülür.<br>

Kullanıcıdan `uzunluk()` adında bir girdi alarak, oluşturulacak parolanın uzunluğunu belirleriz.<br>

`parola_olustur()` fonksiyonunu, kullanıcının girdisi olan `uzunluk()` değeriyle çağırarak rastgele bir parola oluşturulur.<br>

Oluşturulan parola ekrana basılır ve kullanıcıya gösterilir.<br>

Bu basit parola oluşturucu, kullanıcıdan belirli bir uzunlukta bir parola alır ve belirtilen karakter kümesinden rastgele karakterler kullanarak parolayı oluşturur. Daha güvenli parolalar oluşturmak için karmaşık algoritmalar, daha uzun uzunluklar ve özel gereksinimler göz önünde bulundurulmalıdır.






