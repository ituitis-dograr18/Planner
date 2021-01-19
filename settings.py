DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin":"$pbkdf2-sha256$29000$D0Go9V7rnbO2NqbUGmMshQ$KxkUTcHeUDsh8TMyaLuzhIa2sZIc9OD/0Mwn38qSz04",
    "normaluser":"$pbkdf2-sha256$29000$0fofw3jPmZOyFgLA2HsPwQ$Rz9uAfKOPUQXa3wb4sBhoyq7/D/trxc6CMxjRX9GwUM"
}

ADMIN_USERS = ["admin"]
