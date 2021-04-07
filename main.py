import secrets
from fastapi import Request
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates

from cipher.polycipher import PolyCipher
# from cipher.enigma import Enigma


DEFAULT_PASSWORD = 'admin'

app = FastAPI()
security = HTTPBasic()
templates = Jinja2Templates(directory='templates')

cipher = PolyCipher()
password = cipher.encode(DEFAULT_PASSWORD)

users = {'admin': password,}

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    '''Handles the authorization'''

    # Check if user exist
    username_exist = credentials.username in users

    # if users exist takes password decodes and compares
    if username_exist:
        correct_password = secrets.compare_digest(
            users[credentials.username],
            cipher.encode(credentials.password)
        )
    else:
        correct_password = False

    # if users does not exist or incorrect password
    # ask for authentication
    if not (username_exist and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password. Go to /Sign-in",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def root(request: Request, username: str = Depends(get_current_username)):
    context = {"request": request, 'username': username}
    return templates.TemplateResponse('index.html', context)
