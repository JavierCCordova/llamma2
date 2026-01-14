from functools import lru_cache             ## guarda en cache la session o el objeto creado
from  pydantic_settings import BaseSettings ## Generar clases para acceso al env.


class Settings(BaseSettings):
    SECRET_KEY  :   str
    ACCESS_TOKEN_EXPIRE_MINUTES :   int=30
    MONGO_URL   :   str
    DB_NAME     :   str
    
    class Config:
        """
        Gestiona la configuración de la aplicación obteniendo valores desde
        variables de entorno.

        Esta clase centraliza el acceso a las variables definidas en el archivo
        `.env` o en el entorno del sistema.

        Attributes:
            env (str): Nombre del entorno de ejecución (por ejemplo: 'dev', 'prod').
        """
        env_file    =   ".env"
        
        
@lru_cache
def getSettings():
    """
    Carga la configuración de la aplicación desde las variables de entorno.

    Returns:
        Settings: Instancia de la clase `Settings` con todos los valores
        cargados desde el archivo `.env` o desde el entorno del sistema.
    """
    return Settings()

settings    =   getSettings()
# BaseSettings lee automáticamente .env
# lru_cache() evita que se lea el archivo cada vez.