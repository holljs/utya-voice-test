import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === СКАЗКА: ЛЕСНОЙ ОБМЕН (ЦЕПОЧКА) ===
    "chain_story_1.wav": "Одна́жды.. хи́трая лиса́.. нашла́ под де́ревом.. краси́ивую коро́обку.",
    "chain_story_2.wav": "Она́ обра́довалась.. и поду́умала, что внутри́ лежи́т.. сла́адкая я́года.",
    "chain_story_3.wav": "Но когда́ она́ откры́ыла коро́бку.. та́м оказа́лась.. то́олько бе́лая ко́ость.",
    "chain_story_4.wav": "В э́тот моме́нт.. из кусто́ов вы́бежала.. голо́одная соба́ака.",
    "chain_story_5.wav": "Лиса́ отдала́ ко́сть.. а соба́ака подари́ла ей.. большо́ой жёлудь.",
    "chain_story_6.wav": "Лиса́ расколо́ла жёлудь.. а внутри́ оказа́лся.. густо́ой.. сла́адкий мёёд!"
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
        # Вернули правильную частоту 24000!
        sf.write(filename, wav.squeeze(), 24000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
