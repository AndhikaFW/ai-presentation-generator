import uvicorn

async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    uvicorn.run("main:slides", port=5000, log_level="info")

import generation
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from openai import OpenAI
from dotenv import load_dotenv                                 
load_dotenv()                                                  
api_key = os.getenv("OPENAI_API_KEY")                          

slides = FastAPI()

slides.mount("/static", StaticFiles(directory="static"), name="static")

@slides.post("/prompt/")
async def create_files(title: str = Form(...), author: str = Form(...), theme: str = Form(...)):
                                                                                          
        generator = generation.Generator()
        generator.generate_presentation(title, author, theme)
        chatcontent = """<!DOCTYPE html>                                                                                       
        <html lang="en">
        <head>
            <title>📚 Chat dengan dokumen</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="../static/css/styles.css" rel="stylesheet">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/grids-responsive-min.css">
        </head>
        <body> 
            <div class="content">
                <h1>Generate Presentation Slides 📚</h1>
                <div class="pure-g">
                    <div class="pure-u-1 pure-u-xl-1-2">
                        <br>
                        <form action="/prompt/" enctype="multipart/form-data" method="post">
                            <fieldset>
                                <div class="pure-g">
                                    <div class="pure-u-1 pure-u-md-1-2">
                                        <div>
                                            Presentation title:
                                            <input type="text" name="title" id="title" placeholder="Write any title...">
                                        </div>
                                    </div>
                                    <div class="pure-u-1 pure-u-md-1-2">
                                        <div>
                                            Author's name(optional):
                                            <input type="text" name="author" id="author" placeholder="Write any name...">
                                        </div>
                                    </div>
                                </div>
                                <div class="theme">
                                    Theme
                                    <br>
                                    <select name="theme" id="theme">
                                    <option value="1">Default</option>
                                    <option value="2">Gaia</option>
                                    </select>
                                    <div class="desktop">
                                        <div class="pure-g">
                                            <div class="pure-u-1-2">
                                                <div>
                                                    <h3>Default:</h3>
                                                </div>
                                            </div>
                                            <div class="pure-u-1-2">
                                                <div>
                                                    <h3>Gaia:</h3>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <input type="submit" name="answer" onclick="Load()" class="btn-hover color-3" value="Generate"/>
                                </div>
                            </fieldset>
                        </form>
                    </div>
                    <div id="prompt" class="pure-u-1 pure-u-xl-1-2">
                        <div class="mid">
                            <h2>Prompt:</h2>
                            <embed src="../files/presentation.html">
                            <div class="pure-g">
                            <div class="pure-u-1 pure-u-md-1-2">
                                <span class="button">
                                <a href="../files/presentation.pdf">
                                    <span class="button-background"></span>
                                    <span class="button-text">presentation.pdf</span>
                                </a>
                                </span>
                            </div>
                            <div class="pure-u-1 pure-u-md-1-2">
                                <span class="button">
                                <a href="../files/presentation.ppt">
                                    <span class="button-background"></span>
                                    <span class="button-text">presentation.ppt</span>
                                </a>
                                </span>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div id="load" style="display:none;" class="desktop-xl pure-u-xl-1-2">
                        <div class="mid">
                            <br>
                            <div class="pure-g">
                                <div class="pure-u-2-3">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                                <div class="pure-u-1-3">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                            </div>
                            <div class="pure-g">
                                <div class="pure-u-1-5">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                                <div class="pure-u-4-5">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                            </div>
                            <div class="pure-g">
                                <div class="pure-u-5-6">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                                <div class="pure-u-1-6">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                            </div>
                            <div class="pure-g">
                                <div class="pure-u-1-3">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                                <div class="pure-u-2-3">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                            </div>
                            <div class="pure-g">
                                <div class="pure-u-7-12">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                                <div class="pure-u-5-12">
                                    <span class="load-item">
                                        <span class="load-item-background"></span>
                                    </span>
                                </div>
                            </div>
                            <div class="pure-g">
                            <div class="pure-u-1 pure-u-md-1-2">
                                <span class="button">
                                    <span class="load-item-background"></span>
                                </span>
                            </div>
                            <div class="pure-u-1 pure-u-md-1-2">
                                <span class="button">
                                    <span class="load-item-background"></span>
                                </span>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer">                                 
                Situs ini dibuat dengan <b>Pure</b>
            </div>                                               
            <script>
            function Load() {
                document.getElementById("prompt").style.display = "none";
                document.getElementById("load").style.display = "";
            }
            </script> 
        </body>
        </html>"""                                                                                                                                                                                                     
        return HTMLResponse(content=chatcontent)
@slides.get("/")
async def main():
    return FileResponse('index.html')


