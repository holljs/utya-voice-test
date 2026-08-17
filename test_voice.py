import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS для сказки «Утя-Колобок»...")

tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

kolobok_phrases = {
 
    # === ШАГ 3: ВСТРЕЧА С ВОЛКОМ ===
    "kb_q3.wav": "Уутя побежа́л да́льше, а навстре́чу Се́рый Волк! Что пода́рим Во́лку?",
    "kb_a3_hat.wav": "Красота́! Волк наде́л шля́пу и стал насто́ящим джентльме́ном!",
    "kb_a3_cake.wav": "Ням-ня́м! Волк о́чень лю́бит сла́дкий то́ртик!",

    # === ШАГ 6: ДОМА У БАБУШКИ И ДЕДУШКИ ===
    "kb_q6.wav": "Уутя вернуулся домо́й к ба́бушке и де́душке! Что же нам устро́оить?",
    "kb_a6_pancakes.wav": "Вкусноти́ща! Буудем куушать горя́чие бли́нчики с ча́ем!",
    "kb_a6_bath.wav": "Бууль-бууль! Пе́нная вечери́нка с ууточками в ва́нной!",

    # === ФИНАЛ ===
    "kb_end.wav": "Вот и ска́зочке коне́ц, а кто игра́л и слуушал — тот суупер-молоде́ц!",
}

print(f"Запуск синтеза {len(kolobok_phrases)} файлов для сказки «Утя-Колобок»...")

for filename, text in kolobok_phrases.items():
    print(f"Генерация: {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.78
        )
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка в {filename}: {e}")

print("✅ Все аудиофайлы для сказки «Утя-Колобок» полностью готовы!")
