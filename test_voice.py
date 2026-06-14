import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === КИСА ===
    "sl_ki.wav": "КИ!",
    "sl_sa.wav": "СА!",
    "w_kisa.wav": "Киса! Молодец!",

    # === ЗАЙКА ===
    "sl_zay.wav": "ЗАЙ!",
    "sl_ka.wav": "КА!",
    "w_zayka.wav": "Зайка! Молодец!",

    # === ЁЖИК ===
    "sl_yo.wav": "Ё!",
    "sl_zhik.wav": "ЖИК!",
    "w_yozhik.wav": "Ёжик! Молодец!",

    # === СЛОНИК ===
    "sl_slo.wav": "СЛО!",
    "sl_nik.wav": "НИК!",
    "w_slonik.wav": "Слоник! Молодец!",

    # === ОСЛИК ===
    "sl_os.wav": "ОС!",
    "sl_lik.wav": "ЛИК!",
    "w_oslik.wav": "Ослик! Молодец!",

    # === СВИНКА ===
    "sl_svin.wav": "СВИН!",
    "w_svinka.wav": "Свинка! Молодец!",

    # === ЛОШАДЬ ===
    "sl_lo.wav": "ЛО!",
    "sl_shad.wav": "ШАДЬ!",
    "w_loshad.wav": "Лошадь! Молодец!",

    # === ДОМИК ===
    "sl_do.wav": "ДО!",
    "sl_mik.wav": "МИК!",
    "w_domik.wav": "Домик! Молодец!",

    # === МЯЧИК ===
    "sl_mya.wav": "МЯ!",
    "sl_chik.wav": "ЧИК!",
    "w_myachik.wav": "Мячик! Молодец!",

    # === ЛИСА ===
    "sl_li.wav": "ЛИ!",
    "w_lisa.wav": "Лиса! Молодец!",

    # === КАША ===
    "sl_sha.wav": "ША!",
    "w_kasha.wav": "Каша! Молодец!",

    # === РЫБА ===
    "sl_ry.wav": "РЫ!",
    "sl_ba.wav": "БА!",
    "w_ryba.wav": "Рыба! Молодец!",

    # === МЫШКА ===
    "sl_mysh.wav": "МЫШ!",
    "w_myshka.wav": "Мышка! Молодец!",

    # === КОЗА ===
    "sl_ko.wav": "КО!",
    "sl_za.wav": "ЗА!",
    "w_koza.wav": "Коза! Молодец!",

    # === ОВЦА ===
    "sl_ov.wav": "ОВ!",
    "sl_tsa.wav": "ЦА!",
    "w_ovtsa.wav": "Овца! Молодец!",
    
    # === ВВОДНАЯ ФРАЗА КОМНАТЫ ===
    "words_intro.wav": "Собери картинку из кусочков!"
}

print(f"Запуск озвучки {len(quiz_phrases)} фраз...")

for filename, text in quiz_phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7 
        )
        # Магия Ути-Те (частота 54000)
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
