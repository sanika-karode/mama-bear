import pickle

from pathlib import Path
import streamlit_authenticator as stauth


names = ["pp", "rj"]
usernames = ["rp", "sk"]
passwords = ["pprp", "rjsk"]

hashed_passwords = stauth.Hasher(passwords).generate()

print(Path(__file__).parent)

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

