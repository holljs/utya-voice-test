import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

phrases = {
    "wind_intro.wav": "Сыграем в ветерóк! Подууй на вертушку что есть си́лы!",
    "wind_good.wav": "Огó, как круутится! Ты настоя́щий урагáн!",
    "wind_more.wav": "Подууй ещё сильне́е!"
}

print(f"Запуск озвучки тренажера дыхания...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    wav, duration = tts.synthesize(
        text=text,
        lang="ru",
        voice_style=style,
        total_steps=10,
        speed=0.7 
    )
    sf.write(filename, wav.squeeze(), 54000)

print("✅ Готово! Звуки для ветерка записаны.")
