from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from titanis import Titanis

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Инициализация Titanis
tt = Titanis(
    psy_cues=True,
    psy_cues_normalization='words',
    psy_dict=True,
    psy_dict_normalization='abs',
    syntax=True,
    discourse=True,
    frustration_clf=True,
    emotive_srl=True
)

# Модель для передачи текста через API
class TextRequest(BaseModel):
    text: str

# Функция для анализа текста с помощью Titanis
def analyze_text(text: str):
    try:
        result = tt(text)  # Анализируем текст
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing text: {e}")

# Роут для обработки POST-запросов с текстом
@app.post("/analyze/")
async def analyze(request: TextRequest):
    text = request.text
    analysis_result = analyze_text(text)
    return analysis_result
