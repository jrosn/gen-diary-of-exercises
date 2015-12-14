# Генератор дневника самоконтроля
## Установка
### Ubuntu
```bash
# Устанавливаем git
sudo apt-get install -y git
# Клонируем репозиторий
git clone https://github.com/rmnssnvsk/gen-diary-of-exercises && cd gen-diary-of-exercises
# Запускаем установку
sudo python3 setup.py install
```

## Использование
```
gen-diary-of-exercises --start-date YYYY-MM-DD --finish-date YYYY-MM-DD
```
* `--start-date` - дата, с которой начинаем "вести" дневник самоконтроля
* `--finish-date` - дата, на которой заканчиваем "вести" дневник самоконтроля (не включительно)
