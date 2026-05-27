import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Словарь: имя файла -> текст с ударениями (для 'у' под ударением — удваиваем в 'уу')
phrases = {
    # ---------- КОМНАТА: СЛОГИ И СЛОВА ----------
    # Слова целиком (для карточек обучения)
    "w_lisa.wav": "Лиса́",
    "w_ryba.wav": "Ры́ба",
    "w_kasha.wav": "Ка́ша",
    "w_raketa.wav": "Раке́та",
    "w_mashina.wav": "Маши́на",
    "w_sobaka.wav": "Соба́ка",

    # Отдельные слоги (озвучка кирпичиков при нажатии/перетаскивании)
    "sl_li.wav": "Ли́",
    "sl_sa.wav": "Са́",
    "sl_ry.wav": "Ры́",
    "sl_ba.wav": "Ба́",
    "sl_ka.wav": "Ка́",
    "sl_sha.wav": "Ша́",
    "sl_ra.wav": "Ра́",
    "sl_ke.wav": "Ке́",
    "sl_ta.wav": "Та́",
    "sl_ma.wav": "Ма́",
    "sl_shi.wav": "Ши́",
    "sl_na.wav": "На́",
    "sl_so.wav": "Со́",

    # Системные фразы для Слогов
    "words_intro.wav": "Собери́ сло́во из кусо́чков!",
    "words_win.wav": "Гениа́льно! Ты собра́л все слова́!",

    # ---------- КОМНАТА: МЕНТАЛЬНЫЙ СОРОБАН ----------
    # Инструкции
    "soroban_intro.wav": "Дава́й посчита́ем, дви́гай ко́сточки!",
    
    # Озвучка чисел от 1 до 10 (цифры с 'у' удвоены)
    "num_1.wav": "Оди́н",
    "num_2.wav": "Два́",
    "num_3.wav": "Три́",
    "num_4.wav": "Четы́ре",
    "num_5.wav": "Пя́ть",
    "num_6.wav": "Ше́сть",
    "num_7.wav": "Се́мь",
    "num_8.wav": "Во́семь",
    "num_9.wav": "Де́вять",
    "num_10.wav": "Де́сять",
    
    # Реакция на успех в счёте
    "soroban_win.wav": "Великоле́пно! Ты счита́ешь как настоя́щий мента́льный матема́тик!"
}

print(f"Запуск озвучки {len(phrases)} фраз...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7
        )
        # Сохраняем файл на диск
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все новые звуковые файлы для 5+ успешно сгенерированы в текущую папку.")
