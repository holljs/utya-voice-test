import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

# Берем мягкий женский голос
style = tts.get_voice_style(voice_name="F4")

# Оставляем в списке только то, что нужно переделать
phrases = {
    "9.wav": "дЕвять",
    "q9.wav": "Где цифра дЕвять?"
}

print(f"Начинаем озвучку {len(phrases)} фраз...")

# Запускаем цикл по нашему словарю
for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    
    # Чуть замедляем генерацию (speed=0.7)
    wav, duration = tts.synthesize(
        text=text,
        lang="ru",
        voice_style=style,
        total_steps=10,
        speed=0.7 
    )

    # Частота 54000 даст мультяшный тон
    sf.write(filename, wav.squeeze(), 54000)

print("✅ Готово! Все файлы сохранены, GitHub Actions скоро соберет их в архив.")
