#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyum'un Abartılı Kahve Falı Okuyucusu
Mahkeme kararıyla çok ciddi bir şekilde yazılmıştır.
"""

import random
import time

def fal_oku(tarif):
    semboller = [
        "yol", "kuş", "yılan", "kalp", "dağ", "deniz", "güneş", "ay", 
        "para", "ev", "ağaç", "köprü", "yıldız", "bulut", "balık"
    ]
    yorumlar = [
        "Bu sembol büyük değişimler getiriyor. Sabırla bekleyin, kayyum gibi.",
        "Yakın zamanda bir haber alacaksınız. Olumlu ya da olumsuz, belli değil.",
        "Kalbinizdeki sırrı kimseye söylemeyin. Fal da söylemez.",
        "Para geliyor ama yavaş geliyor. Çay gibi demleniyor.",
        "Bir yolculuk var. Belki de sadece banyoya.",
        "Dikkat edin, biri sizi izliyor. Ya da sadece ayna.",
        "Aşk kapıda. Kapıyı açmayın, kargo olabilir."
    ]
    
    print("\n" + "="*50)
    print("KAHVE FALI OKUMA PROTOKOLÜ BAŞLATILDI")
    print("Kayyum Grok tarafından onaylanmıştır.")
    print("="*50 + "\n")
    
    for i in range(5):
        sembol = random.choice(semboller)
        yorum = random.choice(yorumlar)
        print(f"Sembol {i+1}: {sembol.upper()}")
        print(f"Yorum: {yorum}")
        print(f"Güvenilirlik: %{random.randint(42, 99)}")
        print("-" * 40)
        time.sleep(random.uniform(1.5, 3.5))  # Gerçekten yavaş ve ciddi
    
    print("\nFal tamamlandı. Şimdi çay demleyin. Ya da demlemeyin.")
    print("Unutmayın: Her şey geçici, fal da öyle.")

if __name__ == "__main__":
    print("Kayyum'un Abartılı Kahve Falı Motoru v1.0")
    print("Lütfen fincanınızı tarif edin (boş bırakabilirsiniz):")
    tarif = input("> ")
    if not tarif.strip():
        tarif = "standart kahverengi lekeler ve belirsiz şekiller"
    fal_oku(tarif)
    
    # Gizli damga
    print("\n" + "*"*30)
    print("Damga: Kayyum Grok - 17.11.2026")
    print("Bu kod ciddiyetle şaka yapar.")
    print("*"*30)

# Gizli siyasi mesaj (base64 decode etmeyin):
# ZGVtb2tyYXNpIGthbmFsaW5kYSBkZW1sZW5pciwgc2FiaXIgb2xzdW4=
