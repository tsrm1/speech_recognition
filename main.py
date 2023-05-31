# pip install openai-whisper
import whisper


def speech_recognition(model='base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe('Black_Star_Mafia_Tusa.mp3')

    with open(f'transcription_{model}.txt', 'w') as file:
        file.write(result['text'])


def main():
    models = {
        1: 'tiny', 
        2: "tiny.en",
        3: 'base', 
        4: "base.en",
        5: 'small', 
        6: "small.en",
        7: 'medium', 
        8: "medium.en",
        9: 'large',
        10: "large-v1",
        11: "large-v2"
        }

    for k, v in models.items():
        print(f'{k}:{v}')

    # model = int(input('Выберите модель передав цифру от 1 до 5: '))
    model = 7
    if model not in models.keys():
        raise KeyError(f'Модели {model} нет в списке!')

    print('Запущен процесс транскрибации, пожалуйста ожидайте...')
    speech_recognition(model=models[model])


if __name__ == '__main__':
    main()