import streamlit as st

# Uygulama Ayarları (Geniş ekran düzeni)
st.set_page_config(page_title="Ağ Hesaplama Aracı", page_icon="🕸️", layout="wide")
st.title("🕸️ Ağ ve Halat Hesaplama Uygulaması")
st.markdown("---")

# ==========================================
# 1. BÖLÜM: FORM ALANI (VERİ GİRİŞİ + BUTON)
# ==========================================
st.subheader("📝 Veri Girişi")

# Tüm girişleri bir form içine alıyoruz.
# Böylece butona basana kadar sayfa yenilenmez.
with st.form("hesaplama_formu"):
    
    # Sütunları formun içinde oluşturuyoruz
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("##### 📏 Genel Ölçüler")
        ag_capi = st.number_input("Ağ Çapı (metre)", min_value=0, step=1, value=30)
        gramaj = st.number_input("1 m² Ağ Gramajı (gr/m²)", min_value=0, step=5, value=380)

    with c2:
        st.markdown("##### 🏗️ Dikme Bilgileri")
        dikme_sayisi = st.number_input("Dikme Sayısı (adet)", min_value=0, step=1, value=40)
        dikme_uzunlugu = st.number_input("Dikme Uzunluğu (Derinlik) (m)", min_value=0, step=1, value=10)

    with c3:
        st.markdown("##### 🪢 Halat Ekstraları")
        hac_sayisi = st.number_input("Haç Sayısı (adet)", min_value=0, step=1, value=2)
    
    st.markdown("---")
    
    # Formun gönderme butonu (En önemli kısım burası)
    # use_container_width=True butonu ekrana yayar, daha şık durur.
    hesapla_butonu = st.form_submit_button("🚀 HESAPLA", type="primary", use_container_width=True)


# ==========================================
# 2. BÖLÜM: SONUÇLAR (SADECE BUTONA BASINCA ÇALIŞIR)
# ==========================================

if hesapla_butonu:
    
    # --- 1. ÇEVRE AĞI HESABI ---
    st.header("1. Çevre Ağı Sonuçları")

    # Hesaplamalar
    alan_ana = ag_capi * 3.14 * (dikme_uzunlugu + 0.25)
    alan_pay = (dikme_uzunlugu + 0.25) * (dikme_sayisi * 0.15)
    cevre_toplam_m2 = alan_ana + alan_pay
    cevre_agirlik_kg = (cevre_toplam_m2 * gramaj) / 1000

    # Detaylar
    d1, d2 = st.columns(2)
    with d1:
        st.info(f"🔹 Ana Gövde Alanı:\n### {alan_ana:.2f} m²")
    with d2:
        st.info(f"🔹 Payların Alanı:\n### {alan_pay:.2f} m²")

    # Ana Sonuçlar
    res1, res2 = st.columns(2)
    with res1:
        st.warning(f"TOPLAM ALAN:\n# {cevre_toplam_m2:.2f} m²")
    with res2:
        st.success(f"ÇEVRE AĞIRLIĞI:\n# {cevre_agirlik_kg:.2f} kg")

    st.markdown("---") # Ayırıcı

    # --- 2. TABAN AĞI HESABI ---
    st.header("2. Taban Ağı Sonuçları")

    # Hesaplamalar
    taban_gramaj = (gramaj / 2) * 1.15
    taban_uzunlugu = ag_capi * 1.3
    kose_uzunlugu = (ag_capi * 3.14) / 8

    taban_alani = taban_uzunlugu ** 2
    koseler_alani = (kose_uzunlugu ** 2) * 2
    taban_toplam_m2 = taban_alani - koseler_alani
    taban_agirlik_kg = (taban_toplam_m2 * taban_gramaj) / 1000

    # Detaylar
    st.caption(f"ℹ️ Taban Gramajı: {taban_gramaj:.2f} gr | Taban Uzunluğu: {taban_uzunlugu:.2f} m | Köşe Uzunluğu: {kose_uzunlugu:.2f} m")

    # Ana Sonuçlar
    t_res1, t_res2 = st.columns(2)
    with t_res1:
        st.warning(f"NET TABAN ALANI:\n# {taban_toplam_m2:.2f} m²")
    with t_res2:
        st.success(f"TABAN AĞIRLIĞI:\n# {taban_agirlik_kg:.2f} kg")

    st.markdown("---") # Ayırıcı

    # --- 3. HALAT (DONAM) HESABI ---
    st.header("3. Halat (Donam) Sonuçları")

    # Hesaplamalar
    yaka_halati = 3 * ag_capi * 3.14
    toplam_dikme_payi = dikme_sayisi * 0.2
    
    # Dikme uzunluğuna ekleme yok (Senin istediğin gibi)
    toplam_dikme_uzunlugu_halat = dikme_uzunlugu * dikme_sayisi
    
    toplam_sapan_uzunlugu = dikme_sayisi * 2.5
    toplam_hac_uzunlugu = hac_sayisi * (ag_capi + 2)

    toplam_halat_uzunlugu = (yaka_halati + toplam_dikme_payi + 
                             toplam_dikme_uzunlugu_halat + 
                             toplam_sapan_uzunlugu + toplam_hac_uzunlugu)

    harcanacak_top_adet = toplam_halat_uzunlugu / 220
    toplam_halat_agirligi = harcanacak_top_adet * 25.5

    # Ana Sonuçlar
    h1, h2, h3 = st.columns(3)

    with h1:
        st.info(f"TOPLAM GİDECEK HALAT:\n# {toplam_halat_uzunlugu:.2f} m")
        
    with h2:
        st.warning(f"HARCANACAK TOP:\n# {harcanacak_top_adet:.2f} adet")
        
    with h3:
        st.success(f"HALAT AĞIRLIĞI:\n# {toplam_halat_agirligi:.2f} kg")

    st.markdown("---")

    # ==========================================
    # 4. BÖLÜM: GENEL TOPLAM (FİNAL SONUÇ)
    # ==========================================
    st.header(" Genel Toplam Ağırlık")

    genel_toplam_agirlik = cevre_agirlik_kg + taban_agirlik_kg + toplam_halat_agirligi

    # Tek ve dev bir sütun
    st.success(f"PROJENİN TOPLAM AĞIRLIĞI:\n# {genel_toplam_agirlik:.2f} kg")