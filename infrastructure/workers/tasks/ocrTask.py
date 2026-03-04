from infrastructure.workers.celeryApp import celery_app
from infrastructure.persistence.mongodb.connection import MongoClientManager
from infrastructure.persistence.ai.gemini.connection import GeminiConnexion
from infrastructure.persistence.mongodb.geminiRepository import GeminiRepository

from application.robots.geminiUSeCase import GeminiUseCase
from infrastructure.persistence.ai.gemini.repositoryElement import GeminiRepositoryElement


@celery_app.task
def process_ocr(file_bytes, features):

    mongoClient = MongoClientManager.getCliente()
    gemini      = GeminiConnexion()
    geminiRepo  = GeminiRepository(mongoClient)
    usecase     = GeminiUseCase(
        GeminiRepositoryElement(geminiRepo, gemini)
    )

    return usecase.getDataFile(file_bytes, *features)


@celery_app.task
def test_task(x, y):
    print("Ejecutando tarea en WORKER")
    return x + y