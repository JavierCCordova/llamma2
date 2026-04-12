from domain.playwirght.ports.dni import DniPort
from playwright.async_api import async_playwright

class RobotDniInfra(DniPort):
    
    def __init__(self, url: str):
        self.url_base   =   url
        
    async def getNameWeb(self, dni: str)-> list:        
        async with async_playwright() as p:            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:                
                await page.goto(self.url_base)
                await page.get_by_placeholder("Número de DNI").fill(dni)
                await page.get_by_role("button", name="Buscar datos").click()
                                
                await page.locator("tbody tr td").first.wait_for(state="visible", timeout=10000)
                 
                datos = await page.locator("tbody tr").first.locator("td").all_inner_texts()
                return ' '.join(datos)
                
            except Exception as e:
                print(f"Error en el Robot DNI: {e}")
                return ''
            
            finally: 
                await browser.close()