# SmartEnergyFlow – Gerçek Zamanlı Enerji Tüketimi İzleme
SmartEnergyFlow, ev ortamındaki cihazların enerji tüketimi ve zaman verilerini gerçek zamanlı olarak toplayıp AWS altyapısı üzerinden güvenli bir şekilde veritabanına kaydeden bir veri yönetimi projesidir. 

📚 Kullanılan Kütüphaneler

NumPy & Pandas: Ham sensör verilerini yüklemek, tablo benzeri yapılarla ön işleme ve manipülasyon işlemlerini hızlıca yapmak için kullanıldı.

Matplotlib: Zaman serisi grafikleri ve dağılım görselleştirmeleri ile verinin zamana bağlı davranışını anlamamıza yardımcı oldu.

scikit-learn: Özellik seçimi (feature selection) adımlarında SelectKBest, VarianceThreshold gibi yöntemlerle kritik öznitelikleri belirledik.

LightGBM: Özellik seçimi sonrası daha hızlı ve ölçeklenebilir bir modelleme aracı olarak kullanıldı; tüketim örüntülerinin önem derecelerini analiz etmek için LightGBM’in feature_importances_ özelliğinden yararlandık.

boto3: AWS Kinesis’e veri akışı göndermek ve AWS Lambda fonksiyonları aracılığıyla DynamoDB’ye kayıt işlemlerini tetiklemek için resmi AWS SDK’sı kullanıldı.

📊 Neler Yapıldı?

Veri Toplama & Akış (AWS Kinesis): Ev içi IoT cihazlarından JSON formatında enerji ve zaman verileri toplandı. boto3 ile SmartEnergyFlowStream adlı Kinesis stream’ine gerçek zamanlı olarak gönderildi.

Veri İşleme & Özellik Seçimi: Gelen veriler Pandas DataFrame’e aktarıldı, eksik değerler temizlendi ve aykırı değerler belirlendi. scikit-learn araçlarıyla öznitelik seçimi yapılarak yüksek varyanslı ve hedefle güçlü korelasyonu olan özellikler tespit edildi. LightGBM ile kısa bir ön modelleme yapılarak öznitelik önem sıralaması çıkarıldı.

AWS Lambda & DynamoDB Entegrasyonu: Kinesis’e gelen her kayıt, AWS Lambda fonksiyonuyla tetiklendi. Lambda içindeki iş mantığıyla veriler DynamoDB tablosuna yazıldı; böylece hem sürekli güncellenen bir depolama sağlandı hem de sunucusuz (serverless) mimariyle ölçeklenebilirlik elde edildi.

Grafiksel Analiz & Raporlama: Matplotlib kullanarak zaman serisi çizimleri ve feature importance grafikleri oluşturuldu. Bu grafikler veri mühendisleri ve iş analistleri için dashboard’lara kolayca entegre edilebilir çıktı sağladı.

✅ Sonuç

SmartEnergyFlow ile gerçek zamanlı enerji tüketim verilerini AWS üzerinde kesintisiz şekilde toplayabiliyor ve ölçeklenebilir bir sunucusuz mimariyle DynamoDB’ye kaydedebiliyoruz. Özellik seçimi sayesinde kritik parametreleri belirleyerek ileride tüketim tahmini veya anomali tespiti için sağlam bir temel oluşturduk. Bu proje anlık tüketim trendlerini izlemeye, özelllik seçimi ile kritik parametreleri belirlemeye ve veri odaklı içgörüler elde etmeye yarar.
