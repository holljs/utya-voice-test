import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS для Сказки 3 (Утя-Шапочка)...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

story_phrases = {
    # === РЕАКЦИИ НА ОТВЕТЫ (ОЗВУЧКА СЦЕН) ===
    # Сцена 2
    "rh_a2_abs.wav": "Фу-фу-фу! Во́лк съел мы́ло и на́чал пуска́ть из па́сти мы́льные пузыри́! Бу́ль-бу́ль-бу́ль!",
    
    # Сцена 5
    "rh_a5_norm.wav": "У́тя наде́л очки́ и закрича́л! Ого́! Под одея́лом сиди́т наш знако́мый Во́лк-шутни́к!",
    
    # Финал всей сказки
    "rh_end.wav": "Кака́я весёлая и до́брая ска́зка у нас получи́лась! Ба́бушка, У́тя и Во́лк ста́ли лу́чшими друзья́ми!"
}

print(f"Запуск синтеза {len(story_phrases)} файлов для Сказки 3 (Утя-Шапочка)...")

for filename, text in story_phrases.items():
    print(f"Генерация: {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.75  # Идеальная скорость для детского восприятия
        )
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка в {filename}: {e}")

print("✅ Все файлы озвучки для Сказки 3 «Утя-Шапочка» полностью готовы!")
