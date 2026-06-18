import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Yusuf Alper Gülden | Portfolio", layout="wide")

# --- YAN MENÜ (SIDEBAR) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # Temsili profil fotoğrafı
st.sidebar.title("Yusuf Alper Gülden")
st.sidebar.write("💻 Bilgisayar Mühendisliği Öğrencisi | AI & Data Science")
st.sidebar.markdown("---")
st.sidebar.header("İletişim Bilgileri")
st.sidebar.write("📍 İstanbul, Türkiye")
st.sidebar.write("📧 yusufalpergulden2@gmail.com")
st.sidebar.write("📞 +90 (553) 703 49 83")
st.sidebar.markdown("[LinkedIn Profili](https://linkedin.com/in/yusufalpergülden)")
st.sidebar.markdown("[GitHub Profili](https://github.com/YusufAlperGulden)")

# --- ANA SAYFA (SEKMELER) ---
st.title("YUSUF ALPER GÜLDEN | PORTFOLIO")
st.write("Analitik ve teknoloji odaklı, Yapay Zeka ve Veri Bilimi alanlarında güçlü bir temele sahip Bilgisayar Mühendisliği öğrencisiyim.")

# Sitenin bölümlerini sekmelere ayırıyoruz
tab1, tab2, tab3, tab4 = st.tabs(["Hakkımda & Eğitim", "Deneyim", "Projeler", "Yetenekler & Sertifikalar"])

# 1. SEKME: HAKKIMDA & EĞİTİM
with tab1:
    st.header("Eğitim Geçmişi")
    st.markdown("""
    **Doğuş Üniversitesi** | *Ekim 2023 - Günümüz*
    * Bilgisayar Mühendisliği (İngilizce) - %100 Başarı Bursu
    * Beklenen Mezuniyet: Haziran 2027
    * Lokasyon: İstanbul, Türkiye
    
    **Burak Bora Anadolu Lisesi** | *2018 - 2022*
    * Lise Diploması
    """)

# 2. SEKME: DENEYİM
with tab2:
    st.header("Profesyonel Deneyim")
    st.markdown("""
    **Stajyer | Teknasyon**
    *Temmuz 2025 - Ağustos 2025 | İstanbul, Türkiye*
    * Bilgi Teknolojileri departmanında dijital ürün ve teknoloji odaklı projelere katkı sağladım.
    * Makine Öğrenmesi (Machine Learning) ve Derin Öğrenme (Deep Learning) iş akışlarında pratik deneyim kazandım.
    * Veri analizi, modelleme ve optimizasyon süreçleri için Python ve ilgili kütüphaneleri kullandım.
    * Disiplinlerarası takımlarla çalışarak proje takibi ve profesyonel iletişim becerilerimi geliştirdim.
    """)

# 3. SEKME: PROJELER
with tab3:
    st.header("Geliştirdiğim Projeler")
    
    # Yeni Proje (Isolation Forest)
    with st.expander("AI-Powered Personnel Tracking & Anomaly Detection System (Haziran 2026)"):
        st.markdown("""
        * **Platform:** GitHub & Streamlit Community Cloud
        * **Açıklama:** Çalışanların giriş/çıkış loglarını analiz ederek şüpheli aktiviteleri otomatik tespit eden bulut tabanlı bir web uygulaması geliştirdim.
        * **Kullanılan Teknolojiler:** Python, Scikit-learn (Isolation Forest), Pandas, Streamlit, Google Firebase.
        * **Detay:** Hardcoded (sabit) if-else kuralları yerine, veriden kendi kendine öğrenen gözetimsiz (unsupervised) bir model entegre ettim ve verileri Firebase üzerinde gerçek zamanlı olarak sakladım.
        """)
        
    # Keras Projesi
    with st.expander("Student Grade Prediction with Keras (Temmuz 2025)"):
        st.markdown("""
        * **Platform:** Kaggle
        * **Açıklama:** Keras Sequential API kullanarak öğrencilerin akademik performansını tahmin eden bir makine öğrenmesi modeli geliştirdim.
        * **Detay:** Kapsamlı veri temizliği, ön işleme ve özellik seçimi (feature selection) adımlarını uyguladım. Tahmin doğruluğunu artırmak için model mimarisini optimize ettim.
        """)
        
    # Titanic Projesi
    with st.expander("Titanic Dataset Analysis (Temmuz 2025)"):
        st.markdown("""
        * **Platform:** Kaggle
        * **Açıklama:** Kaggle Titanic veri seti üzerinde kapsamlı veri analizi ve özellik çıkarımı (feature engineering) gerçekleştirdim.
        * **Detay:** Yolcuların hayatta kalma oranlarını yaş, cinsiyet ve sınıf gibi değişkenlere dayanarak tahmin eden bir sınıflandırma modeli kurdum.
        """)
        
    # Scikit-Learn Projeleri
    with st.expander("Scikit-learn Machine Learning Projects (Temmuz 2025)"):
        st.markdown("""
        * **Platform:** GitHub
        * **Açıklama:** Regresyon ve sınıflandırma dahil olmak üzere çeşitli gözetimli öğrenme (supervised learning) algoritmalarını sıfırdan uyguladım.
        * **Detay:** Çapraz doğrulama (cross-validation) ve metrik tabanlı model karşılaştırma pratikleri gerçekleştirdim.
        """)

# 4. SEKME: YETENEKLER & SERTİFİKALAR
with tab4:
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Teknik Yetenekler")
        st.markdown("""
        * **Programlama Dilleri:** Python (İleri Seviye), SQL, Java, C++
        * **Yapay Zeka & Veri Bilimi:** Makine Öğrenmesi, Derin Öğrenme, Keras, Scikit-learn, Veri Analizi, Veri Görselleştirme
        * **Geliştirici Araçları:** Git, GitHub, Kaggle, Streamlit, MS Office, Canva
        * **Diller:** Türkçe (Ana Dil), İngilizce (Orta-İleri)
        """)
        
    with col2:
        st.header("Sertifikalar & Eğitimler")
        st.markdown("""
        * **Introduction to AI**, *NVIDIA* (Ara 2025) - Temel yapay zeka kavramları, sinir ağları ve derin öğrenme.
        * **Cyber Security 101**, *Akbank Gençlik Akademisi* (Eyl 2024) - Bilgi güvenliği prensipleri ve siber tehditler.
        * **Online Staj Programı**, *Yetenek Sultanbeyli & Üretken Akademi* (2024) - Dijital yetkinlikler.
        """)
