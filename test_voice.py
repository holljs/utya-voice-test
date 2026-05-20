import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

# Берем мягкий женский голос
style = tts.get_voice_style(voice_name="F4")

text = "Привет, мой хороший! <laugh> Утя очень рада тебя видеть! Давай скорее играть?"

print("Синтез...")
# Чуть замедляем генерацию (speed=0.9), потому что смена частоты её ускорит
wav, duration = tts.synthesize(
    text=text,
    lang="ru",
    voice_style=style,
    total_steps=10,
    speed=0.7            # Минимально разрешенная скорость
)

final_file = "utya_test.wav"

# Частота 54000 даст мультяшный тон, но не сделает речь слишком быстрой
sf.write(final_file, wav.squeeze(), 54000)

print(f"Готово! Мультяшная Утя сохранена как {final_file}")
