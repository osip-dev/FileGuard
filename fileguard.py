import hashlib
from pathlib import Path

def hash_file(path):
    """Считает SHA-256 хеш файла по кусочкам (по 64 КБ), 
    чтобы программа не зависала на больших файлах.
    """
    sha256_hash = hashlib.sha256()
    
    # Открываем файл в бинарном режиме чтения ("rb")
    with open(path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
            
    # Возвращаем готовый хеш в виде строки из шестнадцатеричных символов
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    # Тестовая проверка прямо в терминале
    print("=== FileGuard (Этап 1) ===")
    
    # Создадим для теста временный файл, если его нет
    test_file = Path("test.txt")
    if not test_file.exists():
        test_file.write_text("Привет, мир кибербезопасности!", encoding="utf-8")
        print(f"Создан тестовый файл: {test_file.name}")
        
    file_hash = hash_file(test_file)
    print(f"Путь к файлу: {test_file}")
    print(f"SHA-256 хеш: {file_hash}")