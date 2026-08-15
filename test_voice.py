import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS для сказки «Утя-Колобок»...")

tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# ПРАВИЛА РАЗМЕТКИ SUPERTONIC:
# 1) Ударение (´) ставится на всех ударных гласных: а́ е́ и́ о́ ы́ э́ я́ ю́
# 2) Ударная «у» пишется УДВОЕННОЙ: уу
# 3) Буква «ё» всегда ударная сама по себе

kolobok_phrases = {
    # === ЭКРАН 1: НАЧАЛО (Картинка: tale_kb_1.webp) ===
    # Выбор: Скейтборд (item_kb_skate.webp) или Шарики (item_kb_balloons.webp)
    "kb_step1_q.wav": "Уутя сиде́л до́ма и о́чень скуучал. Реши́л он отпра́виться в весёлое путеше́ствие! На чём же Ууте отпра́виться в пууть?",

    # === ЭКРАН 2: ВСТРЕЧА С ЗАЙКОЙ ===
    # Картинка 2А: tale_kb_skate.webp | Картинка 2Б: tale_kb_balloons.webp
    # Выбор: Бадминтон (item_kb_badminton.webp) или Морс (item_kb_mors.webp)
    "kb_step2_q.wav": "побежа́л Уутя да́льше, а навстре́чу За́йка-попрыга́йка: Стой, Уутя, я тебя́ пойма́ю! Ой, что же предложи́ть За́йке, что́бы он не пойма́л Уутю?",

    # === ЭКРАН 3: ВСТРЕЧА С ВОЛКОМ ===
    # Картинка 3А: tale_kb_badminton.webp | Картинка 3Б: tale_kb_mors.webp
    # Выбор: Шляпа (item_kb_hat.webp) или Тортик (item_kb_cake.webp)
    "kb_step3_q.wav": "За́йка заигра́лся и отвлёкся, а Уутя побежа́л да́льше! А навстре́чу Се́рый Волк: Стой, Уутя, сейча́с я тебя́ пойма́ю! Что же подари́ть Во́лку, что́бы он не пойма́л Уутю?",

    # === ЭКРАН 4: ВСТРЕЧА С МЕДВЕДЕМ ===
    # Картинка 4А: tale_kb_hat.webp | Картинка 4Б: tale_kb_cake.webp
    # Выбор: Подушка (item_kb_pillow.webp) или Пузыри (item_kb_bubbles.webp)
    "kb_step4_q.wav": "Волк так обра́довался пода́рку, что совсе́м забы́л про всё на све́те! А Уутя побежа́л да́льше, и ви́дит — идёт Большо́й Медве́дь: Кто туут шуми́т? Сейча́с пойма́ю! Что же предложи́ть Ми́шке, что́бы он не пойма́л Уутю?",

    # === ЭКРАН 5: ВСТРЕЧА С ЛИСИЧКОЙ ===
    # Картинка 5А: tale_kb_pillow.webp | Картинка 5Б: tale_kb_bubbles.webp
    # Выбор: Розовые очки (item_kb_glasses.webp) или Танцы (item_kb_disco.webp)
    "kb_step5_q.wav": "Ми́шка заулыба́лся и стал до́брым-предо́брым! А Уутя побежа́л да́льше. Вдрууг из кусто́в выхо́дит хи́трая Лиси́чка: Ой, како́й Уутя хоро́шенький, иди́ ко мне́, я тебя́ пойма́ю! Что же придуумать, что́бы перехитри́ть Лиси́чку?",

    # === ЭКРАН 6: ВОЗВРАЩЕНИЕ ДОМОЙ ===
    # Картинка 6А: tale_kb_glasses.webp | Картинка 6Б: tale_kb_fox_dance.webp
    # Выбор: Дискотека (item_kb_party.webp) или Блинчики (item_kb_pancakes.webp)
    "kb_step6_q.wav": "Лиси́чка закружи́лась в та́нце, а Уутя вернуулся домо́й к ба́бушке и де́душке! Они́ так обра́довались, что реши́ли устро́ить пра́здник! Что же устро́ить до́ма?",

    # === ЭКРАН 7: ФИНАЛ ===
    # Картинка 7А: tale_kb_home_party.webp | Картинка 7Б: tale_kb_pancakes.webp
    "kb_step7_final.wav": "Вот и ска́зочке коне́ц, а кто игра́л и слуушал — тот су́пер-молоде́ц!",
}

output_dir = "/var/www/neuro-malysh-backend/audio_assets/tales"
os.makedirs(output_dir, exist_ok=True)

print(f"Запуск синтеза {len(kolobok_phrases)} файлов для сказки «Утя-Колобок»...")

for filename, text in kolobok_phrases.items():
    filepath = os.path.join(output_dir, filename)
    print(f"Генерация: {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.78  # Чёткий сказочный темп для малышей
        )
        sf.write(filepath, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка в {filename}: {e}")

print("✅ Все аудиофайлы для сказки «Утя-Колобок» успешно сгенерированы!")
