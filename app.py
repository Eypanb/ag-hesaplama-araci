import streamlit as st

# Uygulama Ayarları
st.set_page_config(page_title="Ağ Hesaplama Aracı", page_icon="🕸️", layout="wide")
st.title("🕸️ Ağ ve Halat Hesaplama Uygulaması")
st.markdown("---")

# Sayfayı 4 sekmeye ayırıyoruz
tab_ana_sistem, tab_kus_sistemi, tab_kare_sistem, tab_sekizgen_sistem = st.tabs([
    "🏗️ ANA KAFES (DAİRESEL)", 
    "🐦 KUŞ AĞI SİSTEMİ", 
    "🔲 KARE KAFES SİSTEMİ",
    "🛑 SEKİZGEN KAFES SİSTEMİ"
])

# ==========================================================================================
# 1. SEKME: ANA KAFES SİSTEMİ (DAİRESEL) - Standart Halat
# ==========================================================================================
with tab_ana_sistem:
    st.header("🏗️ Dairesel Ana Kafes Hesaplama")
    
    with st.form("form_ana_kafes"):
        st.subheader("📝 Veri Girişi")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("##### 📏 Genel Ölçüler")
            ag_capi = st.number_input("Ana Ağ Çapı (metre)", min_value=0, step=1, value=30)
            gramaj = st.number_input("Ana Ağ Gramajı (gr/m²)", min_value=0, step=5, value=380)

        with c2:
            st.markdown("##### 🏗️ Dikme Bilgileri")
            dikme_sayisi = st.number_input("Dikme Sayısı (adet)", min_value=0, step=1, value=40)
            dikme_uzunlugu = st.number_input("Dikme Uzunluğu (Derinlik) (m)", min_value=0, step=1, value=10)

        with c3:
            st.markdown("##### 🪢 Halat Ekstraları")
            hac_sayisi = st.number_input("Ana Haç Sayısı (adet)", min_value=0, step=1, value=2)
            
        st.markdown("---")
        btn_hesapla_ana = st.form_submit_button("🚀 ANA KAFESİ HESAPLA", type="primary", use_container_width=True)

    if btn_hesapla_ana:
        st.markdown("### 📊 Hesaplama Sonuçları")
        
        # --- HESAPLAMALAR ---
        # 1. Çevre
        alan_ana = ag_capi * 3.14 * (dikme_uzunlugu + 0.25)
        alan_pay = (dikme_uzunlugu + 0.25) * (dikme_sayisi * 0.15)
        cevre_toplam_m2 = alan_ana + alan_pay
        cevre_agirlik_kg = (cevre_toplam_m2 * gramaj) / 1000

        # 2. Taban
        taban_gramaj = (gramaj / 2) * 1.15
        taban_uzunlugu = ag_capi * 1.3
        kose_uzunlugu = (ag_capi * 3.14) / 8
        taban_alani = taban_uzunlugu ** 2
        koseler_alani = (kose_uzunlugu ** 2) * 2
        taban_toplam_m2 = taban_alani - koseler_alani
        taban_agirlik_kg = (taban_toplam_m2 * taban_gramaj) / 1000

        # 3. Halat (Standart Gemi Halatı Hesabı)
        yaka_halati = 3 * ag_capi * 3.14
        toplam_dikme_payi = dikme_sayisi * 0.2
        toplam_dikme_uzunlugu_halat = dikme_uzunlugu * dikme_sayisi
        toplam_sapan_uzunlugu = dikme_sayisi * 2.5
        toplam_hac_uzunlugu = hac_sayisi * (ag_capi + 2)
        toplam_halat_uzunlugu = (yaka_halati + toplam_dikme_payi + toplam_dikme_uzunlugu_halat + toplam_sapan_uzunlugu + toplam_hac_uzunlugu)
        harcanacak_top_adet = toplam_halat_uzunlugu / 220
        toplam_halat_agirligi = harcanacak_top_adet * 25.5
        
        ana_sistem_toplam = cevre_agirlik_kg + taban_agirlik_kg + toplam_halat_agirligi

        res1, res2, res3 = st.columns(3)
        with res1:
            st.info(f"**ÇEVRE AĞIRLIĞI:**\n# {cevre_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Alan:** {cevre_toplam_m2:.2f} m²")
        with res2:
            st.info(f"**TABAN AĞIRLIĞI:**\n# {taban_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Net Taban Alanı:** {taban_toplam_m2:.2f} m²")
        with res3:
            st.info(f"**ANA HALAT AĞIRLIĞI:**\n# {toplam_halat_agirligi:.2f} kg")
            st.markdown(f"**📏 Toplam Uzunluk:** {toplam_halat_uzunlugu:.2f} m")
            
        st.markdown("---")
        st.success(f"🏗️ **ANA KAFES SİSTEMİ TOPLAMI:**\n# {ana_sistem_toplam:.2f} kg")


# ==========================================================================================
# 2. SEKME: KUŞ AĞI SİSTEMİ - (GÜNCELLENDİ: İSKOTA HALAT)
# ==========================================================================================
with tab_kus_sistemi:
    st.header("🐦 Kuş Ağı Hesaplama")
    
    with st.form("form_kus_agi"):
        st.subheader("📝 Veri Girişi")
        k_col1, k_col2 = st.columns(2)
        with k_col1:
            st.markdown("##### 📏 Kuş Ağı Ölçüleri")
            kus_ag_capi = st.number_input("Kuş Ağı Çapı (metre)", min_value=0, step=1, value=30)
            kus_gramaj = st.number_input("Kuş Ağı Gramajı (gr/m²)", min_value=0, step=5, value=100)
        with k_col2:
            st.markdown("##### ⛓️ Kuş Ağı Aksesuarları")
            kus_sapan_sayisi = st.number_input("Kuş Ağı Sapan Sayısı (adet)", min_value=0, step=1, value=20)
            kus_hac_sayisi = st.number_input("Kuş Ağı Haç Sayısı (adet)", min_value=0, step=1, value=2)
            
        st.markdown("---")
        btn_hesapla_kus = st.form_submit_button("🚀 KUŞ AĞINI HESAPLA", type="primary", use_container_width=True)

    if btn_hesapla_kus:
        st.markdown("### 📊 Hesaplama Sonuçları")
        
        # --- HESAPLAMALAR ---
        yari_cap_kus = kus_ag_capi / 2
        kus_agi_alani = 3.14 * (yari_cap_kus ** 2)
        kus_agi_agirlik_kg = (kus_agi_alani * kus_gramaj) / 1000
        
        # Halat Uzunlukları
        kus_yaka_1 = kus_ag_capi * 3.14
        kus_yaka_2 = (kus_ag_capi - 1) * 3.14
        kus_sapan_toplam = kus_sapan_sayisi * 3
        kus_hac_toplam = kus_hac_sayisi * (kus_ag_capi + 6)
        kus_toplam_halat = kus_yaka_1 + kus_yaka_2 + kus_sapan_toplam + kus_hac_toplam
        
        # İSKOTA HALAT HESABI (45 gr/m)
        kus_halat_agirlik_kg = kus_toplam_halat * 0.045
        
        kus_sistemi_toplam = kus_agi_agirlik_kg + kus_halat_agirlik_kg
        
        k_res1, k_res2 = st.columns(2)
        with k_res1:
            st.warning(f"**KUŞ AĞI AĞIRLIĞI:**\n# {kus_agi_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Kuş Ağı Alanı:** {kus_agi_alani:.2f} m²")
        with k_res2:
            st.warning(f"**KUŞ HALAT AĞIRLIĞI:**\n# {kus_halat_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Halat:** {kus_toplam_halat:.2f} m")
            st.caption("ℹ️ **Not:** 8mm İskota halat (45 gr/m) verilerine göre hesaplanmıştır.")
            
        st.markdown("---")
        st.success(f"🐦 **KUŞ AĞI SİSTEMİ TOPLAMI:**\n# {kus_sistemi_toplam:.2f} kg")

# ==========================================================================================
# 3. SEKME: KARE KAFES SİSTEMİ - (GÜNCELLENDİ: İSKOTA HALAT)
# ==========================================================================================
with tab_kare_sistem:
    st.header("🔲 Kare Kafes Hesaplama")
    
    # --- GİRİŞ KISMI ---
    with st.form("form_kare_kafes"):
        st.subheader("📝 Veri Girişi")
        
        kc1, kc2 = st.columns(2)
        
        with kc1:
            st.markdown("##### 📏 Kare Ölçüleri")
            kare_yaka_uzunlugu = st.number_input("Yaka Uzunluğu / Kenar (m)", min_value=0.0, step=0.1, format="%.1f", value=10.0)
            kare_derinlik = st.number_input("Derinlik (m)", min_value=0.0, step=0.1, format="%.1f", value=10.0)
            kare_gramaj = st.number_input("Kare Ağ Gramajı (gr/m²)", min_value=0, step=5, value=400)
            
        with kc2:
            st.markdown("##### ⚙️ Seçenekler")
            ikinci_yaka_var_mi = st.checkbox("İkinci Yaka Var mı? (Çift Yaka)", value=True)
            st.caption("İşaretlenirse yatay halat hesabına bir tur daha eklenir.")
            
        st.markdown("---")
        btn_hesapla_kare = st.form_submit_button("🚀 KARE KAFESİ HESAPLA", type="primary", use_container_width=True)
        
    # --- SONUÇ KISMI ---
    if btn_hesapla_kare:
        st.markdown("### 📊 Hesaplama Sonuçları")
        
        # --- A) AĞ (FİLE) HESABI ---
        efektif_derinlik = kare_derinlik + 0.25
        efektif_yaka = kare_yaka_uzunlugu + 0.15
        
        kare_cevre_alani = efektif_derinlik * efektif_yaka * 4
        kare_taban_alani = efektif_yaka * efektif_yaka
        
        kare_toplam_alan = kare_cevre_alani + kare_taban_alani
        kare_ag_agirlik_kg = (kare_toplam_alan * kare_gramaj) / 1000
        
        # --- B) HALAT HESABI ---
        bir_tur_yaka_uzunlugu = kare_yaka_uzunlugu * 4
        
        yatay_halat_sayisi = 2
        if ikinci_yaka_var_mi:
            yatay_halat_sayisi += 1
            
        toplam_yatay_halat = bir_tur_yaka_uzunlugu * yatay_halat_sayisi
        
        dikey_halat_birim = kare_derinlik + 3
        toplam_dikey_halat = dikey_halat_birim * 4
        
        kare_toplam_halat = toplam_yatay_halat + toplam_dikey_halat
        
        # İSKOTA HALAT HESABI (45 gr/m)
        kare_halat_agirlik_kg = kare_toplam_halat * 0.045
        
        # --- GENEL TOPLAM ---
        kare_sistem_toplam = kare_ag_agirlik_kg + kare_halat_agirlik_kg
        
        # --- GÖRSELLEŞTİRME ---
        kr1, kr2 = st.columns(2)
        
        with kr1:
            st.error(f"**KARE AĞ AĞIRLIĞI:**\n# {kare_ag_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Ağ Alanı:** {kare_toplam_alan:.2f} m²")
            st.caption(f"Çevre: {kare_cevre_alani:.2f} m² | Taban: {kare_taban_alani:.2f} m²")
            
        with kr2:
            st.error(f"**KARE HALAT AĞIRLIĞI:**\n# {kare_halat_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Halat:** {kare_toplam_halat:.2f} m")
            st.caption(f"Yatay: {toplam_yatay_halat:.2f} m | Dikey: {toplam_dikey_halat:.2f} m")
            st.caption("ℹ️ **Not:** 8mm İskota halat (45 gr/m) verilerine göre hesaplanmıştır.")
            
        st.markdown("---")
        st.success(f"🔲 **KARE KAFES SİSTEMİ TOPLAMI:**\n# {kare_sistem_toplam:.2f} kg")

# ==========================================================================================
# 4. SEKME: SEKİZGEN KAFES SİSTEMİ - (Standart Halat)
# ==========================================================================================
with tab_sekizgen_sistem:
    st.header("🛑 Sekizgen Kafes Hesaplama")
    
    # --- GİRİŞ KISMI ---
    with st.form("form_sekizgen_kafes"):
        st.subheader("📝 Veri Girişi")
        
        s1, s2 = st.columns(2)
        
        with s1:
            st.markdown("##### 📏 Sekizgen Ölçüleri")
            sekizgen_kenar = st.number_input("Bir Kenar Uzunluğu (m)", min_value=0.0, step=0.1, format="%.1f", value=5.0)
            sekizgen_derinlik = st.number_input("Derinlik (m)", min_value=0.0, step=0.1, format="%.1f", value=10.0)
            sekizgen_gramaj = st.number_input("Ağ Gramajı (gr/m²)", min_value=0, step=5, value=400)
            
        with s2:
            st.markdown("##### ⚙️ Halat Seçenekleri")
            sekizgen_cift_yaka = st.checkbox("İkinci Yaka Var mı? (Çift Yaka)", value=True)
            st.caption("İşaretlenirse sekizgenin çevresine bir tur halat daha eklenir.")
            
        st.markdown("---")
        btn_hesapla_sekizgen = st.form_submit_button("🚀 SEKİZGEN KAFESİ HESAPLA", type="primary", use_container_width=True)
        
    # --- SONUÇ KISMI ---
    if btn_hesapla_sekizgen:
        st.markdown("### 📊 Hesaplama Sonuçları")
        
        # --- A) AĞ HESABI ---
        s_efektif_derinlik = sekizgen_derinlik + 0.25
        s_efektif_kenar = sekizgen_kenar + 0.15
        
        sekizgen_cevre_alani = s_efektif_kenar * 8 * s_efektif_derinlik
        
        sanal_cap = sekizgen_kenar * 2.613
        sanal_yaricap = sanal_cap / 2
        sekizgen_taban_alani = 3.14 * (sanal_yaricap ** 2)
        
        sekizgen_toplam_alan = sekizgen_cevre_alani + sekizgen_taban_alani
        sekizgen_ag_agirlik_kg = (sekizgen_toplam_alan * sekizgen_gramaj) / 1000
        
        # --- B) HALAT HESABI ---
        bir_tur_sekizgen_cevre = sekizgen_kenar * 8
        
        s_yatay_halat_sayisi = 2 
        if sekizgen_cift_yaka:
            s_yatay_halat_sayisi += 1
            
        s_toplam_yatay_halat = bir_tur_sekizgen_cevre * s_yatay_halat_sayisi
        
        s_dikey_halat_birim = sekizgen_derinlik + 3
        s_toplam_dikey_halat = s_dikey_halat_birim * 8
        
        sekizgen_toplam_halat = s_toplam_yatay_halat + s_toplam_dikey_halat
        sekizgen_halat_agirlik_kg = (sekizgen_toplam_halat / 220) * 25.5
        
        sekizgen_sistem_toplam = sekizgen_ag_agirlik_kg + sekizgen_halat_agirlik_kg
        
        # --- GÖRSELLEŞTİRME ---
        sr1, sr2 = st.columns(2)
        
        with sr1:
            st.error(f"**AĞ AĞIRLIĞI:**\n# {sekizgen_ag_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Ağ Alanı:** {sekizgen_toplam_alan:.2f} m²")
            st.caption(f"Çevre (8 Duvar): {sekizgen_cevre_alani:.2f} m²")
            st.caption(f"Taban (Daire Formu): {sekizgen_taban_alani:.2f} m²")
            
        with sr2:
            st.error(f"**HALAT AĞIRLIĞI:**\n# {sekizgen_halat_agirlik_kg:.2f} kg")
            st.markdown(f"**📏 Toplam Halat:** {sekizgen_toplam_halat:.2f} m")
            st.caption(f"Yatay: {s_toplam_yatay_halat:.2f} m | Dikey: {s_toplam_dikey_halat:.2f} m")
            
        st.markdown("---")
        st.success(f"🛑 **SEKİZGEN KAFES SİSTEMİ TOPLAMI:**\n# {sekizgen_sistem_toplam:.2f} kg")