import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Esta es una página</h1>
        <li>Opción 1</li>
        <li>Opción 2</li>
        <li>Opción 3</li>
        <p>
        <p>Soy un párrafo</p>
    """
    #return {'name': 'Platzi'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()