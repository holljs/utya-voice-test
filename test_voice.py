import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === НОВЫЕ ФРАЗЫ ДЛЯ ЦЕПОЧКИ ===
    "chain_remember.wav": "Попробуй запомнить эти предметы за пять секунд!",
    "chain_hide.wav": "Ой! Всё исчезло! Трудно запомнить?",
    "chain_train.wav": "Свяжи эти предметы в одну смешную сказку!",

    # === НОВЫЕ ФРАЗЫ ДЛЯ ГАРДЕРОБНОЙ НАПОЛЕОНА ===
    # === НОВЫЕ ФРАЗЫ ДЛЯ ГАРДЕРОБНОЙ НАПОЛЕОНА ===
    "wardrobe_start.wav": "Сначала нажми на вещь, а потом на полку, куда хочешь её положить! И обязательно придумай смешную причину. Например: Собака сидит на самой верхней полке, потому что охраняет шкаф!",
    "wardrobe_hide.wav": "Магия! Всё исчезло! Расставь вещи по своим местам.",

    # === ИСПРАВЛЕНИЕ ДЛЯ СЛОГОВ ===
    "w_malina.wav": "Малина! Молодец!"
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
