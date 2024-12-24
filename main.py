from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - coreapi-coll-e04acc675e654d99a77096de20c90c8a',debug=False,docs_url='/hardcore-pooja-e4aa7a16c1c811ef8cc40242ac12000568/docs',openapi_url='/hardcore-pooja-e4aa7a16c1c811ef8cc40242ac12000568/openapi.json')

app.include_router(router, prefix='/hardcore-pooja-e4aa7a16c1c811ef8cc40242ac12000568/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()