import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

# Берем мягкий женский голос
style = tts.get_voice_style(voice_name="F4")

# Наш список всех нужных фраз (название файла : текст для Ути)
phrases = {
    # Короткие для режима обучения
    "1.wav": "Один",
    "2.wav": "Два",
    "3.wav": "Три",
    "4.wav": "Четыре",
    "5.wav": "Пять",
    "6.wav": "Шесть",
    "7.wav": "Семь",
    "8.wav": "Восемь",
    "9.wav": "Девять",
    "10.wav": "Десять",
    
    # Вопросы для викторины
    "q1.wav": "Где цифра один?",
    "q2.wav": "Где цифра два?",
    "q3.wav": "Где цифра три?",
    "q4.wav": "Где цифра четыре?",
    "q5.wav": "Где цифра пять?",
    "q6.wav": "Где цифра шесть?",
    "q7.wav": "Где цифра семь?",
    "q8.wav": "Где цифра восемь?",
    "q9.wav": "Где цифра девять?",
    "q10.wav": "Где цифра десять?",
    
    # Реакции на ответы
    "correct.wav": "Правильно! Молодец!",
    "wrong.wav": "Ой, не то! Попробуй еще раз."
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
