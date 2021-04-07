## FastAPI BasicAuth using Cipher
This is a **BasicAuth** implemented single page **FastAPI** server. The user is asked to enter a username and password to be able to navigate to the homepage. After one successful log-in, credentials are stored in the browser and send with every request automatically thus the user does not have to enter every time. The default username is ```admin```, and the default password is ```admin```. Password stored in python dictionary with a ciphered password.

### Polyalhabetic Cipher
Polyalhabetic cipher is used to encode and decode. Different then Ceaser's Cipher, this method **uses a different number of shifts** to randomize the ciphered text. To achieve this a **secret key** is created. This key is repeated to cover the length of the secret string. After this mask is created, every letter from the secret string is shifted corresponded letter's index time forward. Assuming we have a key of different letters, even if the secret string is ```LL``` having the same letter in a row. In ciphered string, the same letters will be represented by different letters. So it could be ```CIPHER(LL) = '8D'```.

### Enigma Cipher
An implementation of a famous Enigma machine from ww2 with **slight modifications to eliminate flaws of the original Enigma machine.** Which is ```ENIGMA(C) != C```. It has **10 different rotors** to choose three of them. The number of the rotors can be increased with a little tweaking with code. It has **20 different plugboards** and uses 2 different plugboards before and after the rotors. Different from the original Enigma machine **the direction between characters might be monodirectional.** And even a character might pair with itself. This achieved by randomly selecting in order to achieve more complex ciphering.

#### Development
- Working on a bug that fails on different offsets than initial offsets. However, this bug does not have an effect on the default offset parameter.
- Comments for the Enigma class are being added.

## How to run locally
```bash
git clone git@github.com:LatifB/FastAPI-Cipher.git
cd FastAPI-Cipher
pip install -r requirements.txt
uvicorn main:app --reload
```
Additionally, you can also run the test with:
```bash
python cipher/test_polycipher.py
python cipher/test_enigma.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)